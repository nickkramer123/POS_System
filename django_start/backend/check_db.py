import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, '..', 'inventory.db'))

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()


c.execute("SELECT * FROM items")


rows = c.fetchall()

for row in rows:
    print(row)

conn.close()