import sqlite3
import csv
def setup_database():
    # Create a new SQLite database
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    # Create the items table  
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        item_id INTEGER PRIMARY KEY,
        item TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()
    print("Database setup complete with items table created.")

def populate_database():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    # Populate the items table with data from inventory.csv
    with open('inventory.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cursor.execute('''
                INSERT INTO items(item_id, item, price, quantity)
                VALUES (?, ?, ?, ?)
            ''', (int(row['item_id']), row['item'], float(row['price']), int(row['quantity'])))

    conn.commit()
    conn.close()
    print("Database setup complete and items table populated.")
