# Denna fil seedar data fr en json fil till db
import json
import sqlite3

# Kopplar till order_api.db
conn = sqlite3.connect("order_api.db")
cursor = conn.cursor()

# Öppnar JSON fil och hämtar data
with open("seed.json") as file:
    data = json.load(file)

# Lägger in data till tables
# Seedar data för table product
for record in data["product"]:
    query = """INSERT INTO product (
                    name, price, category
                )
                VALUES (
                    ?, ?, ?
                )"""
    values = (record["name"], record["price"], record["category"])
    cursor.execute(query, values)

# Seedar data för table customers 
for record in data["customer"]:
    query = """INSERT INTO customer (
                name
                )
                VALUES (
                    ?
                )"""
    values = (record["name"],)  
    cursor.execute(query, values)

for record in data["orders"]:
    query = """INSERT INTO orders (
                order_date, 
                customer_id
                )
                VALUES (
                    ?, ?
                )"""
    values = (record["order_date"], record["customer_id"],)  
    cursor.execute(query, values)

for record in data["order_item"]:
    query = """INSERT INTO order_item (
                order_id, 
                product_id, 
                quantity
                )
                VALUES (
                    ?, ?, ?
                )"""
    values = (record["order_id"], record["product_id"], record["quantity"])  
    cursor.execute(query, values)

# Commitar uppdateringen och stänger ner kopplingen till databasen
conn.commit()
conn.close()