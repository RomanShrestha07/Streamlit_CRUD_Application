import sqlite3

from database_functions.read import check_connection


def update_customer(customer_id, first_name, last_name, gender, household_income, birthdate, phone_number, email):
    conn = sqlite3.connect('data/Car_Database.db')

    if check_connection(conn):
        try:
            update_query = "UPDATE Customers SET first_name = ?, last_name = ?, gender = ?, household_income = ?, birthdate = ?, phone_number = ?, email = ? WHERE customer_id = ?;"

            conn.execute(update_query,
                         (first_name, last_name, gender, household_income, birthdate, phone_number, email, customer_id))

            conn.commit()
            print("Customer updated successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()
