# 📁 backend/src/db/models/feeding_model.py
from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum
from ..base import Base

class FeedingType(enum.Enum):
    BREAST_MILK = "breast_milk"      # Lait maternel
    FORMULA = "formula"              # Lait en poudre
    SOLID_FOOD = "solid_food"        # Nourriture solide
    WATER = "water"                  # Eau
    MIXED = "mixed"                  # Mixte

class BreastSide(enum.Enum):
    LEFT = "left"
    RIGHT = "right"
    BOTH = "both"
    NOT_APPLICABLE = "not_applicable"

class SolidFoodType(enum.Enum):
    PUREE = "puree"
    CEREALS = "cereals"
    FRUITS = "fruits"
    VEGETABLES = "vegetables"
    MEAT = "meat"
    FISH = "fish"
    DAIRY = "dairy"
    OTHER = "other"

class FeedingModel(Base):
    __tablename__ = "feedings"
    
    id = Column(Integer, primary_key=True, index=True)
    baby_id = Column(Integer, ForeignKey("babies.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Type et durée
    type = Column(Enum(FeedingType), nullable=False)
    start_time = Column(DateTime, nullable=False, default=func.now())
    end_time = Column(DateTime)
    duration_minutes = Column(Integer)  # en minutes
    
    # Quantités
    quantity_ml = Column(Float)  # en ml pour les liquides
    quantity_grams = Column(Float)  # en grammes pour solides
    
    # Allaitement spécifique
    breast_side = Column(Enum(BreastSide), default=BreastSide.NOT_APPLICABLE)
    breast_empty = Column(Boolean, default=False)
    
    # Nourriture solide spécifique
    solid_food_type = Column(Enum(SolidFoodType))
    food_name = Column(String(255))
    
    # Biberon spécifique
    formula_brand = Column(String(100))
    formula_type = Column(String(100))
    water_ml = Column(Float)
    formula_scoops = Column(Integer)
    
    # Notes et statut
    notes = Column(String(1000))
    was_refused = Column(Boolean, default=False)
    vomiting = Column(Boolean, default=False)
    reflux = Column(Boolean, default=False)
    
    # Métadonnées
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Relations
    baby = relationship("BabyModel", back_populates="feedings")
    user = relationship("UserModel", back_populates="feedings")
    
    def __repr__(self):
        return f"<Feeding(id={self.id}, baby_id={self.baby_id}, type={self.type})>"

