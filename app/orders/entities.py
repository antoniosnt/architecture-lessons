from orders.repository import OrderRepository
from app.orders.model import OrderEntries


class OrderEntities:
    def __init__(self, order_rep=OrderRepository):
        self.order_rep = order_rep()

    def confirm_order(self, order=OrderEntries):
        order = self.order_rep.find_order(identifier=order.get("id"))

        if not order.get("items"):
            raise ValueError("Order without items.")

        return True
