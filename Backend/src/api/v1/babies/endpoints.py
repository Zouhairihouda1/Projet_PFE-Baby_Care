"""
Baby Profile API Endpoints
Routes REST pour la gestion des profils bébé
"""

from fastapi import APIRouter, Depends, HTTPException, status, Query, Body, UploadFile, File
from sqlalchemy.orm import Session
from typing import List, Optional
import logging

from app.api.deps import get_db, get_current_user
from app.db.models.user_model import User
from app.core.services.baby_service import BabyService
from app.api.v1.babies.schemas import (
    BabyCreateSchema,
    BabyUpdateSchema,
    BabyResponseSchema,
    BabyListResponseSchema,
    PhotoUploadResponseSchema,
    ErrorResponseSchema
)


# Configuration
router = APIRouter()
logger = logging.getLogger(__name__)


# ==================== DEPENDENCIES ====================

def get_baby_service(db: Session = Depends(get_db)) -> BabyService:
    """Dependency injection pour le BabyService"""
    return BabyService(db)


# ==================== ENDPOINTS ====================

@router.post(
    "/",
    response_model=BabyResponseSchema,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new baby profile",
    description="Creates a new baby profile for the authenticated user",
    responses={
        201: {
            "description": "Baby profile created successfully",
            "model": BabyResponseSchema
        },
        400: {
            "description": "Invalid input data or limit exceeded",
            "model": ErrorResponseSchema
        },
        401: {
            "description": "Not authenticated",
            "model": ErrorResponseSchema
        },
        422: {
            "description": "Validation error",
            "model": ErrorResponseSchema
        }
    },
    tags=["Babies"]
)
def create_baby_profile(
    baby_data: BabyCreateSchema = Body(
        ...,
        example={
            "name": "Emma",
            "birth_date": "2025-12-01",
            "gender": "female",
            "photo_url": "https://example.com/photos/emma.jpg"
        }
    ),
    current_user: User = Depends(get_current_user),
    baby_service: BabyService = Depends(get_baby_service)
) -> BabyResponseSchema:
    """
    Create a new baby profile.
    
    **Required fields:**
    - **name**: Baby's first name (1-100 characters, letters only)
    - **birth_date**: Date of birth (format: YYYY-MM-DD, cannot be in future)
    - **gender**: One of: male, female, other
    
    **Optional fields:**
    - **photo_url**: URL to baby's photo (must be valid image URL)
    
    **Business rules:**
    - Maximum 10 baby profiles per user
    - Birth date cannot be more than 10 years ago
    - Name must contain only letters, spaces, hyphens, and apostrophes
    """
    logger.info(f"User {current_user.id} creating baby profile: {baby_data.name}")
    
    return baby_service.create_baby(current_user.id, baby_data)


@router.get(
    "/",
    response_model=BabyListResponseSchema,
    summary="Get all baby profiles",
    description="Retrieves all baby profiles for the authenticated user with pagination",
    responses={
        200: {
            "description": "List of baby profiles",
            "model": BabyListResponseSchema
        },
        401: {
            "description": "Not authenticated"
        }
    },
    tags=["Babies"]
)
def get_baby_profiles(
    skip: int = Query(
        0,
        ge=0,
        description="Number of items to skip (for pagination)"
    ),
    limit: int = Query(
        10,
        ge=1,
        le=100,
        description="Maximum number of items to return (1-100)"
    ),
    current_user: User = Depends(get_current_user),
    baby_service: BabyService = Depends(get_baby_service)
) -> BabyListResponseSchema:
    """
    Get all baby profiles for the current user.
    
    **Pagination:**
    - Use `skip` and `limit` parameters to paginate results
    - Default: skip=0, limit=10
    - Maximum limit: 100
    
    **Response includes:**
    - Total count of babies
    - Pagination info (skip, limit)
    - List of baby profiles with calculated age
    
    **Sorting:**
    - Results are sorted by creation date (newest first)
    """
    logger.debug(f"User {current_user.id} fetching baby profiles")
    
    total, babies = baby_service.get_user_babies(current_user.id, skip, limit)
    
    return BabyListResponseSchema(
        total=total,
        skip=skip,
        limit=limit,
        items=babies
    )


