from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import Optional
from enum import Enum

class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"

class BabyBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    gender: Gender
    birth_date: date
    birth_weight: Optional[float] = Field(None, ge=0.5, le=10.0)  # kg
    birth_height: Optional[float] = Field(None, ge=30, le=70)     # cm

class BabyCreate(BabyBase):
    parent_id: int

class BabyUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    birth_weight: Optional[float] = Field(None, ge=0.5, le=10.0)
    birth_height: Optional[float] = Field(None, ge=30, le=70)

class BabyInDB(BabyBase):
    id: int
    parent_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class BabyResponse(BabyInDB):
    age_days: Optional[int] = None
    age_months: Optional[float] = None
