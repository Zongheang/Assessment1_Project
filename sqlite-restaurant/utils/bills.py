from .database import get_connection


def generate_bill(table_number):
    if not table_number:
        print("❌ Error: Table number is required to generate a bill.")
        return 0

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
        return 0

    # Check if a bill already exists for this table with status 'Paid'
    cursor.execute(
        "SELECT * FROM bills WHERE table_number = ? AND payment_status = 'Paid'", (table_number,))
    existing_bill = cursor.fetchone()

    if existing_bill:
        print(f"❌ Error: Bill for table {table_number} has already been paid.")
        conn.close()
        return 0

    # Check if a bill already exists for this table with status 'Pending'
    cursor.execute(
        "SELECT * FROM bills WHERE table_number = ? AND payment_status = 'Pending'", (table_number,))
    pending_bill = cursor.fetchone()

    if pending_bill:
        print(
            f"❌ Error: A pending bill already exists for table {table_number}. Please complete the payment first.")
        conn.close()
        return 0

    # Calculate the total amount from the orders table
    cursor.execute(
        "SELECT SUM(total_amount) FROM orders WHERE table_number = ?", (table_number,))
    total_amount = cursor.fetchone()[0] or 0

    # Insert the bill into the bills table
    cursor.execute("""
        INSERT INTO bills (table_number, total_amount, payment_status)
        VALUES (?, ?, ?)
    """, (table_number, total_amount, "Pending"))
    conn.commit()
    conn.close()

    print(
        f"✅ Bill generated for table number {table_number}. Total amount: ${total_amount:.2f}")
    return total_amount


def mark_bill_paid(table_number):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE bills SET payment_status = 'Paid' WHERE table_number = ?
    """, (table_number,))
    conn.commit()
    conn.close()
