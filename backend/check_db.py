import sqlite3

conn = sqlite3.connect('inventory.db')
c = conn.cursor()

c.execute("SELECT * FROM items")

rows = c.fetchall()

for row in rows:
    print(row)

conn.close()