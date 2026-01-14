from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db.session import get_db

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    # Implémentation temporaire
    return {
        "access_token": "test_token",
        "token_type": "bearer",
        "message": "Login endpoint - à implémenter"
    }

@router.post("/register")
async def register(
    user_data: dict,
    db: Session = Depends(get_db)
):
    # Implémentation temporaire
    return {
        "message": "Register endpoint - à implémenter",
        "user_data": user_data
    }
