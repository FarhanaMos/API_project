from fastapi import FastAPI
from pydantic import BaseModel
from db import DB
from models import Product, Customer

app = FastAPI()
db = DB("order_api.db")

# GET Endpoints
@app.get("/products")
def get_all_products():
    data = db.get(table="product")
    return data

@app.get("/products/price/{price}")
def get_product_by_price(price: int):
    data = db.get(table="product", where=("price", str(price)))
    return data 

@app.get("/products/{id}")
def get_product_by_id(id: int):
    data = db.get(table="product", where=("id", id))
    return data

@app.get("/customers")
def get_all_customers():
    data = db.get(table="customer")
    return data 


# POST Endpoints
@app.post("/products")
def create_product(product: Product):
    db.insert(table="product", fields={"name": product.name, "price": str(product.price), "category": product.category})
    return {"status": "Product created"}


@app.post("/customers")
def create_customer(customer: Customer):
    db.insert(table="customer", fields={"name": customer.name})
    return {"status": "Customer created"}

# PUT Endpoint
@app.put("/products/{id}")
def update_product(id: int, product: Product):
    db.update(table="product", where=("id", id), fields={"name": product.name, "price": str(product.price), "category": product.category})
    return {"status": "Product updated"}


# DELETE Endpoints
@app.delete("/products/{id}")
def delete_product(id: int):
    db.delete(table="product", id=id)
    return {"status": "Product deleted"}

@app.delete("/customers/{id}")
def delete_customer(id: int):
    db.delete(table="customer", id=id)
    return {"status": "Customer deleted"}