"""
SQLAlchemy Model for Diaper Changes (Hygiene tracking)
Représente la table 'diapers' dans PostgreSQL
Spécification 3.3 du cahier des charges - Suivi Quotidien
"""

from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, Enum, ForeignKey, func
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from app.db.base import Base


class DiaperType(str, enum.Enum):
    """
    Types de changement de couche
    """
    WET = "wet"           # Mouillée (urine seulement)
    DIRTY = "dirty"       # Salie (selles seulement)
    BOTH = "both"         # Les deux (urine + selles)
    CLEAN = "clean"       # Changement préventif (couche propre)


class Diaper(Base):
    """
    Modèle pour les changements de couche
    
    Relations:
    - baby: Bébé concerné (Many-to-One)
    """
    
    __tablename__ = "diapers"
    
    # Colonnes principales
    id = Column(
        Integer, 
        primary_key=True, 
        index=True, 
        autoincrement=True,
        comment="ID unique du changement"
    )
    
    baby_id = Column(
        Integer, 
        ForeignKey("babies.id", ondelete="CASCADE"), 
        nullable=False,
        index=True,
        comment="ID du bébé concerné"
    )
    
    changed_at = Column(
        DateTime(timezone=True),
        nullable=False,
        index=True,
        comment="Date et heure du changement de couche"
    )
    
    diaper_type = Column(
        Enum(DiaperType, name="diaper_type_enum"),
        nullable=False,
        comment="Type de couche (wet, dirty, both, clean)"
    )
    
    notes = Column(
        Text,
        nullable=True,
        comment="Remarques sur la couche (texture, couleur, consistance, etc.)"
    )
    
    rash_detected = Column(
        Boolean,
        nullable=False,
        default=False,
        comment="Érythème fessier (rougeur) détecté ?"
    )
    
    cream_applied = Column(
        Boolean,
        nullable=False,
        default=False,
        comment="Crème protectrice appliquée ?"
    )
    
    # Métadonnées
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
        comment="Date de création de l'enregistrement"
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
    baby = relationship(
        "Baby",
        back_populates="diapers",
        lazy="joined"
    )
    
    # Méthodes
    def is_dirty(self) -> bool:
        """Vérifie si la couche contenait des selles"""
        return self.diaper_type in [DiaperType.DIRTY, DiaperType.BOTH]
    
    def is_wet(self) -> bool:
        """Vérifie si la couche était mouillée"""
        return self.diaper_type in [DiaperType.WET, DiaperType.BOTH]
    
    def needs_attention(self) -> bool:
        """Vérifie si le changement nécessite une attention particulière"""
        return self.rash_detected or (self.notes is not None and len(self.notes) > 0)
    
    def time_since_change(self) -> dict:
        """Calcule le temps écoulé depuis le changement"""
        now = datetime.now(self.changed_at.tzinfo)
        delta = now - self.changed_at
        
        hours = delta.total_seconds() // 3600
        minutes = (delta.total_seconds() % 3600) // 60
        
        return {
            "hours": int(hours),
            "minutes": int(minutes),
            "total_minutes": int(delta.total_seconds() // 60)
        }
    
    def soft_delete(self):
        """Marque l'enregistrement comme supprimé"""
        self.deleted_at = datetime.utcnow()
    
    def restore(self):
        """Restaure un enregistrement supprimé"""
        self.deleted_at = None
    
    def is_deleted(self) -> bool:
        """Vérifie si l'enregistrement est supprimé"""
        return self.deleted_at is not None
    
    def __repr__(self) -> str:
        return (
            f"<Diaper(id={self.id}, baby_id={self.baby_id}, "
            f"type={self.diaper_type.value}, changed_at={self.changed_at})>"
        )
    
    def __str__(self) -> str:
        type_fr = {
            DiaperType.WET: "mouillée",
            DiaperType.DIRTY: "salie",
            DiaperType.BOTH: "mouillée et salie",
            DiaperType.CLEAN: "propre"
        }
        return f"Couche {type_fr.get(self.diaper_type)} - {self.changed_at.strftime('%H:%M')}"


# Index composites pour performance
from sqlalchemy import Index

# Index pour récupération rapide par bébé et date
Index(
    'ix_diapers_baby_date',
    Diaper.baby_id,
    Diaper.changed_at.desc(),
    postgresql_where=(Diaper.deleted_at.is_(None))
)

# Index pour les changements nécessitant attention
Index(
    'ix_diapers_needs_attention',
    Diaper.baby_id,
    Diaper.rash_detected,
    postgresql_where=(Diaper.rash_detected == True)
)

