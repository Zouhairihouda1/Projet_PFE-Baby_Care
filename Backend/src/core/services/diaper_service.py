"""
Diaper Changes API Endpoints
Routes REST pour la gestion des changements de couches
"""

from fastapi import APIRouter, Depends, HTTPException, status, Query, Body
from sqlalchemy.orm import Session
from typing import List
from datetime import date
import logging

from app.api.deps import get_db, get_current_user
from app.db.models.user_model import User
from app.core.services.diaper_service import DiaperService
from app.api.v1.daily_log.hygiene.schemas import (
    DiaperCreateSchema, DiaperUpdateSchema, DiaperResponseSchema,
    DiaperListResponseSchema, DiaperStatsSchema, DailyDiaperSummarySchema
)

router = APIRouter()
logger = logging.getLogger(__name__)

def get_diaper_service(db: Session = Depends(get_db)) -> DiaperService:
    return DiaperService(db)

@router.post("/", response_model=DiaperResponseSchema, status_code=201,
             summary="Record a diaper change", tags=["Hygiene"])
def record_diaper_change(
    diaper_data: DiaperCreateSchema = Body(...),
    current_user: User = Depends(get_current_user),
    diaper_service: DiaperService = Depends(get_diaper_service)
) -> DiaperResponseSchema:
    """Record a new diaper change for a baby."""
    logger.info(f"User {current_user.id} recording diaper change")
    return diaper_service.create_diaper_change(current_user.id, diaper_data)

@router.get("/baby/{baby_id}", response_model=DiaperListResponseSchema,
            summary="Get all diaper changes for a baby", tags=["Hygiene"])
def get_baby_diaper_changes(
    baby_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    current_user: User = Depends(get_current_user),
    diaper_service: DiaperService = Depends(get_diaper_service)
) -> DiaperListResponseSchema:
    """Get paginated list of diaper changes for a baby."""
    total, items = diaper_service.get_baby_diaper_changes(
        baby_id, current_user.id, skip, limit
    )
    return DiaperListResponseSchema(total=total, skip=skip, limit=limit, items=items)

@router.get("/{diaper_id}", response_model=DiaperResponseSchema,
            summary="Get a specific diaper change", tags=["Hygiene"])
def get_diaper_change(
    diaper_id: int,
    current_user: User = Depends(get_current_user),
    diaper_service: DiaperService = Depends(get_diaper_service)
) -> DiaperResponseSchema:
    """Get details of a specific diaper change."""
    return diaper_service.get_diaper_by_id(diaper_id, current_user.id)

@router.put("/{diaper_id}", response_model=DiaperResponseSchema,
            summary="Update a diaper change", tags=["Hygiene"])
def update_diaper_change(
    diaper_id: int,
    update_data: DiaperUpdateSchema = Body(...),
    current_user: User = Depends(get_current_user),
    diaper_service: DiaperService = Depends(get_diaper_service)
) -> DiaperResponseSchema:
    """Update a diaper change record."""
    return diaper_service.update_diaper_change(diaper_id, current_user.id, update_data)

@router.delete("/{diaper_id}", status_code=204,
               summary="Delete a diaper change", tags=["Hygiene"])
def delete_diaper_change(
    diaper_id: int,
    permanent: bool = Query(False),
    current_user: User = Depends(get_current_user),
    diaper_service: DiaperService = Depends(get_diaper_service)
):
    """Delete a diaper change (soft or hard delete)."""
    diaper_service.delete_diaper_change(diaper_id, current_user.id, permanent)
    return None

@router.get("/baby/{baby_id}/statistics", response_model=DiaperStatsSchema,
            summary="Get diaper change statistics", tags=["Hygiene", "Statistics"])
def get_diaper_statistics(
    baby_id: int,
    days: int = Query(30, ge=1, le=365),
    current_user: User = Depends(get_current_user),
    diaper_service: DiaperService = Depends(get_diaper_service)
) -> DiaperStatsSchema:
    """Get statistics about diaper changes for a baby."""
    return diaper_service.get_statistics(baby_id, current_user.id, days)
