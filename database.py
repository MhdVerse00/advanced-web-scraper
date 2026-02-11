import sqlite3

def create_connection():
    conn = sqlite3.connect("products.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price TEXT,
            rating TEXT,
            link TEXT
        )
    """)

    conn.commit()
    conn.close()

def insert_data(title, price, rating, link):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO products (title, price, rating, link)
        VALUES (?, ?, ?, ?)
    """, (title, price, rating, link))

    conn.commit()
    conn.close()
