import requests
from models import Customer

BASE_URL = "http://localhost:8000"

def get_all_products():
    response = requests.get(f"{BASE_URL}/products")
    if response.status_code == 200:
        products = response.json()
        for product in products:
            print(product)
    else:
        print("Failed to retrieve products")

def get_product_by_id():
    product_id = input("Enter product ID: ")
    response = requests.get(f"{BASE_URL}/products/{product_id}")
    if response.status_code == 200:
        print(response.json())
    else:
        print("Product not found")

def get_product_by_price():
    price = input("Enter product price: ")
    response = requests.get(f"{BASE_URL}/products/price/{price}")
    if response.status_code == 200:
        products = response.json()
        for product in products:
            print(product)
    else:
        print("Product not found")

def create_product():
    name = input("Enter product name: ")
    price = input("Enter product price: ")
    category = input("Enter product category: ")
    product = {"name": name, "price": int(price), "category": category}
    response = requests.post(f"{BASE_URL}/products", json=product)
    print(response.json())

def update_product():
    product_id = input("Enter product ID: ")
    name = input("Enter new product name: ")
    price = input("Enter new product price: ")
    category = input("Enter new product category: ")
    product = {"name": name, "price": int(price), "category": category}
    response = requests.put(f"{BASE_URL}/products/{product_id}", json=product)
    print(response.json())

def delete_product():
    product_id = input("Enter product ID: ")
    response = requests.delete(f"{BASE_URL}/products/{product_id}")
    print(response.json())

def get_all_customers():
    response = requests.get(f"{BASE_URL}/customers")
    if response.status_code == 200:
        customers = response.json()
        for customer in customers:
            print(customer)
    else:
        print("Failed to retrieve customers")

def create_customer():
    name = input("Enter customer name: ")
    customer = {"name": name}
    response = requests.post(f"{BASE_URL}/customers", json=customer)
    print(response.json())


def delete_customer():
    customer_id = input("Enter customer ID: ")
    response = requests.delete(f"{BASE_URL}/customers/{customer_id}")
    print(response.json())

def menu():
    while True:
        print("\nMenu:")
        print("1. Get all products")
        print("2. Get product by ID")
        print("3. Get product by price")
        print("4. Create product")
        print("5. Update product")
        print("6. Delete product")
        print("7. Get all customers")
        print("8. Create customer")
        print("9. Delete customer")
        print("0. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            get_all_products()
        elif choice == '2':
            get_product_by_id()
        elif choice == '3':
            get_product_by_price()
        elif choice == '4':
            create_product()
        elif choice == '5':
            update_product()
        elif choice == '6':
            delete_product()
        elif choice == '7':
            get_all_customers()
        elif choice == '8':
            create_customer()
        elif choice == '9':
            delete_customer()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
