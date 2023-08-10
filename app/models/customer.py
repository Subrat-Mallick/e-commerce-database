from pydantic import BaseModel


class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    email: str


class CustomerCreate(CustomerBase):
    password: str


class Customer(CustomerBase):
    id: int

    class Config:
        orm_mode = True
