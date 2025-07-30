import sqlite3
# Using item class makes it simpler to manage items
class Item:
    def __init__(self, item_id, name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

# Cart class allows adding/removing items and managing cart price
# It also handles stock management when items are added or removed
# In the main program loop, a Cart object will be created to manage the user's cart, then will be cleared after checkout
# This allows for multiple transactions without needing to recreate the cart each time
class Cart:
    def __init__(self):
        self.items = []
        self.total_price = 0.0
    
    def add_item(self, item, quantity):
        if item.quantity >= quantity:
            self.items.append((item, quantity))
            item.quantity -= quantity
            self.add_to_total_price(item, quantity)
        else:
            print(f"Not enough {item.name} in stock to add to cart.")

    def remove_item(self, item, quantity):
        for cart_item in self.items:
            if cart_item.id == item.id:
                # if its possible to remove that quantity
                if cart_item.quantity >= quantity:
                    cart_item.quantity -= quantity  # remove that quantity
                    item.quantity += quantity  # update stock
                    self.remove_from_total_price(item, quantity) #update cart price
                    if cart_item.quantity == 0:
                        self.items.remove(cart_item)
                else:
                    print(f"Not enough {item.name} in cart to remove.")
                return
    
    # use this for clear button or after checkout
    def clear_cart(self):
        self.total_price = 0.0
        self.items.clear()

    # Price management methods
    def add_to_total_price(self, item, quantity):
        self.total_price += item.price * quantity
    def remove_from_total_price(self, item, quantity):
        self.total_price -= item.price * quantity

# Find item, convert to obj 
def find_item_by_id(item_id):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items WHERE item_id = ?', (item_id,)) #id will be unique
    item_tuple = cursor.fetchone()
    conn.close()
    item_obj = Item(*item_tuple) if item_tuple else None
    return item_obj
def find_item_by_name(item_name):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM items WHERE item = ?', (item_name,))
    item_tuple = cursor.fetchone()
    conn.close()
    item_obj = Item(*item_tuple) if item_tuple else None
    return item_obj
