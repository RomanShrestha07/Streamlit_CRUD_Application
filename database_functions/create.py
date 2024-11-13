import sqlite3

from database_functions.read import check_connection


def create_customer(first_name, last_name, gender, household_income, birthdate, phone_number, email):
    conn = sqlite3.connect('data/Car_Database.db')

    if check_connection(conn):
        try:
            insert_query = "INSERT INTO Customers (first_name, last_name, gender, household_income, birthdate, phone_number, email) VALUES (?, ?, ?, ?, ?, ?, ?);"

            conn.execute(insert_query,
                         (first_name, last_name, gender, household_income, birthdate, phone_number, email))

            conn.commit()
            print("Customer added successfully.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        finally:
            conn.close()
