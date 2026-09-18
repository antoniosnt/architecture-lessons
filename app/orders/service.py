from orders.repository import OrderRepository

from app.orders.model import OrderEntries


class OrderService:
    def __init__(self, order_rep=OrderRepository):
        self.order_rep = order_rep()

    def confirm_order(self, order=OrderEntries):
        order = self.order_rep.find_order(pk_order=order.get("pk_order"))

        if not order.get("items"):
            raise ValueError("Order without items.")

        return True
