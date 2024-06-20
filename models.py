from pydantic import BaseModel
from typing import Optional



#basemodel används eftersom det är datamodellklass som automatiserar hanteringen av attribut och validering av data, 
#och därmed skippa skriva init-metoder. Nedan är pydantic datamodeller som kommer från Basemdel

class Product(BaseModel):
    id: Optional[int] = None
    name: str
    price: int
    category: str
    

class Customer(BaseModel):
    id: Optional[int] = None
    name: str

class Order(BaseModel):
    id: Optional[int]
    order_date: str
    customer_id: int

class OrderItem(BaseModel):
    id: Optional[int]
    order_id: int
    product_id: int
    quantity: int
