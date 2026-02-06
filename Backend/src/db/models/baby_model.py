"""
SQLAlchemy Model for Baby Profile
Représente la table 'babies' dans PostgreSQL
"""

from sqlalchemy import Column, Integer, String, Date, Enum, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from datetime import date, datetime
import enum

from app.db.base import Base


class GenderEnum(str, enum.Enum):
    """Enum pour le genre du bébé"""
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"


class Baby(Base):
    """
    Modèle de profil bébé
    
    Relations:
    - user: Utilisateur parent (Many-to-One)
    - biometrics: Données biométriques (One-to-Many)
    - vaccinations: Vaccinations (One-to-Many)
    - feedings: Alimentations (One-to-Many)
    - sleeps: Sommeils (One-to-Many)
    - diapers: Couches (One-to-Many)
    - medical_records: Dossiers médicaux (One-to-Many)
    """
    
    __tablename__ = "babies"
    
    # Colonnes principales
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(
        Integer, 
        ForeignKey("users.id", ondelete="CASCADE"), 
        nullable=False,
        index=True,
        comment="ID du parent propriétaire"
    )
    name = Column(
        String(100), 
        nullable=False,
        comment="Prénom du bébé"
    )
    birth_date = Column(
        Date, 
        nullable=False,
        index=True,
        comment="Date de naissance"
    )
    gender = Column(
        Enum(GenderEnum, name="gender_enum"),
        nullable=False,
        comment="Genre du bébé"
    )
    photo_url = Column(
        String(500), 
        nullable=True,
        comment="URL de la photo de profil"
    )
    
    # Métadonnées
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
        comment="Date de création du profil"
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
        comment="Date de dernière modification"
    )
    deleted_at = Column(
        DateTime(timezone=True),
        nullable=True,
        comment="Date de suppression (soft delete)"
    )
    
    # Relations
    user = relationship(
        "User", 
        back_populates="babies",
        lazy="joined"  # Charge automatiquement l'utilisateur
    )
    
    biometrics = relationship(
        "Biometric",
        back_populates="baby",
        cascade="all, delete-orphan",
        lazy="dynamic",  # Requête à la demande
        order_by="Biometric.recorded_at.desc()"
    )
    
    vaccinations = relationship(
        "Vaccination",
        back_populates="baby",
        cascade="all, delete-orphan",
        lazy="dynamic",
        order_by="Vaccination.scheduled_date.asc()"
    )
    
    feedings = relationship(
        "Feeding",
        back_populates="baby",
        cascade="all, delete-orphan",
        lazy="dynamic",
        order_by="Feeding.recorded_at.desc()"
    )
    
    sleeps = relationship(
        "Sleep",
        back_populates="baby",
        cascade="all, delete-orphan",
        lazy="dynamic",
        order_by="Sleep.start_time.desc()"
    )
    
    diapers = relationship(
        "Diaper",
        back_populates="baby",
        cascade="all, delete-orphan",
        lazy="dynamic",
        order_by="Diaper.changed_at.desc()"
    )
    
    medical_records = relationship(
        "MedicalRecord",
        back_populates="baby",
        cascade="all, delete-orphan",
        lazy="dynamic",
        order_by="MedicalRecord.consultation_date.desc()"
    )
    
    # Méthodes
    def calculate_age(self) -> dict:
        """
        Calcule l'âge du bébé en jours, semaines et mois
        
        Returns:
            dict: {
                "days": int,
                "weeks": int,
                "months": int,
                "years": int
            }
        """
        today = date.today()
        delta = today - self.birth_date
        
        # Calculs
        days = delta.days
        weeks = days // 7
        
        # Calcul des mois
        months = (today.year - self.birth_date.year) * 12 + (today.month - self.birth_date.month)
        if today.day < self.birth_date.day:
            months -= 1
        
        # Calcul des années
        years = months // 12
        
        return {
            "days": max(0, days),
            "weeks": max(0, weeks),
            "months": max(0, months),
            "years": max(0, years)
        }
    
    def is_deleted(self) -> bool:
        """Vérifie si le profil est supprimé (soft delete)"""
        return self.deleted_at is not None
    
    def soft_delete(self):
        """Marque le profil comme supprimé sans le supprimer de la BDD"""
        self.deleted_at = datetime.utcnow()
    
    def restore(self):
        """Restaure un profil supprimé"""
        self.deleted_at = None
    
    def __repr__(self) -> str:
        return f"<Baby(id={self.id}, name='{self.name}', birth_date={self.birth_date})>"
    
    def __str__(self) -> str:
        age = self.calculate_age()
        return f"{self.name} ({age['months']} mois)"


# Index composites pour performance
from sqlalchemy import Index

# Index pour recherche rapide par utilisateur et statut
Index(
    'ix_babies_user_active',
    Baby.user_id,
    Baby.deleted_at,
    postgresql_where=(Baby.deleted_at.is_(None))
)
