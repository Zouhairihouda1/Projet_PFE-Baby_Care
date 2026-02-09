# 📁 backend/src/db/repositories/sleep_repository.py
from typing import List, Optional, Dict, Any, Tuple
from datetime import datetime, timedelta, date, time
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, func, extract, case
from ...db.models.sleep_model import SleepModel, SleepType, SleepQuality
from .base_repository import BaseRepository

class SleepRepository(BaseRepository[SleepModel]):
    def __init__(self, db: Session):
        super().__init__(db, SleepModel)
    
    def get_by_baby(
        self, 
        baby_id: int, 
        skip: int = 0, 
        limit: int = 100,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        sleep_type: Optional[SleepType] = None
    ) -> List[SleepModel]:
        query = self.db.query(SleepModel).filter(
            SleepModel.baby_id == baby_id
        )
        
        if start_date:
            query = query.filter(SleepModel.start_time >= start_date)
        if end_date:
            query = query.filter(SleepModel.start_time <= end_date)
        if sleep_type:
            query = query.filter(SleepModel.type == sleep_type)
        
        return query.order_by(SleepModel.start_time.desc()).offset(skip).limit(limit).all()
    
    def get_today_sleep_sessions(self, baby_id: int) -> List[SleepModel]:
        today = datetime.now().date()
        tomorrow = today + timedelta(days=1)
        
        return self.db.query(SleepModel).filter(
            SleepModel.baby_id == baby_id,
            SleepModel.start_time >= datetime.combine(today, datetime.min.time()),
            SleepModel.start_time < datetime.combine(tomorrow, datetime.min.time())
        ).order_by(SleepModel.start_time.desc()).all()
    
    def get_current_sleep_session(self, baby_id: int) -> Optional[SleepModel]:
        """Récupérer la session de sommeil en cours (sans end_time)"""
        return self.db.query(SleepModel).filter(
            SleepModel.baby_id == baby_id,
            SleepModel.end_time.is_(None)
        ).order_by(SleepModel.start_time.desc()).first()
    
    def get_last_night_sleep(self, baby_id: int) -> Optional[SleepModel]:
        """Récupérer la dernière nuit de sommeil complète"""
        today = datetime.now().date()
        yesterday = today - timedelta(days=1)
        
        return self.db.query(SleepModel).filter(
            SleepModel.baby_id == baby_id,
            SleepModel.type == SleepType.NIGHT_SLEEP,
            SleepModel.start_time >= datetime.combine(yesterday, datetime.min.time()),
            SleepModel.start_time < datetime.combine(today, datetime.min.time())
        ).order_by(SleepModel.start_time.desc()).first()
    
    def get_sleep_statistics(
        self, 
        baby_id: int, 
        target_date: Optional[date] = None
    ) -> Dict[str, Any]:
        if not target_date:
            target_date = date.today()
        
        start_datetime = datetime.combine(target_date, datetime.min.time())
        end_datetime = start_datetime + timedelta(days=1)
        
        # Requête pour les stats du jour
        result = self.db.query(
            func.coalesce(func.sum(SleepModel.duration_minutes), 0).label('total_sleep'),
            func.count().filter(SleepModel.type == SleepType.NAP).label('nap_count'),
            func.coalesce(func.sum(case(
                (SleepModel.type == SleepType.NIGHT_SLEEP, SleepModel.duration_minutes),
                else_=0
            )), 0).label('night_sleep'),
            func.avg(case(
                (SleepModel.type == SleepType.NAP, SleepModel.duration_minutes),
                else_=None
            )).label('avg_nap_duration'),
            func.avg(case(
                (SleepModel.quality == SleepQuality.EXCELLENT, 5),
                (SleepModel.quality == SleepQuality.GOOD, 4),
                (SleepModel.quality == SleepQuality.FAIR, 3),
                (SleepModel.quality == SleepQuality.POOR, 2),
                (SleepModel.quality == SleepQuality.RESTLESS, 1),
                else_=3
            )).label('avg_quality_score'),
            func.max(SleepModel.end_time).label('last_sleep_end')
        ).filter(
            SleepModel.baby_id == baby_id,
            SleepModel.start_time >= start_datetime,
            SleepModel.start_time < end_datetime,
            SleepModel.end_time.isnot(None)  # seulement les sessions terminées
        ).first()
        
        # Calculer l'efficacité du sommeil
        total_wake_time = self.db.query(
            func.sum(SleepModel.wakeups_count)
        ).filter(
            SleepModel.baby_id == baby_id,
            SleepModel.start_time >= start_datetime,
            SleepModel.start_time < end_datetime
        ).scalar() or 0
        
        sleep_efficiency = 0
        if result.total_sleep > 0:
            # Efficacité = temps de sommeil / (temps de sommeil + réveils)
            sleep_efficiency = (result.total_sleep / (result.total_sleep + total_wake_time * 5)) * 100
        
        # Prédiction prochaine sieste
        next_nap_prediction = None
        last_nap = self.db.query(SleepModel).filter(
            SleepModel.baby_id == baby_id,
            SleepModel.type == SleepType.NAP,
            SleepModel.end_time.isnot(None)
        ).order_by(SleepModel.end_time.desc()).first()
        
        if last_nap and last_nap.end_time:
            # Généralement une sieste toutes les 2-3 heures pour les bébés
            avg_nap_interval = 150  # 2.5h en minutes
            next_nap_prediction = last_nap.end_time + timedelta(minutes=avg_nap_interval)
        
        return {
            'total_sleep_today_minutes': float(result.total_sleep or 0),
            'total_naps_today': result.nap_count or 0,
            'total_night_sleep_minutes': float(result.night_sleep or 0),
            'average_nap_duration': float(result.avg_nap_duration or 0),
            'sleep_efficiency': sleep_efficiency,
            'wakeups_per_hour': total_wake_time / (result.total_sleep / 60) if result.total_sleep > 0 else 0,
            'sleep_cycles': int((result.total_sleep or 0) / 45),  # cycles de 45min environ
            'bedtime_consistency': self._calculate_bedtime_consistency(baby_id, 7),
            'last_sleep_end': result.last_sleep_end,
            'next_nap_prediction': next_nap_prediction,
            'average_quality_score': float(result.avg_quality_score or 3.0)
        }
    
    def _calculate_bedtime_consistency(self, baby_id: int, days: int = 7) -> float:
        """Calculer la régularité de l'heure du coucher sur X jours"""
        end_date = date.today()
        start_date = end_date - timedelta(days=days)
        
        bedtimes = self.db.query(
            func.date(SleepModel.start_time),
            func.extract('hour', SleepModel.start_time) * 60 + func.extract('minute', SleepModel.start_time)
        ).filter(
            SleepModel.baby_id == baby_id,
            SleepModel.type == SleepType.NIGHT_SLEEP,
            SleepModel.start_time >= datetime.combine(start_date, datetime.min.time()),
            SleepModel.start_time < datetime.combine(end_date, datetime.min.time())
        ).all()
        
        if len(bedtimes) < 2:
            return 0.0
        
        # Calculer l'écart-type des heures de coucher
        times = [bt[1] for bt in bedtimes]
        mean = sum(times) / len(times)
        variance = sum((x - mean) ** 2 for x in times) / len(times)
        std_dev = variance ** 0.5
        
        # Normaliser sur une échelle 0-100 (plus c'est bas, mieux c'est)
        # 60 minutes d'écart-type = 0%, 0 minutes = 100%
        consistency = max(0, 100 - (std_dev / 60 * 100))
        
        return consistency
    
    def get_sleep_trends(
        self, 
        baby_id: int, 
        days: int = 7
    ) -> List[Dict[str, Any]]:
        end_date = date.today()
        start_date = end_date - timedelta(days=days)
        
        trends = []
        current_date = start_date
        
        while current_date <= end_date:
            day_start = datetime.combine(current_date, datetime.min.time())
            day_end = day_start + timedelta(days=1)
            
            result = self.db.query(
                func.coalesce(func.sum(SleepModel.duration_minutes), 0).label('total_sleep'),
                func.coalesce(func.sum(case(
                    (SleepModel.type == SleepType.NIGHT_SLEEP, SleepModel.duration_minutes),
                    else_=0
                )), 0).label('night_sleep'),
                func.count().filter(SleepModel.type == SleepType.NAP).label('nap_count'),
                func.avg(case(
                    (SleepModel.quality == SleepQuality.EXCELLENT, 5),
                    (SleepModel.quality == SleepQuality.GOOD, 4),
                    (SleepModel.quality == SleepQuality.FAIR, 3),
                    (SleepModel.quality == SleepQuality.POOR, 2),
                    (SleepModel.quality == SleepQuality.RESTLESS, 1),
                    else_=3
                )).label('avg_quality')
            ).filter(
                SleepModel.baby_id == baby_id,
                SleepModel.start_time >= day_start,
                SleepModel.start_time < day_end,
                SleepModel.end_time.isnot(None)
            ).first()
            
            trends.append({
                'date': current_date.strftime('%Y-%m-%d'),
                'total_sleep_minutes': float(result.total_sleep or 0),
                'night_sleep_minutes': float(result.night_sleep or 0),
                'nap_count': result.nap_count or 0,
                'average_quality': float(result.avg_quality or 3.0)
            })
            
            current_date += timedelta(days=1)
        
        return trends
    
    def get_chart_data(
        self, 
        baby_id: int, 
        days: int = 7
    ) -> Dict[str, Any]:
        trends = self.get_sleep_trends(baby_id, days)
        
        labels = [t['date'] for t in trends]
        total_sleep_data = [t['total_sleep_minutes'] / 60 for t in trends]  # en heures
        night_sleep_data = [t['night_sleep_minutes'] / 60 for t in trends]  # en heures
        nap_count_data = [t['nap_count'] for t in trends]
        quality_data = [t['average_quality'] for t in trends]
        
        return {
            'labels': labels,
            'total_sleep_data': total_sleep_data,
            'night_sleep_data': night_sleep_data,
            'nap_count_data': nap_count_data,
            'quality_data': quality_data
        }
    
    def get_sleep_patterns(
        self, 
        baby_id: int, 
        days: int = 30
    ) -> Dict[str, Any]:
        """Analyser les patterns de sommeil récurrents"""
        end_date = date.today()
        start_date = end_date - timedelta(days=days)
        
        # Analyser les heures de coucher
        bedtimes = self.db.query(
            func.extract('hour', SleepModel.start_time).label('hour'),
            func.extract('minute', SleepModel.start_time).label('minute')
        ).filter(
            SleepModel.baby_id == baby_id,
            SleepModel.type == SleepType.NIGHT_SLEEP,
            SleepModel.start_time >= datetime.combine(start_date, datetime.min.time()),
            SleepModel.start_time < datetime.combine(end_date, datetime.min.time())
        ).all()
        
        # Analyser les heures de réveil
        wake_times = self.db.query(
            func.extract('hour', SleepModel.end_time).label('hour'),
            func.extract('minute', SleepModel.end_time).label('minute')
        ).filter(
            SleepModel.baby_id == baby_id,
            SleepModel.type == SleepType.NIGHT_SLEEP,
            SleepModel.end_time.isnot(None),
            SleepModel.end_time >= datetime.combine(start_date, datetime.min.time()),
            SleepModel.end_time < datetime.combine(end_date, datetime.min.time())
        ).all()
        
        # Calculer les moyennes
        avg_bedtime = self._calculate_average_time(bedtimes)
        avg_wake_time = self._calculate_average_time(wake_times)
        
        # Analyser les durées de sieste
        nap_durations = self.db.query(SleepModel.duration_minutes).filter(
            SleepModel.baby_id == baby_id,
            SleepModel.type == SleepType.NAP,
            SleepModel.start_time >= datetime.combine(start_date, datetime.min.time()),
            SleepModel.start_time < datetime.combine(end_date, datetime.min.time()),
            SleepModel.duration_minutes.isnot(None)
        ).all()
        
        nap_durs = [nd[0] for nd in nap_durations]
        avg_nap_duration = sum(nap_durs) / len(nap_durs) if nap_durs else 0
        
        return {
            'average_bedtime': avg_bedtime,
            'average_wake_time': avg_wake_time,
            'average_nap_duration_minutes': avg_nap_duration,
            'total_nights_analyzed': len(bedtimes),
            'bedtime_std_dev': self._calculate_time_std_dev(bedtimes),
            'most_common_sleep_position': self._get_most_common_position(baby_id, days)
        }
    
    def _calculate_average_time(self, times: List[Tuple[float, float]]) -> Optional[str]:
        if not times:
            return None
        
        total_minutes = sum(h * 60 + m for h, m in times)
        avg_minutes = total_minutes / len(times)
        
        avg_hour = int(avg_minutes // 60)
        avg_minute = int(avg_minutes % 60)
        
        return f"{avg_hour:02d}:{avg_minute:02d}"
    
    def _calculate_time_std_dev(self, times: List[Tuple[float, float]]) -> float:
        if len(times) < 2:
            return 0.0
        
        minutes = [h * 60 + m for h, m in times]
        mean = sum(minutes) / len(minutes)
        variance = sum((x - mean) ** 2 for x in minutes) / len(minutes)
        return variance ** 0.5
    
    def _get_most_common_position(self, baby_id: int, days: int) -> Optional[str]:
        result = self.db.query(
            SleepModel.sleep_position,
            func.count(SleepModel.sleep_position).label('count')
        ).filter(
            SleepModel.baby_id == baby_id,
            SleepModel.start_time >= datetime.now() - timedelta(days=days),
            SleepModel.sleep_position.isnot(None)
        ).group_by(SleepModel.sleep_position).order_by(func.count(SleepModel.sleep_position).desc()).first()
        
        return result[0] if result else None
    
    def get_sleep_recommendations(
        self, 
        baby_id: int, 
        baby_age_days: int
    ) -> List[Dict[str, Any]]:
        """Générer des recommandations basées sur l'âge et les patterns"""
        recommendations = []
        
        # Récupérer les stats récentes
        stats = self.get_sleep_statistics(baby_id)
        patterns = self.get_sleep_patterns(baby_id, 7)
        
        # Recommandations basées sur l'âge
        if baby_age_days < 90:  # 0-3 mois
            if stats['total_sleep_today_minutes'] < 900:  # <15h
                recommendations.append({
                    'category': 'duration',
                    'title': 'Temps de sommeil insuffisant',
                    'description': 'Les nouveau-nés ont besoin de 14-17h de sommeil par jour.',
                    'priority': 4,
                    'action_items': [
                        'Surveillez les signes de fatigue: bâillements, frottement des yeux',
                        'Créez un environnement calme et sombre pour les siestes',
                        'Établissez une routine de coucher précoce'
                    ]
                })
        
        elif baby_age_days < 180:  # 3-6 mois
            if stats['wakeups_per_hour'] > 2:
                recommendations.append({
                    'category': 'quality',
                    'title': 'Réveils fréquents',
                    'description': 'Votre bébé se réveille trop souvent pendant la nuit.',
                    'priority': 3,
                    'action_items': [
                        'Assurez-vous que la pièce est bien obscure',
                        'Utilisez une machine à bruit blanc',
                        'Évitez de nourrir au premier réveil, attendez quelques minutes'
                    ]
                })
        
        # Recommandations basées sur la régularité
        if patterns.get('bedtime_std_dev', 0) > 60:  # écart-type > 1h
            recommendations.append({
                'category': 'routine',
                'title': 'Heure de coucher irrégulière',
                'description': 'Une heure de coucher régulière aide à réguler le rythme circadien.',
                'priority': 3,
                'action_items': [
                    'Fixez une heure de coucher constante à ±30 minutes près',
                    'Commencez la routine 30 minutes avant le coucher',
                    'Incluez des activités calmes: bain, lecture, berceuse'
                ]
            })
        
        # Recommandations de sécurité
        if not patterns.get('most_common_sleep_position') == 'back':
            recommendations.append({
                'category': 'safety',
                'title': 'Position de sommeil',
                'description': 'La position sur le dos est la plus sûre pour prévenir la MSN.',
                'priority': 5,
                'action_items': [
                    'Placez toujours votre bébé sur le dos pour dormir',
                    'Utilisez un matelas ferme et bien ajusté',
                    'Évitez les couvertures, oreillers et peluches dans le lit'
                ]
            })
        
        return recommendations
