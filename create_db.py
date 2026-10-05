import sqlite3

conn = sqlite3.connect("store.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL
)
""")

conn.commit()
conn.close()

print("Database Created")
