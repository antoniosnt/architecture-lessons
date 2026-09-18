from fastapi import APIRouter

from app.orders.model import OrderEntries
from app.orders.service import OrderService

router = APIRouter("/orders")


@router.post("/")
def create_order(order: OrderEntries):
    order_service = OrderService()

    order_service.confirm_order(order=order)

    return {"message": "Confirmed!"}
