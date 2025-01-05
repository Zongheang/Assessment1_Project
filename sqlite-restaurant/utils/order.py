from .database import get_connection


def add_order(table_number, order_details, total_amount):
    if not table_number:
        print("❌ Error: Table number is required to add an order.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    # Check if the table exists in the reservations table
    cursor.execute(
        "SELECT * FROM reservations WHERE table_number = ?", (table_number,))
    reservation = cursor.fetchone()

    if not reservation:
        print(
            f"❌ Error: Table number {table_number} does not exist in the reservations.")
        conn.close()
        return

    # If the table exists, insert the order
    cursor.execute("""
        INSERT INTO orders (table_number, order_details, total_amount)
        VALUES (?, ?, ?)
    """, (table_number, order_details, total_amount))
    conn.commit()
    conn.close()
    print("✅ Order added successfully!")


def view_orders():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    conn.close()
    return orders
