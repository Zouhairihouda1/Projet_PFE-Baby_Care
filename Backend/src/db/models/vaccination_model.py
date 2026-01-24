from sqlalchemy import Column, Integer, String, DateTime, Date, Enum, Boolean, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from . import Base
import enum

class VaccineStatus(enum.Enum):
    PENDING = "pending"
    ADMINISTERED = "administered"
    MISSED = "missed"
    UPCOMING = "upcoming"

class VaccineSchedule(Base):
    __tablename__ = 'vaccine_schedules'
    
    id = Column(Integer, primary_key=True, index=True)
    baby_id = Column(Integer, ForeignKey('babies.id'), nullable=False)
    vaccine_name = Column(String(200), nullable=False)
    vaccine_code = Column(String(50), nullable=False)  # Code standard (ex: "DTaP")
    recommended_age_days = Column(Integer, nullable=False)  # Âge en jours
    dose_number = Column(Integer, nullable=False)
    total_doses = Column(Integer, nullable=False)
    description = Column(String(500), nullable=True)
    
    # Relations
    baby = relationship("Baby", back_populates="vaccine_schedules")
    vaccinations = relationship("Vaccination", back_populates="schedule")
    
    def __repr__(self):
        return f"<VaccineSchedule {self.vaccine_name} dose {self.dose_number}>"

class Vaccination(Base):
    __tablename__ = 'vaccinations'
    
    id = Column(Integer, primary_key=True, index=True)
    baby_id = Column(Integer, ForeignKey('babies.id'), nullable=False)
    schedule_id = Column(Integer, ForeignKey('vaccine_schedules.id'), nullable=True)
    vaccine_name = Column(String(200), nullable=False)
    dose_number = Column(Integer, nullable=False)
    administration_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    status = Column(Enum(VaccineStatus), default=VaccineStatus.PENDING)
    administered_at_clinic = Column(String(200), nullable=True)
    administered_by = Column(String(200), nullable=True)
    notes = Column(String(500), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relations
    baby = relationship("Baby", back_populates="vaccinations")
    schedule = relationship("VaccineSchedule", back_populates="vaccinations")
    
    def __repr__(self):
        return f"<Vaccination {self.vaccine_name} on {self.administration_date}>"
