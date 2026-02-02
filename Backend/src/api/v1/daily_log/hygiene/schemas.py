"""
Pydantic Schemas for Diaper Changes API
Validation et sérialisation des données d'hygiène
"""

from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional
from enum import Enum


class DiaperTypeEnum(str, Enum):
    """Types de changement de couche"""
    WET = "wet"
    DIRTY = "dirty"
    BOTH = "both"
    CLEAN = "clean"


# ==================== SCHEMAS DE CREATION ====================

class DiaperCreateSchema(BaseModel):
    """
    Schema pour enregistrer un nouveau changement de couche
    """
    
    baby_id: int = Field(
        ...,
        gt=0,
        description="ID du bébé",
        example=1
    )
    
    changed_at: datetime = Field(
        ...,
        description="Date et heure du changement (format ISO 8601)",
        example="2026-02-01T14:30:00Z"
    )
    
    diaper_type: DiaperTypeEnum = Field(
        ...,
        description="Type de couche (wet, dirty, both, clean)",
        example="both"
    )
    
    notes: Optional[str] = Field(
        None,
        max_length=500,
        description="Remarques (couleur, texture, etc.)",
        example="Selles molles, couleur jaune"
    )
    
    rash_detected: bool = Field(
        False,
        description="Érythème fessier détecté ?",
        example=False
    )
    
    cream_applied: bool = Field(
        False,
        description="Crème protectrice appliquée ?",
        example=True
    )
    
    # Validators
    
    @validator('changed_at')
    def validate_changed_at(cls, v: datetime) -> datetime:
        """Valide la date de changement"""
        now = datetime.now(v.tzinfo) if v.tzinfo else datetime.now()
        
        # Ne peut pas être dans le futur
        if v > now:
            raise ValueError("Diaper change time cannot be in the future")
        
        # Pas plus de 7 jours dans le passé (limite raisonnable)
        from datetime import timedelta
        one_week_ago = now - timedelta(days=7)
        if v < one_week_ago:
            raise ValueError("Diaper change cannot be more than 7 days in the past")
        
        return v
    
    @validator('notes')
    def validate_notes(cls, v: Optional[str]) -> Optional[str]:
        """Valide les notes"""
        if v is None:
            return v
        
        # Nettoyer les espaces
        v = v.strip()
        
        if len(v) == 0:
            return None
        
        return v
    
    class Config:
        json_schema_extra = {
            "example": {
                "baby_id": 1,
                "changed_at": "2026-02-01T14:30:00Z",
                "diaper_type": "both",
                "notes": "Selles molles, couleur jaune moutarde",
                "rash_detected": False,
                "cream_applied": True
            }
        }


# ==================== SCHEMAS DE MISE A JOUR ====================

class DiaperUpdateSchema(BaseModel):
    """
    Schema pour mettre à jour un changement de couche
    Tous les champs sont optionnels (PATCH)
    """
    
    changed_at: Optional[datetime] = Field(
        None,
        description="Nouvelle date/heure du changement"
    )
    
    diaper_type: Optional[DiaperTypeEnum] = Field(
        None,
        description="Nouveau type de couche"
    )
    
    notes: Optional[str] = Field(
        None,
        max_length=500,
        description="Nouvelles remarques"
    )
    
    rash_detected: Optional[bool] = Field(
        None,
        description="Érythème détecté ?"
    )
    
    cream_applied: Optional[bool] = Field(
        None,
        description="Crème appliquée ?"
    )
    
    # Réutiliser les validators
    _validate_changed_at = validator('changed_at', allow_reuse=True)(
        DiaperCreateSchema.validate_changed_at
    )
    _validate_notes = validator('notes', allow_reuse=True)(
        DiaperCreateSchema.validate_notes
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "notes": "Ajout : texture normale après vérification",
                "cream_applied": True
            }
        }


# ==================== SCHEMAS DE REPONSE ====================

class TimeSinceChangeSchema(BaseModel):
    """Informations sur le temps écoulé depuis le changement"""
    hours: int = Field(..., description="Heures écoulées", example=2)
    minutes: int = Field(..., description="Minutes écoulées", example=45)
    total_minutes: int = Field(..., description="Total en minutes", example=165)


