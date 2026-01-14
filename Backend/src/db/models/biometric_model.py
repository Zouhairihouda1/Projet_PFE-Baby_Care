from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.base import Base

class Biometric(Base):
    __tablename__ = 'biometrics'
    
    id = Column(Integer, primary_key=True, index=True)
    baby_id = Column(Integer, ForeignKey('babies.id'), nullable=False)
    weight = Column(Float, nullable=False)  # en kg
    height = Column(Float, nullable=False)  # en cm
    head_circumference = Column(Float, nullable=True)  # en cm
    temperature = Column(Float, nullable=True)  # en °C
    measured_at = Column(DateTime(timezone=True), nullable=False)
    notes = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    baby = relationship('Baby', back_populates='biometrics')
