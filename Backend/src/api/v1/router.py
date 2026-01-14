from fastapi import APIRouter

api_router = APIRouter()

# Import des routeurs (à activer quand les fichiers seront créés)
# from api.v1.auth.endpoints import router as auth_router
# from api.v1.users.endpoints import router as users_router
# from api.v1.babies.endpoints import router as babies_router
# from api.v1.health.endpoints import router as health_router
# from api.v1.daily_log.endpoints import router as daily_log_router
# from api.v1.notifications.endpoints import router as notifications_router
# from api.v1.advice.endpoints import router as advice_router

# Inclure tous les routeurs
# api_router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
# api_router.include_router(users_router, prefix="/users", tags=["Users"])
# api_router.include_router(babies_router, prefix="/babies", tags=["Babies"])
# api_router.include_router(health_router, prefix="/health", tags=["Health"])
# api_router.include_router(daily_log_router, prefix="/daily-log", tags=["Daily Log"])
# api_router.include_router(notifications_router, prefix="/notifications", tags=["Notifications"])
# api_router.include_router(advice_router, prefix="/advice", tags=["Advice"])

# Pour l'instant, créons une route de test
@api_router.get("/test")
def test_route():
    return {"message": "API is working"}
