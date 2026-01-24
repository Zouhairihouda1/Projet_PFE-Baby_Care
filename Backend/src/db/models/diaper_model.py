from sqlalchemy import Column, Integer, DateTime, Enum, ForeignKey, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from . import Base
import enum

class DiaperType(enum.Enum):
    WET = "wet"
    DIRTY = "dirty"
    MIXED = "mixed"

class DiaperConsistency(enum.Enum):
    NORMAL = "normal"
    LIQUID = "liquid"
    HARD = "hard"
    UNUSUAL = "unusual"

class Diaper(Base):
    __tablename__ = 'diapers'
    
    id = Column(Integer, primary_key=True, index=True)
    baby_id = Column(Integer, ForeignKey('babies.id'), nullable=False)
    type = Column(Enum(DiaperType), nullable=False)
    consistency = Column(Enum(DiaperConsistency), nullable=True)
    time = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    notes = Column(Text, nullable=True)
    
    # Relations
    baby = relationship("Baby", back_populates="diapers")
    
    def __repr__(self):
        return f"<Diaper {self.type} at {self.time}>"
