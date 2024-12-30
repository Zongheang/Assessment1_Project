from .database import get_connection


def reserve_table(customer_name, table_number, reservation_time):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO reservations (customer_name, table_number, reservation_time)
        VALUES (?, ?, ?)
    """, (customer_name, table_number, reservation_time))
    conn.commit()
    conn.close()


def view_reservations():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations")
    reservations = cursor.fetchall()
    conn.close()
    return reservations
