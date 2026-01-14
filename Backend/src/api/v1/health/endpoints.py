from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.session import get_db

router = APIRouter()

@router.get("/biometrics")
async def get_biometrics(
    baby_id: int = None,
    db: Session = Depends(get_db)
):
    return {"biometrics": [], "message": "Get biometrics endpoint - à implémenter"}

@router.get("/vaccinations")
async def get_vaccinations(
    baby_id: int = None,
    db: Session = Depends(get_db)
):
    return {"vaccinations": [], "message": "Get vaccinations endpoint - à implémenter"}

@router.get("/medical-journal")
async def get_medical_journal(
    baby_id: int = None,
    db: Session = Depends(get_db)
):
    return {"medical_records": [], "message": "Get medical journal endpoint - à implémenter"}
