from sqlalchemy import Column, Integer, String, DateTime, Enum, Text, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from . import Base
import enum

class AdviceCategory(enum.Enum):
    FEEDING = "feeding"
    SLEEP = "sleep"
    HEALTH = "health"
    DEVELOPMENT = "development"
    SAFETY = "safety"
    GENERAL = "general"

class Advice(Base):
    __tablename__ = 'advices'
    
    id = Column(Integer, primary_key=True, index=True)
    category = Column(Enum(AdviceCategory), nullable=False, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    min_age_days = Column(Integer, nullable=True)  # Âge minimum en jours
    max_age_days = Column(Integer, nullable=True)  # Âge maximum en jours
    tags = Column(String(500), nullable=True)  # Tags séparés par des virgules
    source = Column(String(200), nullable=True)
    is_featured = Column(Boolean, default=False)
    view_count = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    def __repr__(self):
        return f"<Advice {self.title}>"
