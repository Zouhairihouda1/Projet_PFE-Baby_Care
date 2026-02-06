# User Service
from sqlalchemy.orm import Session
from typing import Optional
from db.models.user_model import UserModel
from core.models.user import UserCreate, UserInDB

class UserService:
    def __init__(self, db: Session):
        self.db = db
    
    def create_user(self, user_create: UserCreate) -> UserInDB:
        # À implémenter
        pass
    
    def get_user_by_email(self, email: str) -> Optional[UserInDB]:
        # À implémenter
        pass
