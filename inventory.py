import datetime

class Product:
    def __init__(self, product_id, product_name, quantity_in_stock):
        self.product_id = product_id
        self.product_name = product_name
        self.quantity_in_stock = quantity_in_stock
    
    def calculate_value(self):
        return self.quantity_in_stock

class Simpleproduct(Product):
    def __init__(self, product_id, product_name, quantity_in_stock, unit_price):
        super().__init__(product_id, product_name, quantity_in_stock)
        self.unit_price = unit_price

    def calculate_value(self):
        return self.quantity_in_stock * self.unit_price

class Perishableproduct(Simpleproduct):
    def __init__(self, product_id, product_name, quantity_in_stock, unit_price, expiry_date, shelf_life):
        super().__init__(product_id, product_name, quantity_in_stock, unit_price)
        self.expiry_date = expiry_date
        self.shelf_life = shelf_life

    def calculate_value(self):
        shelf_life = self.expiry_date - datetime.datetime.now()
        discount_factor = shelf_life.days / self.shelf_life 
        total_value = self.quantity_in_stock * self.unit_price
        discounted_value = total_value * (1 - discount_factor)
        return discounted_value
        
class Digitalproducts(Product):
    def __init__(self, product_id, product_name, quantity_in_stock, price):
        super().__init__(product_id, product_name, quantity_in_stock) 
        self.price = price

    def calculate_value(self):
        return self.quantity_in_stock * self.price

print("Choose the product type:")
print("1. Simple")
print("2. Perishable")
print("3. Digital")
choice = int(input("Enter your choice (1/2/3): "))

product_id = input("Enter product ID: ")
name = input("Enter product name: ")
quantity = int(input("Enter quantity: "))

if choice == 1:
    unit_price = float(input("Enter unit price: "))
    product = Simpleproduct(product_id, name, quantity, unit_price)
elif choice == 2:
    unit_price = float(input("Enter unit price: "))
    expiry_date = datetime.datetime.strptime(input("Enter expiry date (YYYY-MM-DD): "), "%Y-%m-%d")
    shelf_life = float(input("Enter shelf life (in days): "))
    product = Perishableproduct(product_id, name, quantity, unit_price, expiry_date, shelf_life)
elif choice == 3:
    price = float(input("Enter price: "))
    product = Digitalproducts(product_id, name, quantity, price)
else:
    print("Invalid choice.")

total_value = product.calculate_value()
print("Total value of product:", total_value)