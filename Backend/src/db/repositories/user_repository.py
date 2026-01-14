from typing import Optional
from sqlalchemy.orm import Session
from db.models.user_model import UserModel
from db.repositories.base_repository import BaseRepository

class UserRepository(BaseRepository[UserModel]):
    def __init__(self, db: Session):
        super().__init__(UserModel, db)
    
    def get_by_email(self, email: str) -> Optional[UserModel]:
        return self.db.query(UserModel).filter(UserModel.email == email).first()
    
    def email_exists(self, email: str) -> bool:
        return self.db.query(UserModel).filter(UserModel.email == email).first() is not None
