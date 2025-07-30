import sqlite3
import csv
import os


# Get the directory this script is in
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DB_PATH = BASE_DIR / 'inventory.db'
CSV_PATH = BASE_DIR / 'inventory.csv'

print("Database will be created at:", DB_PATH)
print("CSV data will be read from:", CSV_PATH)



def setup_database():
    # Create a new SQLite database
    conn = sqlite3.connect(DB_PATH)
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
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items")

    # Populate the items table with data from inventory.csv
    with open(CSV_PATH, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cursor.execute('''
                INSERT INTO items(item_id, item, price, quantity)
                VALUES (?, ?, ?, ?)
            ''', (int(row['item_id']), row['item'], float(row['price']), int(row['quantity'])))

    conn.commit()
    conn.close()
    print("Database setup complete and items table populated.")

if __name__ == "__main__":
    setup_database()
    populate_database()