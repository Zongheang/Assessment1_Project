from .database import get_connection


def generate_bill(table_number):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT SUM(total_amount) FROM orders WHERE table_number = ?
    """, (table_number,))
    total_amount = cursor.fetchone()[0] or 0
    cursor.execute("""
        INSERT INTO bills (table_number, total_amount, payment_status)
        VALUES (?, ?, ?)
    """, (table_number, total_amount, "Pending"))
    conn.commit()
    conn.close()
    return total_amount


def mark_bill_paid(table_number):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE bills SET payment_status = 'Paid' WHERE table_number = ?
    """, (table_number,))
    conn.commit()
    conn.close()
