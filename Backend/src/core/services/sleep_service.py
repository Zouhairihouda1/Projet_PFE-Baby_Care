# 📁 backend/src/core/services/sleep_service.py
from typing import List, Optional, Dict, Any
from datetime import datetime, date, timedelta, time
from sqlalchemy.orm import Session
from ...db.repositories.sleep_repository import SleepRepository
from ...core.models.sleep import (
    SleepCreate, SleepUpdate, SleepResponse, 
    SleepStatistics, SleepTrend, SleepChartData,
    SleepRhythm, SleepRecommendation
)
from ...db.models.sleep_model import SleepModel, SleepType
from ..exceptions import NotFoundException, ValidationException
from ..utils.date_utils import calculate_baby_age

class SleepService:
    def __init__(self, db: Session):
        self.repository = SleepRepository(db)
    
    def create_sleep_session(self, sleep_data: SleepCreate, user_id: int) -> SleepResponse:
        """Créer une nouvelle session de sommeil"""
        # Validation
        if sleep_data.end_time and sleep_data.start_time:
            if sleep_data.end_time < sleep_data.start_time:
                raise ValidationException("End time cannot be before start time")
            
            # Calcul automatique de la durée
            duration = (sleep_data.end_time - sleep_data.start_time).total_seconds() / 60
            sleep_data.duration_minutes = int(duration)
        
        # Vérifier s'il y a déjà une session en cours
        current_session = self.repository.get_current_sleep_session(sleep_data.baby_id)
        if current_session and not sleep_data.end_time:
            raise ValidationException("A sleep session is already in progress. End it first.")
        
        # Créer l'entrée
        db_sleep = SleepModel(**sleep_data.dict(), user_id=user_id)
        self.repository.create(db_sleep)
        
        return SleepResponse.model_validate(db_sleep)
    
    def get_sleep_session(self, sleep_id: int, user_id: int) -> SleepResponse:
        """Récupérer une session de sommeil par ID"""
        sleep = self.repository.get(sleep_id)
        if not sleep or sleep.user_id != user_id:
            raise NotFoundException(f"Sleep session with id {sleep_id} not found")
        return SleepResponse.model_validate(sleep)
    
    def get_baby_sleep_sessions(
        self, 
        baby_id: int, 
        user_id: int,
        skip: int = 0, 
        limit: int = 100,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        sleep_type: Optional[SleepType] = None
    ) -> List[SleepResponse]:
        """Récupérer toutes les sessions de sommeil d'un bébé"""
        sessions = self.repository.get_by_baby(
            baby_id=baby_id,
            skip=skip,
            limit=limit,
            start_date=start_date,
            end_date=end_date,
            sleep_type=sleep_type
        )
        
        # Filtrer par user_id
        user_sessions = [s for s in sessions if s.user_id == user_id]
        
        return [SleepResponse.model_validate(s) for s in user_sessions]
    
    def update_sleep_session(
        self, 
        sleep_id: int, 
        sleep_data: SleepUpdate, 
        user_id: int
    ) -> SleepResponse:
        """Mettre à jour une session de sommeil"""
        sleep = self.repository.get(sleep_id)
        if not sleep or sleep.user_id != user_id:
            raise NotFoundException(f"Sleep session with id {sleep_id} not found")
        
        # Mettre à jour les champs
        update_data = sleep_data.model_dump(exclude_unset=True)
        
        # Recalculer la durée si end_time est mis à jour
        if 'end_time' in update_data and sleep.start_time:
            end_time = update_data['end_time']
            if isinstance(end_time, str):
                end_time = datetime.fromisoformat(end_time.replace('Z', '+00:00'))
            
            if end_time < sleep.start_time:
                raise ValidationException("End time cannot be before start time")
            
            duration = (end_time - sleep.start_time).total_seconds() / 60
            update_data['duration_minutes'] = int(duration)
        
        for field, value in update_data.items():
            setattr(sleep, field, value)
        
        sleep.updated_at = datetime.now()
        self.repository.db.commit()
        self.repository.db.refresh(sleep)
        
        return SleepResponse.model_validate(sleep)
    
    def delete_sleep_session(self, sleep_id: int, user_id: int) -> bool:
        """Supprimer une session de sommeil"""
        sleep = self.repository.get(sleep_id)
        if not sleep or sleep.user_id != user_id:
            raise NotFoundException(f"Sleep session with id {sleep_id} not found")
        
        self.repository.delete(sleep_id)
        return True
    
    def start_sleep_session(self, baby_id: int, user_id: int, sleep_type: SleepType) -> SleepResponse:
        """Commencer une nouvelle session de sommeil"""
        # Vérifier s'il y a déjà une session en cours
        current_session = self.repository.get_current_sleep_session(baby_id)
        if current_session:
            raise ValidationException("A sleep session is already in progress")
        
        sleep_data = SleepCreate(
            baby_id=baby_id,
            type=sleep_type,
            start_time=datetime.now()
        )
        
        return self.create_sleep_session(sleep_data, user_id)
    
    def end_sleep_session(self, sleep_id: int, user_id: int, quality: Optional[str] = None) -> SleepResponse:
        """Terminer une session de sommeil en cours"""
        sleep = self.repository.get(sleep_id)
        if not sleep or sleep.user_id != user_id:
            raise NotFoundException(f"Sleep session with id {sleep_id} not found")
        
        if sleep.end_time:
            raise ValidationException("Sleep session already ended")
        
        update_data = {
            'end_time': datetime.now()
        }
        
        if quality:
            update_data['quality'] = quality
        
        return self.update_sleep_session(sleep_id, SleepUpdate(**update_data), user_id)
    
    def get_current_sleep_session(self, baby_id: int, user_id: int) -> Optional[SleepResponse]:
        """Récupérer la session de sommeil en cours"""
        session = self.repository.get_current_sleep_session(baby_id)
        if session and session.user_id == user_id:
            return SleepResponse.model_validate(session)
        return None
    
    def get_today_sleep_sessions(self, baby_id: int, user_id: int) -> List[SleepResponse]:
        """Récupérer les sessions de sommeil d'aujourd'hui"""
        sessions = self.repository.get_today_sleep_sessions(baby_id)
        user_sessions = [s for s in sessions if s.user_id == user_id]
        return [SleepResponse.model_validate(s) for s in user_sessions]
    
    def get_sleep_statistics(
        self, 
        baby_id: int, 
        user_id: int,
        target_date: Optional[date] = None
    ) -> SleepStatistics:
        """Récupérer les statistiques de sommeil"""
        stats_dict = self.repository.get_sleep_statistics(baby_id, target_date)
        return SleepStatistics(**stats_dict)
    
    def get_sleep_trends(
        self, 
        baby_id: int, 
        user_id: int,
        days: int = 7
    ) -> List[SleepTrend]:
        """Récupérer les tendances de sommeil"""
        trends_data = self.repository.get_sleep_trends(baby_id, days)
        return [SleepTrend(**data) for data in trends_data]
    
    def get_chart_data(
        self, 
        baby_id: int, 
        user_id: int,
        days: int = 7
    ) -> SleepChartData:
        """Récupérer les données pour les graphiques"""
        chart_data = self.repository.get_chart_data(baby_id, days)
        return SleepChartData(**chart_data)
    
    def get_sleep_patterns(
        self, 
        baby_id: int, 
        user_id: int,
        days: int = 30
    ) -> Dict[str, Any]:
        """Analyser les patterns de sommeil"""
        return self.repository.get_sleep_patterns(baby_id, days)
    
    def get_sleep_rhythm_by_age(self, baby_age_days: int) -> SleepRhythm:
        """Obtenir le rythme de sommeil recommandé par âge"""
        if baby_age_days < 90:  # 0-3 mois
            return SleepRhythm(
                age_group="0-3m",
                total_sleep_hours={"day": 5, "night": 9},
                nap_count=4,
                nap_duration_range={"min": 30, "max": 120},
                bedtime_range={"start": time(19, 0), "end": time(20, 0)},
                wakeup_range={"start": time(6, 0), "end": time(7, 0)}
            )
        elif baby_age_days < 180:  # 3-6 mois
            return SleepRhythm(
                age_group="3-6m",
                total_sleep_hours={"day": 4, "night": 10},
                nap_count=3,
                nap_duration_range={"min": 45, "max": 90},
                bedtime_range={"start": time(19, 0), "end": time(20, 0)},
                wakeup_range={"start": time(6, 0), "end": time(7, 0)}
            )
        elif baby_age_days < 365:  # 6-12 mois
            return SleepRhythm(
                age_group="6-12m",
                total_sleep_hours={"day": 3, "night": 11},
                nap_count=2,
                nap_duration_range={"min": 60, "max": 120},
                bedtime_range={"start": time(19, 0), "end": time(20, 0)},
                wakeup_range={"start": time(6, 0), "end": time(7, 0)}
            )
        else:  # 12-24 mois
            return SleepRhythm(
                age_group="12-24m",
                total_sleep_hours={"day": 2, "night": 11},
                nap_count=1,
                nap_duration_range={"min": 90, "max": 180},
                bedtime_range={"start": time(19, 0), "end": time(20, 0)},
                wakeup_range={"start": time(6, 0), "end": time(7, 0)}
            )
    
    def get_sleep_recommendations(
        self, 
        baby_id: int, 
        user_id: int,
        baby_age_days: int
    ) -> List[SleepRecommendation]:
        """Générer des recommandations personnalisées"""
        recommendations_data = self.repository.get_sleep_recommendations(baby_id, baby_age_days)
        return [SleepRecommendation(**rec) for rec in recommendations_data]
    
    def calculate_sleep_score(self, baby_id: int, user_id: int, days: int = 7) -> Dict[str, Any]:
        """Calculer un score de sommeil global"""
        stats = self.get_sleep_statistics(baby_id, user_id)
        trends = self.get_sleep_trends(baby_id, user_id, days)
        
        if not trends:
            return {"score": 0, "components": {}}
        
        # Calculer différents composants du score
        duration_score = self._calculate_duration_score(stats.total_sleep_today_minutes)
        consistency_score = stats.bedtime_consistency
        quality_score = (stats.average_quality_score / 5) * 100 if hasattr(stats, 'average_quality_score') else 50
        
        # Score global (pondéré)
        total_score = (
            duration_score * 0.4 +
            consistency_score * 0.3 +
            quality_score * 0.3
        )
        
        return {
            "score": round(total_score, 1),
            "components": {
                "duration": round(duration_score, 1),
                "consistency": round(consistency_score, 1),
                "quality": round(quality_score, 1)
            },
            "interpretation": self._interpret_sleep_score(total_score)
        }
    
    def _calculate_duration_score(self, total_minutes: float) -> float:
        """Calculer le score de durée basé sur les recommandations d'âge"""
        # Pour un bébé de 6 mois (exemple)
        recommended_minutes = 14 * 60  # 14h
        deviation = abs(total_minutes - recommended_minutes)
        
        # Score de 0-100, pénalité pour écart
        if deviation == 0:
            return 100
        elif deviation <= 60:  # ±1h
            return 80
        elif deviation <= 120:  # ±2h
            return 60
        elif deviation <= 180:  # ±3h
            return 40
        else:
            return 20
    
    def _interpret_sleep_score(self, score: float) -> str:
        """Interpréter le score de sommeil"""
        if score >= 85:
            return "Excellent - Sommeil très sain et régulier"
        elif score >= 70:
            return "Bon - Sommeil généralement bon avec quelques améliorations possibles"
        elif score >= 50:
            return "Moyen - Quelques problèmes à adresser"
        else:
            return "À améliorer - Consultez les recommandations pour des suggestions"
    
    def generate_sleep_report(
        self, 
        baby_id: int, 
        user_id: int,
        start_date: date, 
        end_date: date
    ) -> Dict[str, Any]:
        """Générer un rapport de sommeil complet"""
        # Calculer la période
        days = (end_date - start_date).days + 1
        
        # Récupérer les données
        stats = self.get_sleep_statistics(baby_id, user_id)
        trends = self.get_sleep_trends(baby_id, user_id, days)
        patterns = self.get_sleep_patterns(baby_id, user_id, days)
        score = self.calculate_sleep_score(baby_id, user_id, days)
        
        # Calculer les totaux et moyennes
        total_sleep_hours = sum(t.total_sleep_minutes for t in trends) / 60
        avg_daily_sleep = total_sleep_hours / days if days > 0 else 0
        
        # Identifier les patterns
        best_day = max(trends, key=lambda x: x.total_sleep_minutes) if trends else None
        worst_day = min(trends, key=lambda x: x.total_sleep_minutes) if trends else None
        
        return {
            "period": {
                "start_date": start_date.isoformat(),
                "end_date": end_date.isoformat(),
                "days": days
            },
            "summary": {
                "total_sleep_hours": round(total_sleep_hours, 1),
                "average_daily_sleep_hours": round(avg_daily_sleep, 1),
                "average_naps_per_day": sum(t.nap_count for t in trends) / days if days > 0 else 0,
                "sleep_score": score
            },
            "patterns": patterns,
            "best_day": best_day,
            "worst_day": worst_day,
            "recommendations": self.get_sleep_recommendations(baby_id, user_id, 180)  # exemple: 6 mois
        }
