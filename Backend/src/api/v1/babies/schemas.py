"""
Pydantic Schemas for Baby Profile API
Validation et sérialisation des données
"""

from pydantic import BaseModel, Field, validator, root_validator
from datetime import date, datetime
from typing import Optional, List
from enum import Enum
import re


class GenderEnum(str, Enum):
    """Enum pour le genre"""
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


# ==================== SCHEMAS DE CREATION ====================

class BabyCreateSchema(BaseModel):
    """
    Schema pour créer un nouveau profil bébé
    Utilisé pour POST /api/v1/babies/
    """
    
    name: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Prénom du bébé",
        example="Emma"
    )
    
    birth_date: date = Field(
        ...,
        description="Date de naissance (format: YYYY-MM-DD)",
        example="2025-12-01"
    )
    
    gender: GenderEnum = Field(
        ...,
        description="Genre du bébé (male, female, other)",
        example="female"
    )
    
    photo_url: Optional[str] = Field(
        None,
        max_length=500,
        description="URL de la photo de profil",
        example="https://example.com/photos/baby.jpg"
    )
    
    # Validators
    
    @validator('name')
    def validate_name(cls, v: str) -> str:
        """Valide le prénom du bébé"""
        # Supprimer espaces inutiles
        v = v.strip()
        
        # Vérifier qu'il n'est pas vide après trim
        if not v:
            raise ValueError("Name cannot be empty or only whitespace")
        
        # Autoriser seulement lettres, espaces, tirets et apostrophes
        if not re.match(r"^[a-zA-ZÀ-ÿ\s\-']+$", v):
            raise ValueError(
                "Name can only contain letters, spaces, hyphens and apostrophes"
            )
        
        # Vérifier longueur min après nettoyage
        if len(v) < 2:
            raise ValueError("Name must be at least 2 characters long")
        
        return v
    
    @validator('birth_date')
    def validate_birth_date(cls, v: date) -> date:
        """Valide la date de naissance"""
        today = date.today()
        
        # Ne peut pas être dans le futur
        if v > today:
            raise ValueError("Birth date cannot be in the future")
        
        # Limite raisonnable : maximum 10 ans (pour app puériculture)
        max_age_date = today.replace(year=today.year - 10)
        if v < max_age_date:
            raise ValueError(
                "Birth date is too old. This app is designed for babies up to 10 years old"
            )
        
        return v
    
    @validator('photo_url')
    def validate_photo_url(cls, v: Optional[str]) -> Optional[str]:
        """Valide l'URL de la photo"""
        if v is None:
            return v
        
        v = v.strip()
        
        # Vérifier format URL basique
        if not re.match(r'^https?://', v):
            raise ValueError("Photo URL must start with http:// or https://")
        
        # Vérifier extension image
        valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
        if not any(v.lower().endswith(ext) for ext in valid_extensions):
            raise ValueError(
                f"Photo URL must end with one of: {', '.join(valid_extensions)}"
            )
        
        return v
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Emma",
                "birth_date": "2025-12-01",
                "gender": "female",
                "photo_url": "https://example.com/photos/emma.jpg"
            }
        }


# ==================== SCHEMAS DE MISE A JOUR ====================

class BabyUpdateSchema(BaseModel):
    """
    Schema pour mettre à jour un profil bébé
    Tous les champs sont optionnels (PATCH)
    """
    
    name: Optional[str] = Field(
        None,
        min_length=1,
        max_length=100,
        description="Nouveau prénom du bébé"
    )
    
    birth_date: Optional[date] = Field(
        None,
        description="Nouvelle date de naissance"
    )
    
    gender: Optional[GenderEnum] = Field(
        None,
        description="Nouveau genre"
    )
    
    photo_url: Optional[str] = Field(
        None,
        max_length=500,
        description="Nouvelle URL de photo"
    )
    
    # Réutiliser les mêmes validators
    _validate_name = validator('name', allow_reuse=True)(
        BabyCreateSchema.validate_name
    )
    _validate_birth_date = validator('birth_date', allow_reuse=True)(
        BabyCreateSchema.validate_birth_date
    )
    _validate_photo_url = validator('photo_url', allow_reuse=True)(
        BabyCreateSchema.validate_photo_url
    )
    
    @root_validator
    def at_least_one_field(cls, values):
        """Vérifie qu'au moins un champ est fourni"""
        if not any(values.values()):
            raise ValueError("At least one field must be provided for update")
        return values
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Emma Rose"
            }
        }


