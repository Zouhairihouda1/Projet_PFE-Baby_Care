# 📁 backend/src/core/models/feeding.py
from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional, List
from enum import Enum

class FeedingType(str, Enum):
    BREAST_MILK = "breast_milk"
    FORMULA = "formula"
    SOLID_FOOD = "solid_food"
    WATER = "water"
    MIXED = "mixed"

class BreastSide(str, Enum):
    LEFT = "left"
    RIGHT = "right"
    BOTH = "both"
    NOT_APPLICABLE = "not_applicable"

class SolidFoodType(str, Enum):
    PUREE = "puree"
    CEREALS = "cereals"
    FRUITS = "fruits"
    VEGETABLES = "vegetables"
    MEAT = "meat"
    FISH = "fish"
    DAIRY = "dairy"
    OTHER = "other"

class FeedingBase(BaseModel):
    baby_id: int
    type: FeedingType
    start_time: datetime = Field(default_factory=datetime.now)
    end_time: Optional[datetime] = None
    duration_minutes: Optional[int] = None
    
    # Quantités
    quantity_ml: Optional[float] = None  # pour liquides
    quantity_grams: Optional[float] = None  # pour solides
    
    # Allaitement
    breast_side: BreastSide = BreastSide.NOT_APPLICABLE
    breast_empty: bool = False
    
    # Solides
    solid_food_type: Optional[SolidFoodType] = None
    food_name: Optional[str] = None
    
    # Biberon
    formula_brand: Optional[str] = None
    formula_type: Optional[str] = None
    water_ml: Optional[float] = None
    formula_scoops: Optional[int] = None
    
    # Notes
    notes: Optional[str] = None
    was_refused: bool = False
    vomiting: bool = False
    reflux: bool = False
    
    @validator('duration_minutes')
    def validate_duration(cls, v, values):
        if v is not None and v < 0:
            raise ValueError('Duration cannot be negative')
        return v
    
    @validator('quantity_ml')
    def validate_quantity_ml(cls, v, values):
        if v is not None and v < 0:
            raise ValueError('Quantity cannot be negative')
        return v

class FeedingCreate(FeedingBase):
    pass

class FeedingUpdate(BaseModel):
    end_time: Optional[datetime] = None
    duration_minutes: Optional[int] = None
    quantity_ml: Optional[float] = None
    quantity_grams: Optional[float] = None
    breast_side: Optional[BreastSide] = None
    breast_empty: Optional[bool] = None
    notes: Optional[str] = None
    was_refused: Optional[bool] = None
    vomiting: Optional[bool] = None
    reflux: Optional[bool] = None

class FeedingInDB(FeedingBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class FeedingResponse(FeedingInDB):
    pass

# Statistiques
class FeedingStatistics(BaseModel):
    total_today: int = 0
    total_ml_today: float = 0.0
    total_grams_today: float = 0.0
    average_interval_minutes: float = 0.0
    breast_milk_count: int = 0
    formula_count: int = 0
    solid_food_count: int = 0
    last_feeding_time: Optional[datetime] = None
    next_feeding_estimate: Optional[datetime] = None
    
class FeedingTrend(BaseModel):
    date: str
    total_feedings: int
    total_ml: float
    total_grams: float

# Pour les graphiques
class FeedingChartData(BaseModel):
    labels: List[str]
    breast_milk_data: List[float]
    formula_data: List[float]
    solid_food_data: List[float]
