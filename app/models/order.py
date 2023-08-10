from pydantic import BaseModel
from typing import List


class OrderItem(BaseModel):
    product_id: int
    quantity: int


class OrderBase(BaseModel):
    customer_id: int
    items: List[OrderItem]


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True
