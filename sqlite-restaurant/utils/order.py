from .database import get_connection


def add_order(table_number, order_details, total_amount):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO orders (table_number, order_details, total_amount)
        VALUES (?, ?, ?)
    """, (table_number, order_details, total_amount))
    conn.commit()
    conn.close()


def view_orders():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    conn.close()
    return orders