# ==================== SCHEMAS DE REPONSE ====================

class AgeInfoSchema(BaseModel):
    """Informations sur l'âge du bébé"""
    days: int = Field(..., description="Âge en jours", example=92)
    weeks: int = Field(..., description="Âge en semaines", example=13)
    months: int = Field(..., description="Âge en mois", example=3)
    years: int = Field(..., description="Âge en années", example=0)


class BabyResponseSchema(BaseModel):
    """
    Schema de réponse pour un profil bébé
    Retourné par GET, POST, PUT
    """
    
    id: int = Field(..., description="ID unique du bébé")
    user_id: int = Field(..., description="ID du parent propriétaire")
    name: str = Field(..., description="Prénom du bébé")
    birth_date: date = Field(..., description="Date de naissance")
    gender: GenderEnum = Field(..., description="Genre")
    photo_url: Optional[str] = Field(None, description="URL de la photo")
    age: AgeInfoSchema = Field(..., description="Informations d'âge calculées")
    created_at: datetime = Field(..., description="Date de création du profil")
    updated_at: datetime = Field(..., description="Date de dernière modification")
    
    class Config:
        from_attributes = True  # Pydantic v2 (orm_mode dans v1)
        json_schema_extra = {
            "example": {
                "id": 1,
                "user_id": 42,
                "name": "Emma",
                "birth_date": "2025-12-01",
                "gender": "female",
                "photo_url": "https://example.com/photos/emma.jpg",
                "age": {
                    "days": 92,
                    "weeks": 13,
                    "months": 3,
                    "years": 0
                },
                "created_at": "2026-01-15T10:30:00Z",
                "updated_at": "2026-02-01T14:20:00Z"
            }
        }


class BabyListResponseSchema(BaseModel):
    """
    Schema pour liste de bébés (avec pagination)
    """
    total: int = Field(..., description="Nombre total de bébés")
    skip: int = Field(..., description="Nombre d'éléments sautés")
    limit: int = Field(..., description="Limite par page")
    items: List[BabyResponseSchema] = Field(..., description="Liste des bébés")
    
    class Config:
        json_schema_extra = {
            "example": {
                "total": 2,
                "skip": 0,
                "limit": 10,
                "items": [
                    {
                        "id": 1,
                        "user_id": 42,
                        "name": "Emma",
                        "birth_date": "2025-12-01",
                        "gender": "female",
                        "photo_url": None,
                        "age": {"days": 92, "weeks": 13, "months": 3, "years": 0},
                        "created_at": "2026-01-15T10:30:00Z",
                        "updated_at": "2026-01-15T10:30:00Z"
                    }
                ]
            }
        }


# ==================== SCHEMAS D'UPLOAD ====================

class PhotoUploadResponseSchema(BaseModel):
    """Schema de réponse après upload de photo"""
    photo_url: str = Field(..., description="URL de la photo uploadée")
    message: str = Field(..., description="Message de confirmation")
    
    class Config:
        json_schema_extra = {
            "example": {
                "photo_url": "/uploads/babies/a1b2c3d4-emma.jpg",
                "message": "Photo uploaded successfully"
            }
        }


# ==================== SCHEMAS D'ERREUR ====================

class ErrorResponseSchema(BaseModel):
    """Schema standard pour les erreurs"""
    detail: str = Field(..., description="Message d'erreur")
    error_code: Optional[str] = Field(None, description="Code d'erreur spécifique")
    
    class Config:
        json_schema_extra = {
            "example": {
                "detail": "Baby profile not found",
                "error_code": "BABY_NOT_FOUND"
            }
        }

