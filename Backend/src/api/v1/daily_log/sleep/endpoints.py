# 📁 backend/src/api/v1/daily_log/sleep/endpoints.py
from typing import List, Optional
from datetime import datetime, date, timedelta
from fastapi import APIRouter, Depends, HTTPException, status, Query, BackgroundTasks
from sqlalchemy.orm import Session

from ....dependencies import get_db, get_current_user
from .....core.services.sleep_service import SleepService
from .....core.models.sleep import (
    SleepCreate, SleepUpdate, SleepResponse,
    SleepStatistics, SleepTrend, SleepChartData,
    SleepRhythm, SleepRecommendation
)
from .....core.models.user import User

router = APIRouter(prefix="/sleep", tags=["sleep"])

@router.post("/", response_model=SleepResponse, status_code=status.HTTP_201_CREATED)
def create_sleep_session(
    sleep: SleepCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Créer une nouvelle session de sommeil"""
    service = SleepService(db)
    return service.create_sleep_session(sleep, current_user.id)

@router.get("/{sleep_id}", response_model=SleepResponse)
def get_sleep_session(
    sleep_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer une session de sommeil par ID"""
    service = SleepService(db)
    return service.get_sleep_session(sleep_id, current_user.id)

@router.get("/", response_model=List[SleepResponse])
def get_baby_sleep_sessions(
    baby_id: int = Query(..., description="ID du bébé"),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    start_date: Optional[datetime] = Query(None),
    end_date: Optional[datetime] = Query(None),
    sleep_type: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer toutes les sessions de sommeil d'un bébé"""
    service = SleepService(db)
    return service.get_baby_sleep_sessions(
        baby_id=baby_id,
        user_id=current_user.id,
        skip=skip,
        limit=limit,
        start_date=start_date,
        end_date=end_date,
        sleep_type=sleep_type
    )

@router.put("/{sleep_id}", response_model=SleepResponse)
def update_sleep_session(
    sleep_id: int,
    sleep_update: SleepUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Mettre à jour une session de sommeil"""
    service = SleepService(db)
    return service.update_sleep_session(sleep_id, sleep_update, current_user.id)

@router.delete("/{sleep_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sleep_session(
    sleep_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Supprimer une session de sommeil"""
    service = SleepService(db)
    service.delete_sleep_session(sleep_id, current_user.id)
    return None

@router.post("/start", response_model=SleepResponse)
def start_sleep_session(
    baby_id: int = Query(..., description="ID du bébé"),
    sleep_type: str = Query(..., description="Type: nap, night_sleep"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Commencer une nouvelle session de sommeil"""
    service = SleepService(db)
    return service.start_sleep_session(baby_id, current_user.id, sleep_type)

@router.post("/{sleep_id}/end", response_model=SleepResponse)
def end_sleep_session(
    sleep_id: int,
    quality: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Terminer une session de sommeil en cours"""
    service = SleepService(db)
    return service.end_sleep_session(sleep_id, current_user.id, quality)

@router.get("/baby/{baby_id}/current", response_model=Optional[SleepResponse])
def get_current_sleep_session(
    baby_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer la session de sommeil en cours"""
    service = SleepService(db)
    return service.get_current_sleep_session(baby_id, current_user.id)

@router.get("/baby/{baby_id}/today", response_model=List[SleepResponse])
def get_today_sleep_sessions(
    baby_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer les sessions de sommeil d'aujourd'hui"""
    service = SleepService(db)
    return service.get_today_sleep_sessions(baby_id, current_user.id)

@router.get("/baby/{baby_id}/statistics", response_model=SleepStatistics)
def get_sleep_statistics(
    baby_id: int,
    target_date: Optional[date] = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer les statistiques de sommeil"""
    service = SleepService(db)
    return service.get_sleep_statistics(baby_id, current_user.id, target_date)

@router.get("/baby/{baby_id}/trends", response_model=List[SleepTrend])
def get_sleep_trends(
    baby_id: int,
    days: int = Query(7, ge=1, le=30),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer les tendances de sommeil sur X jours"""
    service = SleepService(db)
    return service.get_sleep_trends(baby_id, current_user.id, days)

@router.get("/baby/{baby_id}/chart-data", response_model=SleepChartData)
def get_chart_data(
    baby_id: int,
    days: int = Query(7, ge=1, le=30),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Récupérer les données pour les graphiques"""
    service = SleepService(db)
    return service.get_chart_data(baby_id, current_user.id, days)

@router.get("/baby/{baby_id}/patterns")
def get_sleep_patterns(
    baby_id: int,
    days: int = Query(30, ge=7, le=90),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Analyser les patterns de sommeil"""
    service = SleepService(db)
    return service.get_sleep_patterns(baby_id, current_user.id, days)

@router.get("/rhythm/{baby_age_days}", response_model=SleepRhythm)
def get_sleep_rhythm_by_age(
    baby_age_days: int = Query(..., ge=0, le=730, description="Âge du bébé en jours"),
    db: Session = Depends(get_db)
):
    """Obtenir le rythme de sommeil recommandé par âge"""
    service = SleepService(db)
    return service.get_sleep_rhythm_by_age(baby_age_days)

@router.get("/baby/{baby_id}/recommendations", response_model=List[SleepRecommendation])
def get_sleep_recommendations(
    baby_id: int,
    baby_age_days: int = Query(..., ge=0, le=730),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Générer des recommandations personnalisées"""
    service = SleepService(db)
    return service.get_sleep_recommendations(baby_id, current_user.id, baby_age_days)

@router.get("/baby/{baby_id}/score")
def calculate_sleep_score(
    baby_id: int,
    days: int = Query(7, ge=1, le=30),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Calculer un score de sommeil global"""
    service = SleepService(db)
    return service.calculate_sleep_score(baby_id, current_user.id, days)

@router.get("/baby/{baby_id}/report")
def generate_sleep_report(
    baby_id: int,
    start_date: date = Query(..., description="Date de début (YYYY-MM-DD)"),
    end_date: date = Query(..., description="Date de fin (YYYY-MM-DD)"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Générer un rapport de sommeil complet"""
    # Validation
    if end_date < start_date:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="End date must be after start date"
        )
    
    if (end_date - start_date).days > 90:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Report period cannot exceed 90 days"
        )
    
    service = SleepService(db)
    return service.generate_sleep_report(baby_id, current_user.id, start_date, end_date)

@router.get("/baby/{baby_id}/predict-next-nap")
def predict_next_nap(
    baby_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Prédire la prochaine sieste"""
    service = SleepService(db)
    stats = service.get_sleep_statistics(baby_id, current_user.id)
    
    if not stats.next_nap_prediction:
        # Si pas de prédiction, suggérer basé sur l'heure
        now = datetime.now()
        if now.hour < 12:
            next_nap = now.replace(hour=10, minute=0, second=0, microsecond=0)
        elif now.hour < 15:
            next_nap = now.replace(hour=13, minute=0, second=0, microsecond=0)
        else:
            next_nap = now.replace(hour=16, minute=0, second=0, microsecond=0)
        
        return {"predicted_time": next_nap, "confidence": "low"}
    
    return {"predicted_time": stats.next_nap_prediction, "confidence": "medium"}

@router.post("/baby/{baby_id}/reminders/enable")
def enable_sleep_reminders(
    baby_id: int,
    reminder_type: str = Query(..., description="bedtime, nap, wake_window"),
    time_offset: int = Query(15, description="Minutes avant pour le rappel"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Activer les rappels de sommeil"""
    # Ici, vous intégreriez avec un service de notifications
    return {
        "message": f"Sleep reminders enabled for {reminder_type}",
        "time_offset": time_offset,
        "status": "active"
    }
