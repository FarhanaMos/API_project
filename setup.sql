-- denna setup.sql filen är schema för tabellerna i databasen som används i db.py

-- tabell för customers
CREATE TABLE 
    customer (
        id INTEGER PRIMARY KEY, 
        name VARCHAR(255)
    );

-- tabell for products
CREATE TABLE 
    product (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR(255), 
        price INTEGER, 
        category VARCHAR(255)
    );

-- tabell för orders
CREATE TABLE
    orders (
        id INTEGER PRIMARY KEY,
        order_date DATE,
        customer_id INTEGER,
        FOREIGN KEY (customer_id) REFERENCES customer(id)
    );

-- tabell för order_items
CREATE TABLE
    order_item (
        id INTEGER PRIMARY KEY,
        order_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        FOREIGN KEY (order_id) REFERENCES orders(id),
        FOREIGN KEY (product_id) REFERENCES product(id)
    );
