from sqlalchemy import Column, Integer, String, DateTime, Enum, Boolean, ForeignKey, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from . import Base
import enum

class NotificationType(enum.Enum):
    VACCINE_REMINDER = "vaccine_reminder"
    FEEDING_REMINDER = "feeding_reminder"
    SLEEP_REMINDER = "sleep_reminder"
    MEDICAL_REMINDER = "medical_reminder"
    SYSTEM = "system"
    ADVICE = "advice"

class NotificationStatus(enum.Enum):
    PENDING = "pending"
    SENT = "sent"
    READ = "read"
    FAILED = "failed"

class Notification(Base):
    __tablename__ = 'notifications'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    baby_id = Column(Integer, ForeignKey('babies.id'), nullable=True)
    type = Column(Enum(NotificationType), nullable=False)
    title = Column(String(200), nullable=False)
    message = Column(String(500), nullable=False)
    scheduled_time = Column(DateTime(timezone=True), nullable=False)
    sent_time = Column(DateTime(timezone=True), nullable=True)
    status = Column(Enum(NotificationStatus), default=NotificationStatus.PENDING)
    is_recurring = Column(Boolean, default=False)
    recurrence_pattern = Column(String(100), nullable=True)  # "daily", "weekly", etc.
    metadata = Column(JSON, nullable=True)  # Données supplémentaires
    
    # Relations
    user = relationship("User", back_populates="notifications")
    
    def __repr__(self):
        return f"<Notification {self.type} for {self.user_id}>"
