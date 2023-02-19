import random

class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.food_id = random.randint(1000,9999)
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock


class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.food_items = []

    def add_food_item(self, name, quantity, price, discount, stock):
        food_item = FoodItem(name, quantity, price, discount, stock)
        self.food_items.append(food_item)
        print("Food item added successfully!")
    
    def edit_food_item(self, food_id, name=None, quantity=None, price=None, discount=None, stock=None):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                if name:
                    food_item.name = name
                if quantity:
                    food_item.quantity = quantity
                if price:
                    food_item.price = price
                if discount:
                    food_item.discount = discount
                if stock:
                    food_item.stock = stock
                print("Food item updated successfully!")
                return
        print("Food item not found!")
    
    def view_all_food_items(self):
        for food_item in self.food_items:
            print("Food ID:", food_item.food_id)
            print("Name:", food_item.name)
            print("Quantity:", food_item.quantity)
            print("Price:", food_item.price)
            print("Discount:", food_item.discount)
            print("Stock:", food_item.stock)
            print("")

    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                print("Food item removed successfully!")
                return
        print("Food item not found!")

class User:
    def __init__(self, full_name, phone_number, email, address, password):
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.orders = []

    def place_order(self, food_items):
        order = {
            "food_items": food_items,
            "status": "Placed"
        }
        self.orders.append(order)
        print("Order placed successfully!")
    
    def view_order_history(self):
        for order in self.orders:
            print("Food items:", order["food_items"])
            print("Status:", order["status"])
            print("")
    
    def update_profile(self, full_name=None, phone_number=None, email=None, address=None, password=None):
        if full_name:
            self.full_name = full_name
        if phone_number:
            self.phone_number = phone_number
        if email:
            self.email = email
        if address:
            self.address = address
        if password:
            self.password = password
        print("Profile updated successfully!")

# Sample usage
admin = Admin("admin", "password")
user = User("John Doe", "+1 123-456-7890", "johndoe@example.com", "123 Main St, Anytown, USA", "password")

# Admin functionalities
admin.add_food_item("Tandoori Chicken", "4 pieces", 240, 0, 50)
admin.add_food_item("Vegan Burger", "1 piece", 320, 10, 20)
admin.add_food_item("Truffle Cake", "500gm", 900, 5,30) 


admin.remove_food_item('102')
admin.edit_food_item("Truffle Cake", "500gm", 900, 5,30)
admin.view_all_food_items()
user.view_order_history()
user.place_order('poha')
admin.view_all_food_items()
user.update_profile('Mayur Puranik','+91-75117340199','abc@gmail.com','balaji nagar','passwqord')

    
            
