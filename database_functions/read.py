import sqlite3

import pandas as pd


def check_connection(connection):
    val = True

    try:
        connection.cursor()
    except sqlite3.ProgrammingError:
        print('Connection closed. Cannot operate on a closed database.')
        val = False

    return val


def read_customer_data():
    conn = sqlite3.connect('data/Car_Database.db')

    columns = []
    rows = []

    if check_connection(conn):
        read_query = "SELECT * FROM Customers"

        get_table = conn.execute(read_query)

        columns = ','.join([description[0] for description in get_table.description]).title().replace('_', ' ').split(
            ',')
        rows = [row for row in get_table]

    conn.close()

    return columns, rows


def get_customers_data():
    customer_cols, customer_rows = read_customer_data()

    customer_df = pd.DataFrame(customer_rows, columns=customer_cols)

    return customer_df
