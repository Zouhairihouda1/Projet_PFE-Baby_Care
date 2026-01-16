from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum
from db.database import Base

class FeedingType(enum.Enum):
    BREAST = "breast"
    BOTTLE = "bottle"
    FORMULA = "formula"
    SOLID = "solid"

class Feeding(Base):
    __tablename__ = 'feedings'
    
    id = Column(Integer, primary_key=True, index=True)
    baby_id = Column(Integer, ForeignKey('babies.id'), nullable=False)
    type = Column(Enum(FeedingType), nullable=False)
    amount = Column(Float)  # en ml ou grammes
    duration = Column(Integer)  # en minutes
    notes = Column(String(500))
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)
    
    # Relation avec Baby
    baby = relationship("Baby", back_populates="feedings")
    
    def __repr__(self):
        return f"<Feeding {self.type} for Baby {self.baby_id}>"
