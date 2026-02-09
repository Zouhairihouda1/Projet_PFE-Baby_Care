# 📁 backend/src/db/repositories/feeding_repository.py
from typing import List, Optional, Dict, Any
from datetime import datetime, timedelta, date
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, func, extract
from ...db.models.feeding_model import FeedingModel, FeedingType
from .base_repository import BaseRepository

class FeedingRepository(BaseRepository[FeedingModel]):
    def __init__(self, db: Session):
        super().__init__(db, FeedingModel)
    
    def get_by_baby(
        self, 
        baby_id: int, 
        skip: int = 0, 
        limit: int = 100,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None
    ) -> List[FeedingModel]:
        query = self.db.query(FeedingModel).filter(
            FeedingModel.baby_id == baby_id
        )
        
        if start_date:
            query = query.filter(FeedingModel.start_time >= start_date)
        if end_date:
            query = query.filter(FeedingModel.start_time <= end_date)
        
        return query.order_by(FeedingModel.start_time.desc()).offset(skip).limit(limit).all()
    
    def get_today_feedings(self, baby_id: int) -> List[FeedingModel]:
        today = datetime.now().date()
        tomorrow = today + timedelta(days=1)
        
        return self.db.query(FeedingModel).filter(
            FeedingModel.baby_id == baby_id,
            FeedingModel.start_time >= datetime.combine(today, datetime.min.time()),
            FeedingModel.start_time < datetime.combine(tomorrow, datetime.min.time())
        ).order_by(FeedingModel.start_time.desc()).all()
    
    def get_last_feeding(self, baby_id: int) -> Optional[FeedingModel]:
        return self.db.query(FeedingModel).filter(
            FeedingModel.baby_id == baby_id
        ).order_by(FeedingModel.start_time.desc()).first()
    
    def get_feeding_statistics(
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
            func.count(FeedingModel.id).label('total'),
            func.coalesce(func.sum(FeedingModel.quantity_ml), 0).label('total_ml'),
            func.coalesce(func.sum(FeedingModel.quantity_grams), 0).label('total_grams'),
            func.count().filter(FeedingModel.type == FeedingType.BREAST_MILK).label('breast_milk_count'),
            func.count().filter(FeedingModel.type == FeedingType.FORMULA).label('formula_count'),
            func.count().filter(FeedingModel.type == FeedingType.SOLID_FOOD).label('solid_food_count'),
            func.max(FeedingModel.start_time).label('last_feeding_time')
        ).filter(
            FeedingModel.baby_id == baby_id,
            FeedingModel.start_time >= start_datetime,
            FeedingModel.start_time < end_datetime
        ).first()
        
        # Calcul intervalle moyen
        feedings_today = self.db.query(FeedingModel).filter(
            FeedingModel.baby_id == baby_id,
            FeedingModel.start_time >= start_datetime,
            FeedingModel.start_time < end_datetime
        ).order_by(FeedingModel.start_time).all()
        
        intervals = []
        for i in range(1, len(feedings_today)):
            interval = (feedings_today[i].start_time - feedings_today[i-1].start_time).total_seconds() / 60
            intervals.append(interval)
        
        avg_interval = sum(intervals) / len(intervals) if intervals else 0
        
        # Estimation prochain repas
        next_feeding_estimate = None
        if result.last_feeding_time:
            next_feeding_estimate = result.last_feeding_time + timedelta(minutes=avg_interval)
        
        return {
            'total_today': result.total or 0,
            'total_ml_today': float(result.total_ml or 0),
            'total_grams_today': float(result.total_grams or 0),
            'average_interval_minutes': avg_interval,
            'breast_milk_count': result.breast_milk_count or 0,
            'formula_count': result.formula_count or 0,
            'solid_food_count': result.solid_food_count or 0,
            'last_feeding_time': result.last_feeding_time,
            'next_feeding_estimate': next_feeding_estimate
        }
    
    def get_feeding_trends(
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
                func.count(FeedingModel.id).label('total'),
                func.coalesce(func.sum(FeedingModel.quantity_ml), 0).label('total_ml'),
                func.coalesce(func.sum(FeedingModel.quantity_grams), 0).label('total_grams')
            ).filter(
                FeedingModel.baby_id == baby_id,
                FeedingModel.start_time >= day_start,
                FeedingModel.start_time < day_end
            ).first()
            
            trends.append({
                'date': current_date.strftime('%Y-%m-%d'),
                'total_feedings': result.total or 0,
                'total_ml': float(result.total_ml or 0),
                'total_grams': float(result.total_grams or 0)
            })
            
            current_date += timedelta(days=1)
        
        return trends
    
    def get_chart_data(
        self, 
        baby_id: int, 
        days: int = 7
    ) -> Dict[str, Any]:
        trends = self.get_feeding_trends(baby_id, days)
        
        labels = [t['date'] for t in trends]
        breast_milk_data = []
        formula_data = []
        solid_food_data = []
        
        for trend_date in trends:
            date_obj = datetime.strptime(trend_date['date'], '%Y-%m-%d').date()
            day_start = datetime.combine(date_obj, datetime.min.time())
            day_end = day_start + timedelta(days=1)
            
            # Compter par type pour ce jour
            breast_count = self.db.query(func.count(FeedingModel.id)).filter(
                FeedingModel.baby_id == baby_id,
                FeedingModel.type == FeedingType.BREAST_MILK,
                FeedingModel.start_time >= day_start,
                FeedingModel.start_time < day_end
            ).scalar() or 0
            
            formula_count = self.db.query(func.count(FeedingModel.id)).filter(
                FeedingModel.baby_id == baby_id,
                FeedingModel.type == FeedingType.FORMULA,
                FeedingModel.start_time >= day_start,
                FeedingModel.start_time < day_end
            ).scalar() or 0
            
            solid_count = self.db.query(func.count(FeedingModel.id)).filter(
                FeedingModel.baby_id == baby_id,
                FeedingModel.type == FeedingType.SOLID_FOOD,
                FeedingModel.start_time >= day_start,
                FeedingModel.start_time < day_end
            ).scalar() or 0
            
            breast_milk_data.append(breast_count)
            formula_data.append(formula_count)
            solid_food_data.append(solid_count)
        
        return {
            'labels': labels,
            'breast_milk_data': breast_milk_data,
            'formula_data': formula_data,
            'solid_food_data': solid_food_data
        }
