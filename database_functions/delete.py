import sqlite3

from database_functions.read import check_connection


def delete_customer(customer_id):
    conn = sqlite3.connect('data/Car_Database.db')

    if check_connection(conn):
        try:
            delete_query = "DELETE FROM Customers WHERE (customer_id = ?);"

            conn.execute(delete_query, (customer_id,))

            conn.commit()
            print("Customer deleted successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()
