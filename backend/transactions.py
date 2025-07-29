# In the program loop, a day object will be created to manage the transactions before close
# Every time a cart is sold, all of the items in the card will be recorded as items sold in the data object
# When the day is closed, transactions will be recorded to the database, data will be recorded, and the day object will be cleared
import sqlite3

class Day:
    def __init__(self):
        self.items_sold = [] # list of cart items
        self.total_revenue = 0.0
    
    def sell_cart(self, cart):
