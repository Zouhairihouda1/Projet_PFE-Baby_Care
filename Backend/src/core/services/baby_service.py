"""
Baby Service
Couche de logique métier pour la gestion des profils bébé
Orchestre les repositories et applique les règles business
"""

from sqlalchemy.orm import Session
from typing import List, Optional, Tuple
from datetime import date
import logging

from app.db.repositories.baby_repository import BabyRepository
from app.db.models.baby_model import Baby, GenderEnum
from app.api.v1.babies.schemas import (
    BabyCreateSchema, 
    BabyUpdateSchema,
    BabyResponseSchema,
    AgeInfoSchema
)
from fastapi import HTTPException, status


# Configuration du logger
logger = logging.getLogger(__name__)


class BabyService:
    """
    Service de gestion des profils bébé
    Contient toute la logique métier
    """
    
    def __init__(self, db: Session):
        """
        Initialise le service avec une session de base de données
        
        Args:
            db: Session SQLAlchemy
        """
        self.db = db
        self.repository = BabyRepository(db)
    
    # ==================== CREATION ====================
    
    def create_baby(self, user_id: int, baby_data: BabyCreateSchema) -> BabyResponseSchema:
        """
        Crée un nouveau profil bébé avec validation métier
        
        Args:
            user_id: ID du parent
            baby_data: Données du bébé validées par Pydantic
        
        Returns:
            BabyResponseSchema: Profil créé
        
        Raises:
            HTTPException: Si erreur de création
        """
        try:
            logger.info(f"Creating baby profile for user {user_id}")
            
            # Vérifier la limite de bébés par utilisateur (règle métier)
            baby_count = self.repository.count_by_user(user_id)
            MAX_BABIES_PER_USER = 10  # Limite raisonnable
            
            if baby_count >= MAX_BABIES_PER_USER:
                logger.warning(
                    f"User {user_id} exceeded maximum babies limit ({MAX_BABIES_PER_USER})"
                )
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Maximum number of baby profiles reached ({MAX_BABIES_PER_USER})"
                )
            
            # Créer le profil
            baby = self.repository.create(
                user_id=user_id,
                name=baby_data.name,
                birth_date=baby_data.birth_date,
                gender=baby_data.gender,
                photo_url=baby_data.photo_url
            )
            
            logger.info(f"Baby profile created successfully: ID={baby.id}, Name={baby.name}")
            
            # Retourner le schema de réponse
            return self._baby_to_response_schema(baby)
            
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error creating baby profile for user {user_id}: {str(e)}")
            self.db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to create baby profile"
            )
    
    # ==================== LECTURE ====================
    
    def get_baby_by_id(self, baby_id: int, user_id: int) -> BabyResponseSchema:
        """
        Récupère un profil bébé par ID
        
        Args:
            baby_id: ID du bébé
            user_id: ID de l'utilisateur (vérification ownership)
        
        Returns:
            BabyResponseSchema: Profil du bébé
        
        Raises:
            HTTPException 404: Si bébé non trouvé ou pas propriétaire
        """
        logger.debug(f"Fetching baby {baby_id} for user {user_id}")
        
        baby = self.repository.get_by_id(baby_id, user_id)
        
        if not baby:
            logger.warning(
                f"Baby {baby_id} not found or user {user_id} is not the owner"
            )
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Baby profile not found or access denied"
            )
        
        return self._baby_to_response_schema(baby)
    
    def get_user_babies(
        self, 
        user_id: int, 
        skip: int = 0, 
        limit: int = 10
    ) -> Tuple[int, List[BabyResponseSchema]]:
        """
        Récupère tous les bébés d'un utilisateur avec pagination
        
        Args:
            user_id: ID de l'utilisateur
            skip: Nombre d'éléments à sauter
            limit: Nombre maximum d'éléments
        
        Returns:
            Tuple (total, liste_bébés)
        """
        logger.debug(f"Fetching babies for user {user_id} (skip={skip}, limit={limit})")
        
        # Compter le total
        total = self.repository.count_by_user(user_id)
        
        # Récupérer les bébés
        babies = self.repository.get_all_by_user(user_id, skip, limit)
        
        # Convertir en schemas de réponse
        babies_response = [
            self._baby_to_response_schema(baby) for baby in babies
        ]
        
        logger.debug(f"Found {len(babies)} babies for user {user_id}")
        
        return total, babies_response
    
    def search_babies(
        self, 
        user_id: int, 
        name_query: str,
        skip: int = 0,
        limit: int = 10
    ) -> List[BabyResponseSchema]:
        """
        Recherche des bébés par nom
        
        Args:
            user_id: ID de l'utilisateur
            name_query: Terme de recherche
            skip: Pagination
            limit: Limite
        
        Returns:
            Liste des bébés correspondants
        """
        logger.debug(f"Searching babies for user {user_id} with query '{name_query}'")
        
        babies = self.repository.search_by_name(user_id, name_query, skip, limit)
        
        return [self._baby_to_response_schema(baby) for baby in babies]
    
    # ==================== MISE A JOUR ====================
    
    def update_baby(
        self, 
        baby_id: int, 
        user_id: int, 
        update_data: BabyUpdateSchema
    ) -> BabyResponseSchema:
        """
        Met à jour un profil bébé
        
        Args:
            baby_id: ID du bébé
            user_id: ID de l'utilisateur
            update_data: Données à mettre à jour
        
        Returns:
            BabyResponseSchema: Profil mis à jour
        
        Raises:
            HTTPException 404: Si bébé non trouvé
        """
        logger.info(f"Updating baby {baby_id} for user {user_id}")
        
        # Vérifier que le bébé existe et appartient à l'utilisateur
        existing_baby = self.repository.get_by_id(baby_id, user_id)
        if not existing_baby:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Baby profile not found or access denied"
            )
        
        try:
            # Préparer les données à mettre à jour (exclure None)
            update_dict = update_data.dict(exclude_unset=True, exclude_none=True)
            
            if not update_dict:
                logger.warning(f"No fields to update for baby {baby_id}")
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="No fields provided for update"
                )
            
            # Mettre à jour
            updated_baby = self.repository.update(baby_id, user_id, **update_dict)
            
            if not updated_baby:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Failed to update baby profile"
                )
            
            logger.info(f"Baby {baby_id} updated successfully")
            
            return self._baby_to_response_schema(updated_baby)
            
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error updating baby {baby_id}: {str(e)}")
            self.db.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to update baby profile"
            )
    
    def update_baby_photo(
        self, 
        baby_id: int, 
        user_id: int, 
        photo_url: str
    ) -> BabyResponseSchema:
        """
        Met à jour uniquement la photo du profil
        
        Args:
            baby_id: ID du bébé
            user_id: ID de l'utilisateur
            photo_url: Nouvelle URL de la photo
        
        Returns:
            BabyResponseSchema: Profil mis à jour
        """
        logger.info(f"Updating photo for baby {baby_id}")
        
        updated_baby = self.repository.update_photo(baby_id, user_id, photo_url)
        
        if not updated_baby:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Baby profile not found"
            )
        
        return self._baby_to_response_schema(updated_baby)
    
    # ==================== SUPPRESSION ====================
    
    def delete_baby(self, baby_id: int, user_id: int, hard_delete: bool = False) -> bool:
        """
        Supprime un profil bébé (soft ou hard delete)
        
        Args:
            baby_id: ID du bébé
            user_id: ID de l'utilisateur
            hard_delete: True pour suppression définitive, False pour soft delete
        
        Returns:
            bool: True si supprimé avec succès
        
        Raises:
            HTTPException 404: Si bébé non trouvé
        """
        logger.info(
            f"Deleting baby {baby_id} for user {user_id} "
            f"(hard_delete={hard_delete})"
        )
        
        if hard_delete:
            success = self.repository.hard_delete(baby_id, user_id)
        else:
            success = self.repository.soft_delete(baby_id, user_id)
        
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Baby profile not found or already deleted"
            )
        
        logger.info(f"Baby {baby_id} deleted successfully")
        
        return True
    
    def restore_baby(self, baby_id: int, user_id: int) -> BabyResponseSchema:
        """
        Restaure un profil supprimé
        
        Args:
            baby_id: ID du bébé
            user_id: ID de l'utilisateur
        
        Returns:
            BabyResponseSchema: Profil restauré
        """
        logger.info(f"Restoring baby {baby_id} for user {user_id}")
        
        restored_baby = self.repository.restore(baby_id, user_id)
        
        if not restored_baby:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Baby profile not found or not deleted"
            )
        
        logger.info(f"Baby {baby_id} restored successfully")
        
        return self._baby_to_response_schema(restored_baby)
    
    # ==================== STATISTIQUES ====================
    
    def get_user_statistics(self, user_id: int) -> dict:
        """
        Récupère les statistiques des bébés d'un utilisateur
        
        Args:
            user_id: ID de l'utilisateur
        
        Returns:
            dict: Statistiques
        """
        logger.debug(f"Fetching statistics for user {user_id}")
        
        return self.repository.get_statistics_by_user(user_id)
    
    # ==================== HELPERS ====================
    
    def _baby_to_response_schema(self, baby: Baby) -> BabyResponseSchema:
        """
        Convertit un objet Baby en BabyResponseSchema
        
        Args:
            baby: Instance Baby
        
        Returns:
            BabyResponseSchema
        """
        age_info = baby.calculate_age()
        
        return BabyResponseSchema(
            id=baby.id,
            user_id=baby.user_id,
            name=baby.name,
            birth_date=baby.birth_date,
            gender=baby.gender,
            photo_url=baby.photo_url,
            age=AgeInfoSchema(**age_info),
            created_at=baby.created_at,
            updated_at=baby.updated_at
        )
    
    def verify_ownership(self, baby_id: int, user_id: int) -> bool:
        """
        Vérifie qu'un utilisateur est propriétaire d'un profil bébé
        
        Args:
            baby_id: ID du bébé
            user_id: ID de l'utilisateur
        
        Returns:
            bool: True si propriétaire, False sinon
        """
        return self.repository.exists(baby_id, user_id)
    
    def __repr__(self) -> str:
        return f"<BabyService(session={self.db})>"
