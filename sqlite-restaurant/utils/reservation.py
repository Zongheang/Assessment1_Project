from .database import get_connection


def reserve_table(customer_name, table_number, reservation_time):
    conn = get_connection()
    cursor = conn.cursor()

    # Check if the table is already reserved at the given time
    cursor.execute("""
        SELECT * FROM reservations
        WHERE table_number = ? AND reservation_time = ?
    """, (table_number, reservation_time))
    existing_reservation = cursor.fetchone()

    if existing_reservation:
        print(
            f"\n❌ Table {table_number} is already reserved for {reservation_time}. Please choose a different time or table.")
        conn.close()
        return False
    else:
        # If no conflict, proceed with the reservation
        cursor.execute("""
            INSERT INTO reservations (customer_name, table_number, reservation_time)
            VALUES (?, ?, ?)
        """, (customer_name, table_number, reservation_time))
        conn.commit()
        conn.close()

        print(
            f"\n✅ Reservation confirmed for {customer_name} at table {table_number} on {reservation_time}.")
        return True


def view_reservations():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations")
    reservations = cursor.fetchall()
    conn.close()
    return reservations
