# 📁 backend/src/core/models/sleep.py
from pydantic import BaseModel, Field, validator, ConfigDict
from datetime import datetime, time
from typing import Optional, List, Dict, Any
from enum import Enum
import re

class SleepType(str, Enum):
    NAP = "nap"
    NIGHT_SLEEP = "night_sleep"
    BEDTIME = "bedtime"
    WAKEUP = "wakeup"

class SleepQuality(str, Enum):
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    RESTLESS = "restless"

class SleepEnvironment(str, Enum):
    CRIB = "crib"
    BASSINET = "bassinet"
    PARENT_BED = "parent_bed"
    SWING = "swing"
    CAR_SEAT = "car_seat"
    STROLLER = "stroller"
    OTHER = "other"

class SleepBase(BaseModel):
    baby_id: int
    type: SleepType
    start_time: datetime = Field(default_factory=datetime.now)
    end_time: Optional[datetime] = None
    duration_minutes: Optional[int] = Field(None, ge=0, le=1440)  # max 24h
    
    # Qualité et environnement
    quality: SleepQuality = SleepQuality.GOOD
    environment: SleepEnvironment = SleepEnvironment.CRIB
    room_temperature: Optional[float] = Field(None, ge=15, le=30)  # °C
    was_swaddled: bool = False
    used_white_noise: bool = False
    used_pacifier: bool = False
    
    # Position
    sleep_position: Optional[str] = None
    wakeups_count: int = Field(0, ge=0)
    longest_stretch_minutes: Optional[int] = Field(None, ge=0)
    
    # Alimentation
    fed_before_sleep: bool = False
    feeding_minutes_before: Optional[int] = Field(None, ge=0)
    
    # Notes
    notes: Optional[str] = None
    dreams_observed: bool = False
    snoring: bool = False
    breathing_issues: bool = False
    
    @validator('sleep_position')
    def validate_position(cls, v):
        if v and v not in ['back', 'side', 'stomach', 'varied']:
            raise ValueError('Position must be back, side, stomach, or varied')
        return v
    
    @validator('end_time')
    def validate_end_time(cls, v, values):
        if v and 'start_time' in values and v < values['start_time']:
            raise ValueError('End time cannot be before start time')
        return v
    
    @validator('duration_minutes')
    def calculate_duration(cls, v, values):
        if v is None and 'start_time' in values and 'end_time' in values:
            if values['start_time'] and values['end_time']:
                duration = (values['end_time'] - values['start_time']).total_seconds() / 60
                return int(duration)
        return v

class SleepCreate(SleepBase):
    pass

class SleepUpdate(BaseModel):
    end_time: Optional[datetime] = None
    duration_minutes: Optional[int] = None
    quality: Optional[SleepQuality] = None
    environment: Optional[SleepEnvironment] = None
    wakeups_count: Optional[int] = None
    longest_stretch_minutes: Optional[int] = None
    notes: Optional[str] = None
    snoring: Optional[bool] = None
    breathing_issues: Optional[bool] = None

class SleepInDB(SleepBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class SleepResponse(SleepInDB):
    pass

# Statistiques
class SleepStatistics(BaseModel):
    total_sleep_today_minutes: float = 0.0
    total_naps_today: int = 0
    total_night_sleep_minutes: float = 0.0
    average_nap_duration: float = 0.0
    sleep_efficiency: float = 0.0  # pourcentage
    wakeups_per_hour: float = 0.0
    sleep_cycles: int = 0
    bedtime_consistency: float = 0.0  # régularité heure coucher
    last_sleep_end: Optional[datetime] = None
    next_nap_prediction: Optional[datetime] = None

class SleepTrend(BaseModel):
    date: str
    total_sleep_minutes: float
    night_sleep_minutes: float
    nap_count: int
    average_quality: float

# Pour les graphiques
class SleepChartData(BaseModel):
    labels: List[str]
    total_sleep_data: List[float]
    night_sleep_data: List[float]
    nap_count_data: List[int]
    quality_data: List[float]

# Rythme de sommeil
class SleepRhythm(BaseModel):
    age_group: str  # "0-3m", "3-6m", "6-12m", "12-24m"
    total_sleep_hours: Dict[str, float]  # day_night totals
    nap_count: int
    nap_duration_range: Dict[str, float]  # min-max
    bedtime_range: Dict[str, time]  # recommended bedtime
    wakeup_range: Dict[str, time]  # recommended wakeup

# Recommandations
class SleepRecommendation(BaseModel):
    category: str  # "duration", "environment", "routine", "safety"
    title: str
    description: str
    priority: int  # 1-5, 5 étant le plus important
    action_items: List[str]