@router.get(
    "/search",
    response_model=List[BabyResponseSchema],
    summary="Search baby profiles by name",
    description="Search for baby profiles by name (case-insensitive partial match)",
    tags=["Babies"]
)
def search_babies(
    q: str = Query(
        ...,
        min_length=1,
        max_length=100,
        description="Search query (name)"
    ),
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    current_user: User = Depends(get_current_user),
    baby_service: BabyService = Depends(get_baby_service)
) -> List[BabyResponseSchema]:
    """
    Search for babies by name.
    
    **Search features:**
    - Case-insensitive
    - Partial match (e.g., "Em" matches "Emma")
    - Only searches current user's babies
    
    **Parameters:**
    - **q**: Search query (required)
    - **skip**, **limit**: Pagination
    """
    logger.debug(f"User {current_user.id} searching babies with query: {q}")
    
    return baby_service.search_babies(current_user.id, q, skip, limit)


@router.get(
    "/{baby_id}",
    response_model=BabyResponseSchema,
    summary="Get a specific baby profile",
    description="Retrieves detailed information about a specific baby profile",
    responses={
        200: {
            "description": "Baby profile details",
            "model": BabyResponseSchema
        },
        404: {
            "description": "Baby not found or access denied",
            "model": ErrorResponseSchema
        }
    },
    tags=["Babies"]
)
def get_baby_profile(
    baby_id: int,
    current_user: User = Depends(get_current_user),
    baby_service: BabyService = Depends(get_baby_service)
) -> BabyResponseSchema:
    """
    Get details of a specific baby profile.
    
    **Security:**
    - Only the profile owner can access it
    - Returns 404 if baby doesn't exist or user is not the owner
    
    **Response includes:**
    - All baby information
    - Calculated age (days, weeks, months, years)
    - Creation and update timestamps
    """
    logger.debug(f"User {current_user.id} fetching baby {baby_id}")
    
    return baby_service.get_baby_by_id(baby_id, current_user.id)


@router.put(
    "/{baby_id}",
    response_model=BabyResponseSchema,
    summary="Update a baby profile",
    description="Updates one or more fields of a baby profile (partial update)",
    responses={
        200: {
            "description": "Baby profile updated successfully",
            "model": BabyResponseSchema
        },
        400: {
            "description": "Invalid input or no fields provided"
        },
        404: {
            "description": "Baby not found or access denied"
        }
    },
    tags=["Babies"]
)
def update_baby_profile(
    baby_id: int,
    update_data: BabyUpdateSchema = Body(
        ...,
        example={
            "name": "Emma Rose"
        }
    ),
    current_user: User = Depends(get_current_user),
    baby_service: BabyService = Depends(get_baby_service)
) -> BabyResponseSchema:
    """
    Update a baby profile (partial update).
    
    **Updatable fields:**
    - name
    - birth_date
    - gender
    - photo_url
    
    **Rules:**
    - At least one field must be provided
    - All fields are optional (partial update)
    - Same validation rules as creation apply
    - Only the owner can update the profile
    
    **Example - Update only name:**
    ```json
    {
        "name": "Emma Rose"
    }
    ```
    """
    logger.info(f"User {current_user.id} updating baby {baby_id}")
    
    return baby_service.update_baby(baby_id, current_user.id, update_data)


@router.patch(
    "/{baby_id}",
    response_model=BabyResponseSchema,
    summary="Partial update (alias for PUT)",
    description="Same as PUT - updates one or more fields",
    include_in_schema=False,  # Masquer dans Swagger (doublon avec PUT)
    tags=["Babies"]
)
def patch_baby_profile(
    baby_id: int,
    update_data: BabyUpdateSchema,
    current_user: User = Depends(get_current_user),
    baby_service: BabyService = Depends(get_baby_service)
) -> BabyResponseSchema:
    """Alias pour PUT (PATCH et PUT ont le même comportement)"""
    return baby_service.update_baby(baby_id, current_user.id, update_data)


