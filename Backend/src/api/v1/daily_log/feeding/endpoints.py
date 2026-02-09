# 📁 backend/src/api/v1/daily_log/feeding/endpoints.py
from typing import List, Optional
from datetime import datetime, date
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from ....dependencies import get_db, get_current_user
from .....core.services.feeding_service import FeedingService
from .....core.models.feeding import (
    FeedingCreate, FeedingUpdate, FeedingResponse,
    FeedingStatistics, FeedingTrend, FeedingChartData
)
from .....core.models.user import User

router = APIRouter(prefix="/feedings", tags=["feedings"])

@router.post("/", response_model=FeedingResponse, status_code=status.HTTP_201_CREATED)
def create_feeding(
    feeding: FeedingCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Créer un nouveau repas"""
    service = FeedingService(db)
    return service.create_feeding(feeding, current_user.id)

@router.get("/{feeding_id}", response_model=FeedingResponse)
def get_feeding(
    feeding_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer un repas par ID"""
    service = FeedingService(db)
    return service.get_feeding(feeding_id, current_user.id)

@router.get("/", response_model=List[FeedingResponse])
def get_baby_feedings(
    baby_id: int = Query(..., description="ID du bébé"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    start_date: Optional[datetime] = Query(None),
    end_date: Optional[datetime] = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer tous les repas d'un bébé"""
    service = FeedingService(db)
    return service.get_baby_feedings(
        baby_id=baby_id,
        user_id=current_user.id,
        skip=skip,
        limit=limit,
        start_date=start_date,
        end_date=end_date
    )

@router.put("/{feeding_id}", response_model=FeedingResponse)
def update_feeding(
    feeding_id: int,
    feeding_update: FeedingUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Mettre à jour un repas"""
    service = FeedingService(db)
    return service.update_feeding(feeding_id, feeding_update, current_user.id)

@router.delete("/{feeding_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_feeding(
    feeding_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Supprimer un repas"""
    service = FeedingService(db)
    service.delete_feeding(feeding_id, current_user.id)
    return None

@router.get("/baby/{baby_id}/today", response_model=List[FeedingResponse])
def get_today_feedings(
    baby_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer les repas d'aujourd'hui pour un bébé"""
    service = FeedingService(db)
    return service.get_today_feedings(baby_id, current_user.id)

@router.get("/baby/{baby_id}/last", response_model=Optional[FeedingResponse])
def get_last_feeding(
    baby_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer le dernier repas d'un bébé"""
    service = FeedingService(db)
    return service.get_last_feeding(baby_id, current_user.id)

@router.get("/baby/{baby_id}/statistics", response_model=FeedingStatistics)
def get_feeding_statistics(
    baby_id: int,
    target_date: Optional[date] = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer les statistiques des repas"""
    service = FeedingService(db)
    return service.get_feeding_statistics(baby_id, current_user.id, target_date)

@router.get("/baby/{baby_id}/trends", response_model=List[FeedingTrend])
def get_feeding_trends(
    baby_id: int,
    days: int = Query(7, ge=1, le=30),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer les tendances des repas sur X jours"""
    service = FeedingService(db)
    return service.get_feeding_trends(baby_id, current_user.id, days)

@router.get("/baby/{baby_id}/chart-data", response_model=FeedingChartData)
def get_chart_data(
    baby_id: int,
    days: int = Query(7, ge=1, le=30),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer les données pour les graphiques"""
    service = FeedingService(db)
    return service.get_chart_data(baby_id, current_user.id, days)

@router.get("/baby/{baby_id}/daily-goal")
def get_daily_goal(
    baby_id: int,
    baby_age_days: int = Query(..., ge=0),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer les objectifs quotidiens selon l'âge"""
    service = FeedingService(db)
    goals = service.calculate_daily_goal(baby_id, baby_age_days)
    return goals

@router.get("/baby/{baby_id}/schedule")
def get_feeding_schedule(
    baby_id: int,
    schedule_date: date = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer le planning des repas pour une journée"""
    if not schedule_date:
        schedule_date = date.today()
    
    service = FeedingService(db)
    return service.get_feeding_schedule(baby_id, current_user.id, schedule_date)

@router.post("/baby/{baby_id}/quick-add")
def quick_add_feeding(
    baby_id: int,
    feeding_type: str = Query(..., description="Type: breast_milk, formula, solid_food"),
    quantity: Optional[float] = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Ajout rapide d'un repas"""
    service = FeedingService(db)
    
    # Créer un repas basique
    feeding_data = FeedingCreate(
        baby_id=baby_id,
        type=feeding_type,
        start_time=datetime.now(),
        quantity_ml=quantity if feeding_type in ["breast_milk", "formula", "water"] else None,
        quantity_grams=quantity if feeding_type == "solid_food" else None
    )
    
    return service.create_feeding(feeding_data, current_user.id)
