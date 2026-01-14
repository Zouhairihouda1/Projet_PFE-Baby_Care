from fastapi import APIRouter

# Import des routes
from .auth.endpoints import router as auth_router
from .babies.endpoints import router as babies_router
from .health.endpoints import router as health_router
from .daily_log.endpoints import router as daily_log_router
from .notifications.endpoints import router as notifications_router
from .advice.endpoints import router as advice_router
from .users.endpoints import router as users_router

api_router = APIRouter()

# Inclure les routes
api_router.include_router(auth_router, prefix="/auth", tags=["authentication"])
api_router.include_router(babies_router, prefix="/babies", tags=["babies"])
api_router.include_router(health_router, prefix="/health", tags=["health"])
api_router.include_router(daily_log_router, prefix="/daily-log", tags=["daily-log"])
api_router.include_router(notifications_router, prefix="/notifications", tags=["notifications"])
api_router.include_router(advice_router, prefix="/advice", tags=["advice"])
api_router.include_router(users_router, prefix="/users", tags=["users"])
