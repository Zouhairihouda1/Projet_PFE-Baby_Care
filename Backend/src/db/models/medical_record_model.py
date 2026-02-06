from sqlalchemy import Column, Integer, String, DateTime, Date, Float, Enum, ForeignKey, Text
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from . import Base
import enum

class RecordType(enum.Enum):
    CONSULTATION = "consultation"
    HOSPITALIZATION = "hospitalization"
    EMERGENCY = "emergency"
    FOLLOW_UP = "follow_up"

class Symptom(Base):
    __tablename__ = 'symptoms'
    
    id = Column(Integer, primary_key=True, index=True)
    baby_id = Column(Integer, ForeignKey('babies.id'), nullable=False)
    symptom_name = Column(String(200), nullable=False)
    start_date = Column(DateTime(timezone=True), nullable=False)
    end_date = Column(DateTime(timezone=True), nullable=True)
    severity = Column(Integer, nullable=True)  # 1-10 échelle
    notes = Column(Text, nullable=True)
    
    # Relations
    baby = relationship("Baby")
    medical_records = relationship("MedicalRecord", secondary="record_symptoms")
    
    def __repr__(self):
        return f"<Symptom {self.symptom_name}>"

class MedicalRecord(Base):
    __tablename__ = 'medical_records'
    
    id = Column(Integer, primary_key=True, index=True)
    baby_id = Column(Integer, ForeignKey('babies.id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    record_type = Column(Enum(RecordType), nullable=False)
    visit_date = Column(Date, nullable=False)
    clinic_name = Column(String(200), nullable=True)
    doctor_name = Column(String(200), nullable=True)
    diagnosis = Column(Text, nullable=True)
    prescription = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)
    temperature = Column(Float, nullable=True)
    weight = Column(Float, nullable=True)
    height = Column(Float, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relations
    baby = relationship("Baby", back_populates="medical_records")
    doctor = relationship("User", back_populates="medical_records", foreign_keys=[doctor_id])
    symptoms = relationship("Symptom", secondary="record_symptoms")
    
    def __repr__(self):
        return f"<MedicalRecord {self.record_type} on {self.visit_date}>"

# Table d'association pour symptômes
class RecordSymptom(Base):
    __tablename__ = 'record_symptoms'
    
    record_id = Column(Integer, ForeignKey('medical_records.id'), primary_key=True)
    symptom_id = Column(Integer, ForeignKey('symptoms.id'), primary_key=True)
