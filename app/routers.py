from fastapi import APIRouter

from app.healthy.routes import router as healthy_router
from app.orders.routes import router as order_router

router = APIRouter(prefix="/api")

router.include_router(healthy_router)
router.include_router(order_router)

