# 📁 backend/src/core/services/feeding_service.py
from typing import List, Optional, Dict, Any
from datetime import datetime, date, timedelta
from sqlalchemy.orm import Session
from ...db.repositories.feeding_repository import FeedingRepository
from ...core.models.feeding import (
    FeedingCreate, FeedingUpdate, FeedingResponse, 
    FeedingStatistics, FeedingTrend, FeedingChartData
)
from ...db.models.feeding_model import FeedingModel
from ..exceptions import NotFoundException, ValidationException

class FeedingService:
    def __init__(self, db: Session):
        self.repository = FeedingRepository(db)
    
    def create_feeding(self, feeding_data: FeedingCreate, user_id: int) -> FeedingResponse:
        """Créer un nouveau repas"""
        # Validation supplémentaire
        if feeding_data.end_time and feeding_data.start_time:
            if feeding_data.end_time < feeding_data.start_time:
                raise ValidationException("End time cannot be before start time")
            
            # Calcul automatique de la durée
            duration = (feeding_data.end_time - feeding_data.start_time).total_seconds() / 60
            feeding_data.duration_minutes = int(duration)
        
        # Vérifier les quantités selon le type
        if feeding_data.type == "breast_milk" or feeding_data.type == "formula" or feeding_data.type == "water":
            if feeding_data.quantity_ml is None:
                raise ValidationException("Quantity in ml is required for liquid feeding")
        
        if feeding_data.type == "solid_food":
            if feeding_data.quantity_grams is None:
                raise ValidationException("Quantity in grams is required for solid food")
            if not feeding_data.solid_food_type:
                raise ValidationException("Solid food type is required for solid food")
        
        # Créer l'entrée en base
        db_feeding = FeedingModel(**feeding_data.dict(), user_id=user_id)
        self.repository.create(db_feeding)
        
        return FeedingResponse.from_orm(db_feeding)
    
    def get_feeding(self, feeding_id: int, user_id: int) -> FeedingResponse:
        """Récupérer un repas par ID"""
        feeding = self.repository.get(feeding_id)
        if not feeding or feeding.user_id != user_id:
            raise NotFoundException(f"Feeding with id {feeding_id} not found")
        return FeedingResponse.from_orm(feeding)
    
    def get_baby_feedings(
        self, 
        baby_id: int, 
        user_id: int,
        skip: int = 0, 
        limit: int = 100,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> List[FeedingResponse]:
        """Récupérer tous les repas d'un bébé"""
        feedings = self.repository.get_by_baby(
            baby_id=baby_id,
            skip=skip,
            limit=limit,
            start_date=start_date,
            end_date=end_date
        )
        
        # Filtrer par user_id (sécurité)
        user_feedings = [f for f in feedings if f.user_id == user_id]
        
        return [FeedingResponse.from_orm(f) for f in user_feedings]
    
    def update_feeding(
        self, 
        feeding_id: int, 
        feeding_data: FeedingUpdate, 
        user_id: int
    ) -> FeedingResponse:
        """Mettre à jour un repas"""
        feeding = self.repository.get(feeding_id)
        if not feeding or feeding.user_id != user_id:
            raise NotFoundException(f"Feeding with id {feeding_id} not found")
        
        # Mettre à jour les champs
        update_data = feeding_data.dict(exclude_unset=True)
        
        # Recalculer la durée si end_time est mis à jour
        if 'end_time' in update_data and feeding.start_time:
            end_time = update_data['end_time']
            if isinstance(end_time, str):
                end_time = datetime.fromisoformat(end_time.replace('Z', '+00:00'))
            
            if end_time < feeding.start_time:
                raise ValidationException("End time cannot be before start time")
            
            duration = (end_time - feeding.start_time).total_seconds() / 60
            update_data['duration_minutes'] = int(duration)
        
        for field, value in update_data.items():
            setattr(feeding, field, value)
        
        feeding.updated_at = datetime.now()
        self.repository.db.commit()
        self.repository.db.refresh(feeding)
        
        return FeedingResponse.from_orm(feeding)
    
    def delete_feeding(self, feeding_id: int, user_id: int) -> bool:
        """Supprimer un repas"""
        feeding = self.repository.get(feeding_id)
        if not feeding or feeding.user_id != user_id:
            raise NotFoundException(f"Feeding with id {feeding_id} not found")
        
        self.repository.delete(feeding_id)
        return True
    
    def get_today_feedings(self, baby_id: int, user_id: int) -> List[FeedingResponse]:
        """Récupérer les repas d'aujourd'hui"""
        feedings = self.repository.get_today_feedings(baby_id)
        user_feedings = [f for f in feedings if f.user_id == user_id]
        return [FeedingResponse.from_orm(f) for f in user_feedings]
    
    def get_last_feeding(self, baby_id: int, user_id: int) -> Optional[FeedingResponse]:
        """Récupérer le dernier repas"""
        feeding = self.repository.get_last_feeding(baby_id)
        if feeding and feeding.user_id == user_id:
            return FeedingResponse.from_orm(feeding)
        return None
    
    def get_feeding_statistics(
        self, 
        baby_id: int, 
        user_id: int,
        target_date: Optional[date] = None
    ) -> FeedingStatistics:
        """Récupérer les statistiques des repas"""
        # Vérifier que le bébé appartient à l'utilisateur
        # (implémenter cette vérification selon votre modèle)
        
        stats_dict = self.repository.get_feeding_statistics(baby_id, target_date)
        return FeedingStatistics(**stats_dict)
    
    def get_feeding_trends(
        self, 
        baby_id: int, 
        user_id: int,
        days: int = 7
    ) -> List[FeedingTrend]:
        """Récupérer les tendances des repas"""
        trends_data = self.repository.get_feeding_trends(baby_id, days)
        return [FeedingTrend(**data) for data in trends_data]
    
    def get_chart_data(
        self, 
        baby_id: int, 
        user_id: int,
        days: int = 7
    ) -> FeedingChartData:
        """Récupérer les données pour les graphiques"""
        chart_data = self.repository.get_chart_data(baby_id, days)
        return FeedingChartData(**chart_data)
    
    def calculate_daily_goal(self, baby_id: int, baby_age_days: int) -> Dict[str, float]:
        """Calculer les objectifs quotidiens selon l'âge du bébé"""
        goals = {}
        
        if baby_age_days <= 180:  # Moins de 6 mois
            goals['total_ml'] = 150 * baby_age_days / 30  # Formule approximative
            goals['feedings_count'] = 8  # 8 repas par jour
        elif baby_age_days <= 365:  # 6-12 mois
            goals['total_ml'] = 900  # ml par jour
            goals['solid_food_grams'] = 200  # grammes de nourriture solide
            goals['feedings_count'] = 6  # 6 repas par jour
        else:  # Plus de 12 mois
            goals['total_ml'] = 500  # ml de lait
            goals['solid_food_grams'] = 500  # grammes de nourriture solide
            goals['feedings_count'] = 4  # 4 repas par jour
        
        return goals
    
    def get_feeding_schedule(
        self, 
        baby_id: int, 
        user_id: int,
        date: date
    ) -> List[Dict[str, Any]]:
        """Générer un planning de repas pour la journée"""
        # Récupérer les repas existants
        start_datetime = datetime.combine(date, datetime.min.time())
        end_datetime = start_datetime + timedelta(days=1)
        
        existing_feedings = self.repository.get_by_baby(
            baby_id=baby_id,
            start_date=start_datetime,
            end_date=end_datetime
        )
        
        # Générer des créneaux suggérés
        schedule = []
        
        # Heures typiques pour les repas
        typical_times = ['08:00', '10:00', '12:00', '15:00', '18:00', '20:00', '23:00']
        
        for time_str in typical_times:
            time_obj = datetime.strptime(time_str, '%H:%M').time()
            schedule_datetime = datetime.combine(date, time_obj)
            
            # Vérifier si un repas existe déjà à cette heure
            has_feeding = any(
                abs((f.start_time - schedule_datetime).total_seconds()) < 3600
                for f in existing_feedings
            )
            
            schedule.append({
                'scheduled_time': schedule_datetime,
                'has_feeding': has_feeding,
                'suggested_type': 'breast_milk' if time_str in ['08:00', '20:00', '23:00'] else 'solid_food'
            })
        
        return schedule