@router.delete(
    "/{baby_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a baby profile",
    description="Soft-deletes a baby profile (can be restored later)",
    responses={
        204: {
            "description": "Baby profile deleted successfully"
        },
        404: {
            "description": "Baby not found or already deleted"
        }
    },
    tags=["Babies"]
)
def delete_baby_profile(
    baby_id: int,
    permanent: bool = Query(
        False,
        description="If True, permanently delete (cannot be restored)"
    ),
    current_user: User = Depends(get_current_user),
    baby_service: BabyService = Depends(get_baby_service)
):
    """
    Delete a baby profile.
    
    **Deletion modes:**
    
    **Soft delete (default):**
    - Profile is marked as deleted but remains in database
    - Can be restored later with POST /babies/{baby_id}/restore
    - All related data is preserved
    
    **Permanent delete (permanent=true):**
    - Profile is completely removed from database
    - **WARNING**: This action cannot be undone
    - All related data (vaccinations, feedings, etc.) is also deleted (CASCADE)
    
    **Security:**
    - Only the owner can delete the profile
    
    **Parameters:**
    - **permanent**: Set to `true` for permanent deletion (default: false)
    """
    logger.info(
        f"User {current_user.id} deleting baby {baby_id} "
        f"(permanent={permanent})"
    )
    
    baby_service.delete_baby(baby_id, current_user.id, hard_delete=permanent)
    
    return None  # 204 No Content


@router.post(
    "/{baby_id}/restore",
    response_model=BabyResponseSchema,
    summary="Restore a deleted baby profile",
    description="Restores a soft-deleted baby profile",
    responses={
        200: {
            "description": "Baby profile restored successfully"
        },
        404: {
            "description": "Baby not found or not deleted"
        }
    },
    tags=["Babies"]
)
def restore_baby_profile(
    baby_id: int,
    current_user: User = Depends(get_current_user),
    baby_service: BabyService = Depends(get_baby_service)
) -> BabyResponseSchema:
    """
    Restore a soft-deleted baby profile.
    
    **Requirements:**
    - Profile must have been soft-deleted (not permanently deleted)
    - Only the owner can restore the profile
    
    **Effect:**
    - Profile becomes active again
    - All related data is accessible
    """
    logger.info(f"User {current_user.id} restoring baby {baby_id}")
    
    return baby_service.restore_baby(baby_id, current_user.id)


@router.post(
    "/{baby_id}/photo",
    response_model=PhotoUploadResponseSchema,
    summary="Upload baby photo",
    description="Uploads a photo for the baby profile",
    responses={
        200: {
            "description": "Photo uploaded successfully"
        },
        400: {
            "description": "Invalid file type or size"
        },
        404: {
            "description": "Baby not found"
        }
    },
    tags=["Babies"]
)
async def upload_baby_photo(
    baby_id: int,
    file: UploadFile = File(..., description="Image file (JPEG, PNG, WebP, max 5MB)"),
    current_user: User = Depends(get_current_user),
    baby_service: BabyService = Depends(get_baby_service)
) -> PhotoUploadResponseSchema:
    """
    Upload a photo for the baby profile.
    
    **Supported formats:**
    - JPEG (.jpg, .jpeg)
    - PNG (.png)
    - WebP (.webp)
    
    **Limitations:**
    - Maximum file size: 5 MB
    
    **Process:**
    1. File is validated
    2. File is saved to server storage
    3. Baby profile is updated with photo URL
    
    **Note:** This is a placeholder. Actual implementation needs file storage setup.
    """
    # TODO: Implémenter upload réel de fichier
    # Pour l'instant, retourne un exemple
    
    logger.info(f"User {current_user.id} uploading photo for baby {baby_id}")
    
    # Vérifier que le bébé existe et appartient à l'utilisateur
    baby_service.get_baby_by_id(baby_id, current_user.id)
    
    # Validation basique
    if file.content_type not in ["image/jpeg", "image/png", "image/webp"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file type. Accepted: JPEG, PNG, WebP"
        )
    
    # TODO: Implémenter la logique de sauvegarde du fichier
    # Pour l'instant, retourne un exemple
    
    return PhotoUploadResponseSchema(
        photo_url=f"/uploads/babies/{baby_id}/{file.filename}",
        message="Photo upload feature is not yet implemented"
    )


@router.get(
    "/statistics/overview",
    summary="Get user baby statistics",
    description="Retrieves statistics about all user's babies",
    tags=["Babies", "Statistics"]
)
def get_baby_statistics(
    current_user: User = Depends(get_current_user),
    baby_service: BabyService = Depends(get_baby_service)
) -> dict:
    """
    Get statistics about user's babies.
    
    **Includes:**
    - Total number of babies
    - Count by gender
    - Information about youngest baby
    - Information about oldest baby
    """
    logger.debug(f"User {current_user.id} fetching baby statistics")
    
    return baby_service.get_user_statistics(current_user.id)
