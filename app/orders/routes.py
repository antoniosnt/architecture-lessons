from fastapi import APIRouter

from app.orders.model import OrderEntries

router = APIRouter("/orders")


@router.post("/")
def create_order(order: OrderEntries):
    return {"message": "Order received!", "cep": order.cep}
