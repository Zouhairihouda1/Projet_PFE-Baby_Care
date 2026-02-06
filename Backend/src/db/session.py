from sqlalchemy.orm import sessionmaker
from db.base import engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_session():
    """Dependency to get DB session (alternative to get_db in base.py)"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
