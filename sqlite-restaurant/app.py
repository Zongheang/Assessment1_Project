from utils.database import init_db
from utils.reservation import reserve_table, view_reservations
from utils.order import add_order, view_orders
from utils.bills import generate_bill, mark_bill_paid


def main_menu():
    """Display the main menu with options."""
    print("\n==================== Restaurant Management System ====================")
    print("1. Reserve a Table")
    print("2. View Reservations")
    print("3. Add Order")
    print("4. View Orders")
    print("5. Generate Bill")
    print("6. Mark Bill as Paid")
    print("0. Exit")
    print("=======================================================================")


def display_reservation(reservation):
    """Display reservation details in a clean and professional format."""
    print(f"\nReservation ID: {reservation[0]}")
    print(f"Customer Name: {reservation[1]}")
    print(f"Table Number: {reservation[2]}")
    print(f"Reservation Time: {reservation[3]}")
    print("---------------------------------------------------------------")


def display_order(order):
    """Display order details in a clean and professional format."""
    print(f"\nOrder ID: {order[0]}")
    print(f"Table Number: {order[1]}")
    print(f"Order Details: {order[2]}")
    print(f"Total Amount: ${order[3]:.2f}")
    print("---------------------------------------------------------------")


def display_beer_bill(table_number, total_amount, payment_status):
    """Display the beer-themed bill with a professional layout."""
    print("\n================== Your Beer Bill ==================")
    print("🍻 Beer-Inspired Bill 🍻")
    print("===============================================")
    print(f"Table Number: {table_number}")
    print(f"Total Amount: ${total_amount:.2f}")
    print(f"Payment Status: {payment_status}")
    print("===============================================")
    print("\nThank you for dining with us! We hope you enjoyed your meal and drink! 🍻")
    print("---------------------------------------------------------------")


def main():
    """Main function to run the Restaurant Management System."""
    init_db()  # Initialize the database

    while True:
        main_menu()  # Display the main menu
        choice = input("Enter your choice: ")

        if choice == "1":
            customer_name = input("Enter customer name: ")
            table_number = int(input("Enter table number: "))
            reservation_time = input(
                "Enter reservation time (YYYY-MM-DD HH:MM): ")

            if reserve_table(customer_name, table_number, reservation_time):
                print(
                    f"\nReservation confirmed for {customer_name} at table {table_number} on {reservation_time}.\n")
            else:
                print(
                    f"\nTable {table_number} is already reserved at {reservation_time}. Please choose a different time or table.\n")

        elif choice == "2":
            reservations = view_reservations()
            if reservations:
                print("\n=== All Reservations ===")
                for res in reservations:
                    display_reservation(res)
            else:
                print("\nNo reservations found.\n")

        elif choice == "3":
            table_number = int(input("Enter table number: "))
            order_details = input("Enter order details: ")
            total_amount = float(input("Enter total amount: "))
            add_order(table_number, order_details, total_amount)
            print(
                f"\nOrder for table {table_number} added successfully. Total: ${total_amount:.2f}.\n")

        elif choice == "4":
            orders = view_orders()
            if orders:
                print("\n=== All Orders ===")
                for order in orders:
                    display_order(order)
            else:
                print("\nNo orders found.\n")

        elif choice == "5":
            table_number = int(input("Enter table number: "))
            total_amount = generate_bill(table_number)

            # Check if total_amount is 0 (indicating the table number wasn't found)
            if total_amount == 0:
                print(
                    f"\n❌ Error: No reservations found for table {table_number}. Bill cannot be generated.\n")
            else:
                print(f"\nGenerating your bill for table {table_number}...\n")
                display_beer_bill(table_number, total_amount, "Pending")
                print(
                    "\nYour bill has been generated. Please proceed with the payment.\n")

        elif choice == "6":
            table_number = int(input("Enter table number: "))
            mark_bill_paid(table_number)
            print(
                f"\nBill for table {table_number} has been marked as paid.\n")

        elif choice == "0":
            print(
                "\nThank you for using the Restaurant Management System! Have a great day!\n")
            break

        else:
            print("\nInvalid choice! Please select a valid option.\n")


if __name__ == "__main__":
    main()
