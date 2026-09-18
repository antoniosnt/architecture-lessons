from fastapi import APIRouter

from app.healthy.routes import router as healthy_router

router = APIRouter(prefix="/api")

router.include_router(healthy_router)

