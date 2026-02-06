from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKey, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from . import Base
import enum

class SleepType(enum.Enum):
    NIGHT = "night"
    NAP = "nap"
    DAY_SLEEP = "day_sleep"

class Sleep(Base):
    __tablename__ = 'sleeps'
    
    id = Column(Integer, primary_key=True, index=True)
    baby_id = Column(Integer, ForeignKey('babies.id'), nullable=False)
    type = Column(Enum(SleepType), nullable=False)
    start_time = Column(DateTime(timezone=True), nullable=False, index=True)
    end_time = Column(DateTime(timezone=True), nullable=True)
    quality = Column(Integer, nullable=True)  # 1-5 échelle
    notes = Column(Text, nullable=True)
    
    # Calcul de la durée (à faire dans une propriété ou méthode)
    
    # Relations
    baby = relationship("Baby", back_populates="sleeps")
    
    def __repr__(self):
        return f"<Sleep {self.type} from {self.start_time}>"
