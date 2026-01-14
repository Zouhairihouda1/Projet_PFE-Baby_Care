from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey, DateTime, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.base import Base
import enum

class Gender(enum.Enum):
    MALE = 'male'
    FEMALE = 'female'

class Baby(Base):
    __tablename__ = 'babies'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    gender = Column(Enum(Gender), nullable=False)
    birth_weight = Column(Integer, nullable=True)  # en grammes
    birth_height = Column(Integer, nullable=True)  # en cm
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relations
    user = relationship('User', back_populates='babies')
    biometrics = relationship('Biometric', back_populates='baby')
    vaccinations = relationship('Vaccination', back_populates='baby')
    feedings = relationship('Feeding', back_populates='baby')
    sleeps = relationship('Sleep', back_populates='baby')
    diapers = relationship('Diaper', back_populates='baby')
