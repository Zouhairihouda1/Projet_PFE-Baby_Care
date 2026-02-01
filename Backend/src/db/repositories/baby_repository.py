"""
Baby Repository
Pattern Repository pour l'accès aux données des bébés
Centralise toutes les requêtes SQL
"""

from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, func
from typing import List, Optional
from datetime import datetime

from app.db.models.baby_model import Baby, GenderEnum


class BabyRepository:
    """
    Repository pour gérer les opérations CRUD sur les bébés
    Centralise toute la logique d'accès aux données
    """
    
    def __init__(self, db: Session):
        """
        Initialise le repository avec une session de base de données
        
        Args:
            db: Session SQLAlchemy
        """
        self.db = db
    
    # ==================== CREATE ====================
    
    def create(self, user_id: int, name: str, birth_date, gender: GenderEnum, 
               photo_url: Optional[str] = None) -> Baby:
        """
        Crée un nouveau profil bébé
        
        Args:
            user_id: ID du parent propriétaire
            name: Prénom du bébé
            birth_date: Date de naissance
            gender: Genre du bébé
            photo_url: URL de la photo (optionnel)
        
        Returns:
            Baby: Instance du bébé créé
        """
        baby = Baby(
            user_id=user_id,
            name=name,
            birth_date=birth_date,
            gender=gender,
            photo_url=photo_url
        )
        
        self.db.add(baby)
        self.db.commit()
        self.db.refresh(baby)
        
        return baby
    
    # ==================== READ ====================
    
    def get_by_id(self, baby_id: int, user_id: Optional[int] = None, 
                  include_deleted: bool = False) -> Optional[Baby]:
        """
        Récupère un bébé par son ID
        
        Args:
            baby_id: ID du bébé
            user_id: ID de l'utilisateur (pour vérifier ownership)
            include_deleted: Inclure les profils supprimés
        
        Returns:
            Baby ou None si non trouvé
        """
        query = self.db.query(Baby).filter(Baby.id == baby_id)
        
        # Vérifier ownership si user_id fourni
        if user_id is not None:
            query = query.filter(Baby.user_id == user_id)
        
        # Exclure les supprimés par défaut
        if not include_deleted:
            query = query.filter(Baby.deleted_at.is_(None))
        
        return query.first()
    
    def get_all_by_user(self, user_id: int, skip: int = 0, limit: int = 100,
                        include_deleted: bool = False) -> List[Baby]:
        """
        Récupère tous les bébés d'un utilisateur
        
        Args:
            user_id: ID de l'utilisateur
            skip: Nombre d'éléments à sauter (pagination)
            limit: Nombre maximum d'éléments à retourner
            include_deleted: Inclure les profils supprimés
        
        Returns:
            Liste des bébés
        """
        query = self.db.query(Baby).filter(Baby.user_id == user_id)
        
        # Exclure les supprimés par défaut
        if not include_deleted:
            query = query.filter(Baby.deleted_at.is_(None))
        
        # Trier par date de création (plus récent d'abord)
        query = query.order_by(Baby.created_at.desc())
        
        # Pagination
        return query.offset(skip).limit(limit).all()
    
    def count_by_user(self, user_id: int, include_deleted: bool = False) -> int:
        """
        Compte le nombre de bébés d'un utilisateur
        
        Args:
            user_id: ID de l'utilisateur
            include_deleted: Inclure les profils supprimés
        
        Returns:
            Nombre de bébés
        """
        query = self.db.query(func.count(Baby.id)).filter(Baby.user_id == user_id)
        
        if not include_deleted:
            query = query.filter(Baby.deleted_at.is_(None))
        
        return query.scalar()
    
    def search_by_name(self, user_id: int, name_query: str, 
                       skip: int = 0, limit: int = 100) -> List[Baby]:
        """
        Recherche des bébés par nom (recherche partielle, insensible à la casse)
        
        Args:
            user_id: ID de l'utilisateur
            name_query: Terme de recherche
            skip: Pagination
            limit: Limite
        
        Returns:
            Liste des bébés correspondants
        """
        return self.db.query(Baby).filter(
            and_(
                Baby.user_id == user_id,
                Baby.name.ilike(f"%{name_query}%"),
                Baby.deleted_at.is_(None)
            )
        ).order_by(Baby.name.asc()).offset(skip).limit(limit).all()
    
    def get_by_birth_date_range(self, user_id: int, start_date, end_date) -> List[Baby]:
        """
        Récupère les bébés nés dans une plage de dates
        
        Args:
            user_id: ID de l'utilisateur
            start_date: Date de début
            end_date: Date de fin
        
        Returns:
            Liste des bébés
        """
        return self.db.query(Baby).filter(
            and_(
                Baby.user_id == user_id,
                Baby.birth_date >= start_date,
                Baby.birth_date <= end_date,
                Baby.deleted_at.is_(None)
            )
        ).order_by(Baby.birth_date.desc()).all()
    
    def exists(self, baby_id: int, user_id: Optional[int] = None) -> bool:
        """
        Vérifie si un bébé existe
        
        Args:
            baby_id: ID du bébé
            user_id: ID de l'utilisateur (optionnel)
        
        Returns:
            True si existe, False sinon
        """
        query = self.db.query(Baby.id).filter(
            and_(
                Baby.id == baby_id,
                Baby.deleted_at.is_(None)
            )
        )
        
        if user_id is not None:
            query = query.filter(Baby.user_id == user_id)
        
        return self.db.query(query.exists()).scalar()
    
    # ==================== UPDATE ====================
    
    def update(self, baby_id: int, user_id: int, **update_data) -> Optional[Baby]:
        """
        Met à jour un profil bébé
        
        Args:
            baby_id: ID du bébé
            user_id: ID de l'utilisateur (vérification ownership)
            **update_data: Champs à mettre à jour
        
        Returns:
            Baby mis à jour ou None si non trouvé
        """
        baby = self.get_by_id(baby_id, user_id)
        
        if not baby:
            return None
        
        # Mettre à jour seulement les champs fournis
        for field, value in update_data.items():
            if hasattr(baby, field) and value is not None:
                setattr(baby, field, value)
        
        # updated_at sera automatiquement mis à jour par SQLAlchemy
        self.db.commit()
        self.db.refresh(baby)
        
        return baby
    
    def update_photo(self, baby_id: int, user_id: int, photo_url: str) -> Optional[Baby]:
        """
        Met à jour uniquement la photo du profil
        
        Args:
            baby_id: ID du bébé
            user_id: ID de l'utilisateur
            photo_url: Nouvelle URL de la photo
        
        Returns:
            Baby mis à jour ou None
        """
        return self.update(baby_id, user_id, photo_url=photo_url)
    
    # ==================== DELETE ====================
    
    def soft_delete(self, baby_id: int, user_id: int) -> bool:
        """
        Supprime logiquement un profil (soft delete)
        
        Args:
            baby_id: ID du bébé
            user_id: ID de l'utilisateur
        
        Returns:
            True si supprimé, False si non trouvé
        """
        baby = self.get_by_id(baby_id, user_id)
        
        if not baby:
            return False
        
        baby.soft_delete()
        self.db.commit()
        
        return True
    
    def hard_delete(self, baby_id: int, user_id: int) -> bool:
        """
        Supprime définitivement un profil de la base de données
        ATTENTION: Suppression cascade de toutes les données liées
        
        Args:
            baby_id: ID du bébé
            user_id: ID de l'utilisateur
        
        Returns:
            True si supprimé, False si non trouvé
        """
        baby = self.get_by_id(baby_id, user_id, include_deleted=True)
        
        if not baby:
            return False
        
        self.db.delete(baby)
        self.db.commit()
        
        return True
    
    def restore(self, baby_id: int, user_id: int) -> Optional[Baby]:
        """
        Restaure un profil supprimé (annule le soft delete)
        
        Args:
            baby_id: ID du bébé
            user_id: ID de l'utilisateur
        
        Returns:
            Baby restauré ou None
        """
        baby = self.get_by_id(baby_id, user_id, include_deleted=True)
        
        if not baby or not baby.is_deleted():
            return None
        
        baby.restore()
        self.db.commit()
        self.db.refresh(baby)
        
        return baby
    
    # ==================== STATISTIQUES ====================
    
    def get_statistics_by_user(self, user_id: int) -> dict:
        """
        Récupère des statistiques sur les bébés d'un utilisateur
        
        Args:
            user_id: ID de l'utilisateur
        
        Returns:
            dict avec statistiques
        """
        total = self.count_by_user(user_id)
        
        # Compte par genre
        gender_counts = self.db.query(
            Baby.gender,
            func.count(Baby.id)
        ).filter(
            and_(
                Baby.user_id == user_id,
                Baby.deleted_at.is_(None)
            )
        ).group_by(Baby.gender).all()
        
        gender_stats = {gender.value: count for gender, count in gender_counts}
        
        # Bébé le plus jeune et le plus âgé
        babies = self.get_all_by_user(user_id)
        
        youngest = None
        oldest = None
        
        if babies:
            youngest = max(babies, key=lambda b: b.birth_date)
            oldest = min(babies, key=lambda b: b.birth_date)
        
        return {
            "total": total,
            "by_gender": gender_stats,
            "youngest": {
                "id": youngest.id,
                "name": youngest.name,
                "age": youngest.calculate_age()
            } if youngest else None,
            "oldest": {
                "id": oldest.id,
                "name": oldest.name,
                "age": oldest.calculate_age()
            } if oldest else None
        }
    
    # ==================== BATCH OPERATIONS ====================
    
    def bulk_soft_delete(self, baby_ids: List[int], user_id: int) -> int:
        """
        Supprime plusieurs profils en une seule fois (soft delete)
        
        Args:
            baby_ids: Liste des IDs à supprimer
            user_id: ID de l'utilisateur
        
        Returns:
            Nombre de profils supprimés
        """
        count = self.db.query(Baby).filter(
            and_(
                Baby.id.in_(baby_ids),
                Baby.user_id == user_id,
                Baby.deleted_at.is_(None)
            )
        ).update(
            {"deleted_at": datetime.utcnow()},
            synchronize_session=False
        )
        
        self.db.commit()
        
        return count
    
    def __repr__(self) -> str:
        return f"<BabyRepository(session={self.db})>"