class DiaperResponseSchema(BaseModel):
    """
    Schema de réponse pour un changement de couche
    """
    
    id: int = Field(..., description="ID unique du changement")
    baby_id: int = Field(..., description="ID du bébé")
    changed_at: datetime = Field(..., description="Date/heure du changement")
    diaper_type: DiaperTypeEnum = Field(..., description="Type de couche")
    notes: Optional[str] = Field(None, description="Remarques")
    rash_detected: bool = Field(..., description="Érythème détecté")
    cream_applied: bool = Field(..., description="Crème appliquée")
    time_since: TimeSinceChangeSchema = Field(..., description="Temps écoulé")
    created_at: datetime = Field(..., description="Date de création")
    updated_at: datetime = Field(..., description="Dernière modification")
    
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "baby_id": 1,
                "changed_at": "2026-02-01T14:30:00Z",
                "diaper_type": "both",
                "notes": "Selles molles, couleur normale",
                "rash_detected": False,
                "cream_applied": True,
                "time_since": {
                    "hours": 2,
                    "minutes": 45,
                    "total_minutes": 165
                },
                "created_at": "2026-02-01T14:32:00Z",
                "updated_at": "2026-02-01T14:32:00Z"
            }
        }


class DiaperListResponseSchema(BaseModel):
    """
    Schema pour liste de changements de couches (avec pagination)
    """
    total: int = Field(..., description="Nombre total d'enregistrements")
    skip: int = Field(..., description="Nombre d'éléments sautés")
    limit: int = Field(..., description="Limite par page")
    items: list[DiaperResponseSchema] = Field(..., description="Liste des changements")
    
    class Config:
        json_schema_extra = {
            "example": {
                "total": 15,
                "skip": 0,
                "limit": 10,
                "items": [
                    {
                        "id": 1,
                        "baby_id": 1,
                        "changed_at": "2026-02-01T14:30:00Z",
                        "diaper_type": "both",
                        "notes": None,
                        "rash_detected": False,
                        "cream_applied": True,
                        "time_since": {"hours": 0, "minutes": 30, "total_minutes": 30},
                        "created_at": "2026-02-01T14:32:00Z",
                        "updated_at": "2026-02-01T14:32:00Z"
                    }
                ]
            }
        }


# ==================== SCHEMAS STATISTIQUES ====================

class DiaperStatsSchema(BaseModel):
    """
    Statistiques sur les changements de couches
    """
    total_changes: int = Field(..., description="Nombre total de changements")
    changes_today: int = Field(..., description="Changements aujourd'hui")
    last_change: Optional[DiaperResponseSchema] = Field(None, description="Dernier changement")
    
    # Répartition par type
    wet_count: int = Field(..., description="Nombre de couches mouillées")
    dirty_count: int = Field(..., description="Nombre de couches salies")
    both_count: int = Field(..., description="Nombre de couches mouillées et salies")
    clean_count: int = Field(..., description="Nombre de changements préventifs")
    
    # Alertes
    rash_detected_count: int = Field(..., description="Nombre de fois où érythème détecté")
    average_interval_minutes: Optional[int] = Field(
        None, 
        description="Intervalle moyen entre changements (en minutes)"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "total_changes": 42,
                "changes_today": 6,
                "last_change": {
                    "id": 42,
                    "baby_id": 1,
                    "changed_at": "2026-02-01T14:30:00Z",
                    "diaper_type": "wet",
                    "notes": None,
                    "rash_detected": False,
                    "cream_applied": False,
                    "time_since": {"hours": 1, "minutes": 15, "total_minutes": 75},
                    "created_at": "2026-02-01T14:32:00Z",
                    "updated_at": "2026-02-01T14:32:00Z"
                },
                "wet_count": 20,
                "dirty_count": 10,
                "both_count": 10,
                "clean_count": 2,
                "rash_detected_count": 3,
                "average_interval_minutes": 180
            }
        }


class DailyDiaperSummarySchema(BaseModel):
    """
    Résumé journalier des changements de couches
    """
    date: str = Field(..., description="Date (YYYY-MM-DD)", example="2026-02-01")
    total_changes: int = Field(..., description="Nombre total de changements ce jour")
    wet_count: int = Field(..., description="Couches mouillées")
    dirty_count: int = Field(..., description="Couches salies")
    both_count: int = Field(..., description="Les deux")
    rash_detected: bool = Field(..., description="Érythème détecté ce jour ?")


# ==================== SCHEMAS D'ERREUR ====================

class ErrorResponseSchema(BaseModel):
    """Schema standard pour les erreurs"""
    detail: str = Field(..., description="Message d'erreur")
    error_code: Optional[str] = Field(None, description="Code d'erreur spécifique")
    
    class Config:
        json_schema_extra = {
            "example": {
                "detail": "Diaper change not found",
                "error_code": "DIAPER_NOT_FOUND"
            }
        }
