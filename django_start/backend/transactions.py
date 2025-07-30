# In the program loop, a day object will be created to manage the transactions before close
# Every time a cart is sold, all of the items in the card will be recorded as items sold in the data object
# When the day is closed, transactions will be recorded to the database, data will be recorded, and the day object will be cleared
import sqlite3
from backend.inventory import Cart, Item
from datetime import datetime

def sell_cart(cart):
    record_transaction(cart)
    cart.clear_cart()

def record_transaction(cart, transaction_id):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Record the trasaction in transactions table
    cursor.execute('''
        INSERT INTO transactions (id, price, timestamp)
        VALUES (?, ?, ?)
    ''', (transaction_id, cart.total_price, timestamp))
    
    # Record each item sold in transaction_items table   
    for item in cart.items:
        cursor.execute('''
            INSERT INTO transaction_items (transaction_id, item_id, quantity, price)
            VALUES (?, ?, ?, ?)
        ''', (transaction_id, item.item_id, item.quantity, item.price))
    
    conn.commit()
    conn.close()

    # make sure to increment transaction_id for next transaction  

def get_daily_total_revenue():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT SUM(price) FROM transactions
        WHERE DATE(timestamp) = DATE('now')
    ''')
    total_daily_revenue = cursor.fetchone()[0] #the [0] extracts the single value from the tuple
    conn.close()
    if total_daily_revenue is None:
        print("No transactions today.")
        return 0.0
    
    return total_daily_revenue #float

def get_transaction_history():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    # 
    cursor.execute('''
        SELECT t.id, t.price, t.timestamp,ti. ti.item_id, ti.quantity, ti.price
        FROM transactions t
        JOIN transaction_items ti ON t.id = ti.transaction_id
    ''')
    transactions = cursor.fetchall()
    conn.close()
    
    transaction_history = []
    for row in transactions:
        transaction_history.append({
            'transaction_id': row[0],
            'total_price': row[1],
            'timestamp': row[2],
            'item_id': row[3],
            'quantity': row[4],
            'item_price': row[5]
        })

    return transaction_history #list of dicts