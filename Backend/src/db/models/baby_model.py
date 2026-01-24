from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey, DateTime, Float
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum

class Gender(enum.Enum):
    MALE = 'male'
    FEMALE = 'femelle'

class Baby():
    __tablename__ = 'babies'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    gender = Column(Enum(Gender), nullable=False)
    birth_weight = Column(Integer, nullable=True)  # en grammes
    birth_height = Column(Integer, nullable=True)  # en cm

    
    # Relations
    #celle de profils
    user = relationship('User', back_populates='babies')
    biometrics = relationship('Biometric', back_populates='baby')
    vaccinations = relationship('Vaccination', back_populates='baby')
    feedings = relationship('Feeding', back_populates='baby')
    sleeps = relationship('Sleep', back_populates='baby')
    diapers = relationship('Diaper', back_populates='baby')
def __repr__(self):
        return f"<Baby {self.first_name} {self.last_name}>"
