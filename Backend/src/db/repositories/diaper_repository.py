"""
Diaper Repository
Pattern Repository pour l'accès aux données des changements de couches
Centralise toutes les requêtes SQL
"""

from sqlalchemy.orm import Session
from sqlalchemy import and_, func, case, desc
from typing import List, Optional
from datetime import datetime, date, timedelta

from app.db.models.diaper_model import Diaper, DiaperType


class DiaperRepository:
    """
    Repository pour gérer les opérations CRUD sur les changements de couches
    """
    
    def __init__(self, db: Session):
        """
        Initialise le repository avec une session de base de données
        
        Args:
            db: Session SQLAlchemy
        """
        self.db = db
    
    # ==================== CREATE ====================
    
    def create(
        self,
        baby_id: int,
        changed_at: datetime,
        diaper_type: DiaperType,
        notes: Optional[str] = None,
        rash_detected: bool = False,
        cream_applied: bool = False
    ) -> Diaper:
        """
        Enregistre un nouveau changement de couche
        
        Args:
            baby_id: ID du bébé
            changed_at: Date/heure du changement
            diaper_type: Type de couche
            notes: Remarques optionnelles
            rash_detected: Érythème détecté ?
            cream_applied: Crème appliquée ?
        
        Returns:
            Diaper: Instance créée
        """
        diaper = Diaper(
            baby_id=baby_id,
            changed_at=changed_at,
            diaper_type=diaper_type,
            notes=notes,
            rash_detected=rash_detected,
            cream_applied=cream_applied
        )
        
        self.db.add(diaper)
        self.db.commit()
        self.db.refresh(diaper)
        
        return diaper
    
    # ==================== READ ====================
    
    def get_by_id(
        self,
        diaper_id: int,
        baby_id: Optional[int] = None,
        include_deleted: bool = False
    ) -> Optional[Diaper]:
        """
        Récupère un changement par ID
        
        Args:
            diaper_id: ID du changement
            baby_id: ID du bébé (vérification ownership)
            include_deleted: Inclure les supprimés
        
        Returns:
            Diaper ou None
        """
        query = self.db.query(Diaper).filter(Diaper.id == diaper_id)
        
        if baby_id is not None:
            query = query.filter(Diaper.baby_id == baby_id)
        
        if not include_deleted:
            query = query.filter(Diaper.deleted_at.is_(None))
        
        return query.first()
    
    def get_all_by_baby(
        self,
        baby_id: int,
        skip: int = 0,
        limit: int = 100,
        include_deleted: bool = False
    ) -> List[Diaper]:
        """
        Récupère tous les changements d'un bébé
        
        Args:
            baby_id: ID du bébé
            skip: Pagination
            limit: Limite
            include_deleted: Inclure supprimés
        
        Returns:
            Liste des changements
        """
        query = self.db.query(Diaper).filter(Diaper.baby_id == baby_id)
        
        if not include_deleted:
            query = query.filter(Diaper.deleted_at.is_(None))
        
        # Trier par date décroissante (plus récent d'abord)
        query = query.order_by(Diaper.changed_at.desc())
        
        return query.offset(skip).limit(limit).all()
    
    def count_by_baby(
        self,
        baby_id: int,
        include_deleted: bool = False
    ) -> int:
        """
        Compte le nombre de changements pour un bébé
        
        Args:
            baby_id: ID du bébé
            include_deleted: Inclure supprimés
        
        Returns:
            Nombre de changements
        """
        query = self.db.query(func.count(Diaper.id)).filter(
            Diaper.baby_id == baby_id
        )
        
        if not include_deleted:
            query = query.filter(Diaper.deleted_at.is_(None))
        
        return query.scalar()
    
    def get_by_date_range(
        self,
        baby_id: int,
        start_date: datetime,
        end_date: datetime
    ) -> List[Diaper]:
        """
        Récupère les changements dans une plage de dates
        
        Args:
            baby_id: ID du bébé
            start_date: Date de début
            end_date: Date de fin
        
        Returns:
            Liste des changements
        """
        return self.db.query(Diaper).filter(
            and_(
                Diaper.baby_id == baby_id,
                Diaper.changed_at >= start_date,
                Diaper.changed_at <= end_date,
                Diaper.deleted_at.is_(None)
            )
        ).order_by(Diaper.changed_at.desc()).all()
    
    def get_today(self, baby_id: int) -> List[Diaper]:
        """
        Récupère les changements d'aujourd'hui
        
        Args:
            baby_id: ID du bébé
        
        Returns:
            Liste des changements du jour
        """
        today_start = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = datetime.now().replace(hour=23, minute=59, second=59, microsecond=999999)
        
        return self.get_by_date_range(baby_id, today_start, today_end)
    
    def get_last_change(self, baby_id: int) -> Optional[Diaper]:
        """
        Récupère le dernier changement de couche
        
        Args:
            baby_id: ID du bébé
        
        Returns:
            Dernier changement ou None
        """
        return self.db.query(Diaper).filter(
            and_(
                Diaper.baby_id == baby_id,
                Diaper.deleted_at.is_(None)
            )
        ).order_by(Diaper.changed_at.desc()).first()
    
    def get_changes_with_rash(self, baby_id: int, days: int = 7) -> List[Diaper]:
        """
        Récupère les changements avec érythème détecté
        
        Args:
            baby_id: ID du bébé
            days: Nombre de jours à consulter
        
        Returns:
            Liste des changements avec rash
        """
        cutoff_date = datetime.now() - timedelta(days=days)
        
        return self.db.query(Diaper).filter(
            and_(
                Diaper.baby_id == baby_id,
                Diaper.rash_detected == True,
                Diaper.changed_at >= cutoff_date,
                Diaper.deleted_at.is_(None)
            )
        ).order_by(Diaper.changed_at.desc()).all()
    
    def exists(self, diaper_id: int, baby_id: Optional[int] = None) -> bool:
        """
        Vérifie si un changement existe
        
        Args:
            diaper_id: ID du changement
            baby_id: ID du bébé (optionnel)
        
        Returns:
            True si existe
        """
        query = self.db.query(Diaper.id).filter(
            and_(
                Diaper.id == diaper_id,
                Diaper.deleted_at.is_(None)
            )
        )
        
        if baby_id is not None:
            query = query.filter(Diaper.baby_id == baby_id)
        
        return self.db.query(query.exists()).scalar()
    
    # ==================== UPDATE ====================
    
    def update(
        self,
        diaper_id: int,
        baby_id: int,
        **update_data
    ) -> Optional[Diaper]:
        """
        Met à jour un changement de couche
        
        Args:
            diaper_id: ID du changement
            baby_id: ID du bébé (vérification ownership)
            **update_data: Champs à mettre à jour
        
        Returns:
            Diaper mis à jour ou None
        """
        diaper = self.get_by_id(diaper_id, baby_id)
        
        if not diaper:
            return None
        
        for field, value in update_data.items():
            if hasattr(diaper, field) and value is not None:
                setattr(diaper, field, value)
        
        self.db.commit()
        self.db.refresh(diaper)
        
        return diaper
    
    # ==================== DELETE ====================
    
    def soft_delete(self, diaper_id: int, baby_id: int) -> bool:
        """
        Suppression logique d'un changement
        
        Args:
            diaper_id: ID du changement
            baby_id: ID du bébé
        
        Returns:
            True si supprimé
        """
        diaper = self.get_by_id(diaper_id, baby_id)
        
        if not diaper:
            return False
        
        diaper.soft_delete()
        self.db.commit()
        
        return True
    
    def hard_delete(self, diaper_id: int, baby_id: int) -> bool:
        """
        Suppression définitive d'un changement
        
        Args:
            diaper_id: ID du changement
            baby_id: ID du bébé
        
        Returns:
            True si supprimé
        """
        diaper = self.get_by_id(diaper_id, baby_id, include_deleted=True)
        
        if not diaper:
            return False
        
        self.db.delete(diaper)
        self.db.commit()
        
        return True
    
    def restore(self, diaper_id: int, baby_id: int) -> Optional[Diaper]:
        """
        Restaure un changement supprimé
        
        Args:
            diaper_id: ID du changement
            baby_id: ID du bébé
        
        Returns:
            Diaper restauré ou None
        """
        diaper = self.get_by_id(diaper_id, baby_id, include_deleted=True)
        
        if not diaper or not diaper.is_deleted():
            return None
        
        diaper.restore()
        self.db.commit()
        self.db.refresh(diaper)
        
        return diaper
    
    # ==================== STATISTIQUES ====================
    
    def get_statistics(self, baby_id: int, days: int = 30) -> dict:
        """
        Récupère les statistiques des changements de couches
        
        Args:
            baby_id: ID du bébé
            days: Période en jours
        
        Returns:
            Dictionnaire de statistiques
        """
        cutoff_date = datetime.now() - timedelta(days=days)
        
        # Total de changements
        total = self.count_by_baby(baby_id)
        
        # Changements aujourd'hui
        today = self.get_today(baby_id)
        changes_today = len(today)
        
        # Dernier changement
        last_change = self.get_last_change(baby_id)
        
        # Comptage par type
        type_counts = self.db.query(
            Diaper.diaper_type,
            func.count(Diaper.id)
        ).filter(
            and_(
                Diaper.baby_id == baby_id,
                Diaper.changed_at >= cutoff_date,
                Diaper.deleted_at.is_(None)
            )
        ).group_by(Diaper.diaper_type).all()
        
        type_stats = {dtype.value: 0 for dtype in DiaperType}
        for dtype, count in type_counts:
            type_stats[dtype.value] = count
        
        # Nombre d'érythèmes détectés
        rash_count = self.db.query(func.count(Diaper.id)).filter(
            and_(
                Diaper.baby_id == baby_id,
                Diaper.rash_detected == True,
                Diaper.changed_at >= cutoff_date,
                Diaper.deleted_at.is_(None)
            )
        ).scalar()
        
        # Calcul intervalle moyen
        changes = self.get_by_date_range(
            baby_id,
            cutoff_date,
            datetime.now()
        )
        
        average_interval = None
        if len(changes) > 1:
            # Trier par date croissante pour calculer intervalles
            sorted_changes = sorted(changes, key=lambda x: x.changed_at)
            intervals = []
            
            for i in range(1, len(sorted_changes)):
                delta = sorted_changes[i].changed_at - sorted_changes[i-1].changed_at
                intervals.append(delta.total_seconds() / 60)  # en minutes
            
            if intervals:
                average_interval = int(sum(intervals) / len(intervals))
        
        return {
            "total_changes": total,
            "changes_today": changes_today,
            "last_change": last_change,
            "wet_count": type_stats.get("wet", 0),
            "dirty_count": type_stats.get("dirty", 0),
            "both_count": type_stats.get("both", 0),
            "clean_count": type_stats.get("clean", 0),
            "rash_detected_count": rash_count,
            "average_interval_minutes": average_interval
        }
    
    def get_daily_summary(
        self,
        baby_id: int,
        target_date: date
    ) -> dict:
        """
        Récupère le résumé journalier
        
        Args:
            baby_id: ID du bébé
            target_date: Date cible
        
        Returns:
            Résumé du jour
        """
        day_start = datetime.combine(target_date, datetime.min.time())
        day_end = datetime.combine(target_date, datetime.max.time())
        
        changes = self.get_by_date_range(baby_id, day_start, day_end)
        
        # Comptage par type
        wet = sum(1 for c in changes if c.is_wet())
        dirty = sum(1 for c in changes if c.is_dirty())
        both = sum(1 for c in changes if c.diaper_type == DiaperType.BOTH)
        
        # Érythème détecté ?
        rash = any(c.rash_detected for c in changes)
        
        return {
            "date": target_date.isoformat(),
            "total_changes": len(changes),
            "wet_count": wet,
            "dirty_count": dirty,
            "both_count": both,
            "rash_detected": rash
        }
    
    # ==================== BATCH OPERATIONS ====================
    
    def bulk_soft_delete(
        self,
        diaper_ids: List[int],
        baby_id: int
    ) -> int:
        """
        Supprime plusieurs changements en une fois
        
        Args:
            diaper_ids: Liste des IDs à supprimer
            baby_id: ID du bébé
        
        Returns:
            Nombre de changements supprimés
        """
        count = self.db.query(Diaper).filter(
            and_(
                Diaper.id.in_(diaper_ids),
                Diaper.baby_id == baby_id,
                Diaper.deleted_at.is_(None)
            )
        ).update(
            {"deleted_at": datetime.utcnow()},
            synchronize_session=False
        )
        
        self.db.commit()
        
        return count
    
    def __repr__(self) -> str:
        return f"<DiaperRepository(session={self.db})>"
