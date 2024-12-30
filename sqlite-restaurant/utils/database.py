import sqlite3

DB_FILE = "restaurant.db"


def get_connection():
    return sqlite3.connect(DB_FILE)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            table_number INTEGER,
            reservation_time TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            table_number INTEGER,
            order_details TEXT,
            total_amount REAL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            table_number INTEGER,
            total_amount REAL,
            payment_status TEXT
        )
    """)
    conn.commit()
    conn.close()
