from pydantic_settings import BaseSettings
from typing import List, Optional

class Settings(BaseSettings):
    # API
    API_V1_STR: str = '/api/v1'
    PROJECT_NAME: str = 'BabyCare API'
    
    # Database
    DATABASE_URL: str = 'postgresql://user:password@localhost/babycare_db'
    
    # Security
    SECRET_KEY: str = 'your-secret-key-change-this-in-production'
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ['http://localhost:3000', 'http://localhost:8000']
    
    class Config:
        env_file = '.env'

settings = Settings()
