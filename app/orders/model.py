from pydantic import BaseModel


class ProductEntries(BaseModel):
    product_id: int
    quantity: int
    price: float


class OrderEntries(BaseModel):
    cep: str
    itens: list[ProductEntries]
