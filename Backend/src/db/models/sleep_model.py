# 📁 backend/src/db/models/sleep_model.py
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Enum, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from ..base import Base

class SleepType(enum.Enum):
    NAP = "nap"              # Sieste
    NIGHT_SLEEP = "night_sleep"  # Nuit complète
    BEDTIME = "bedtime"      # Heure du coucher
    WAKEUP = "wakeup"        # Réveil

class SleepQuality(enum.Enum):
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    RESTLESS = "restless"

class SleepEnvironment(enum.Enum):
    CRIB = "crib"           # Lit à barreaux
    BASSINET = "bassinet"   # Berceau
    PARENT_BED = "parent_bed"  # Lit parental
    SWING = "swing"         # Balancelle
    CAR_SEAT = "car_seat"   # Siège auto
    STROLLER = "stroller"   # Poussette
    OTHER = "other"

class SleepModel(Base):
    __tablename__ = "sleep_sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    baby_id = Column(Integer, ForeignKey("babies.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Type et durée
    type = Column(Enum(SleepType), nullable=False)
    start_time = Column(DateTime, nullable=False, default=func.now())
    end_time = Column(DateTime)
    duration_minutes = Column(Integer)  # en minutes
    
    # Qualité et environnement
    quality = Column(Enum(SleepQuality), default=SleepQuality.GOOD)
    environment = Column(Enum(SleepEnvironment), default=SleepEnvironment.CRIB)
    room_temperature = Column(Float)  # en °C
    was_swaddled = Column(Boolean, default=False)
    used_white_noise = Column(Boolean, default=False)
    used_pacifier = Column(Boolean, default=False)
    
    # Position et mouvements
    sleep_position = Column(String(50))  # "back", "side", "stomach"
    wakeups_count = Column(Integer, default=0)
    longest_stretch_minutes = Column(Integer)  # plus longue période de sommeil
    
    # Alimentation liée au sommeil
    fed_before_sleep = Column(Boolean, default=False)
    feeding_minutes_before = Column(Integer)  # minutes avant le sommeil
    
    # Notes et observations
    notes = Column(Text)
    dreams_observed = Column(Boolean, default=False)
    snoring = Column(Boolean, default=False)
    breathing_issues = Column(Boolean, default=False)
    
    # Métadonnées
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Relations
    baby = relationship("BabyModel", back_populates="sleep_sessions")
    user = relationship("UserModel", back_populates="sleep_sessions")
    
    def __repr__(self):
        return f"<Sleep(id={self.id}, baby_id={self.baby_id}, type={self.type})>"

