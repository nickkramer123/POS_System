import sqlite3
import csv

# Create a new SQLite database
conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

# Create the items table  
cursor.execute('''
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
''')

# Populate the items table with data from inventory.csv
with open('inventory.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute('''
            INSERT INTO items(id, item, price, quantity)
            VALUES (?, ?, ?, ?)
        ''', (int(row['id']), row['item'], float(row['price']), int(row['quantity'])))

conn.commit()
conn.close()
print("Database setup complete and items table populated.")
