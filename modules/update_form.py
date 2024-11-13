from datetime import datetime

import streamlit as st

from database_functions.update import update_customer
from modules.create_form import validate_form


def update_form(selected_customer):
    gender_options = ["Male", "Female"]
    min_date = datetime.strptime('1900-01-01', '%Y-%m-%d')

    customer_id = int(selected_customer['Customer Id'].squeeze())
    fname = selected_customer['First Name'].squeeze()
    lname = selected_customer['Last Name'].squeeze()

    gender = selected_customer['Gender'].squeeze()
    income = selected_customer['Household Income'].squeeze()

    birth = datetime.strptime(selected_customer['Birthdate'].squeeze(), '%Y-%m-%d')
    phone = selected_customer['Phone Number'].squeeze()

    email = selected_customer['Email'].squeeze()

    ## Update Customer Form
    with st.form("update_form", enter_to_submit=False, border=False):
        row1 = st.columns([1, 1])
        first_name = row1[0].text_input("First Name", value=fname)
        last_name = row1[1].text_input("Last Name", value=lname)

        row2 = st.columns([1, 1])
        gender = row2[0].selectbox("Gender", gender_options, index=gender_options.index(gender))
        household_income = row2[1].number_input("Household Income", value=income)

        row3 = st.columns([1, 1])
        birthdate = row3[0].date_input("Birthdate", min_value=min_date, max_value=datetime.today(), value=birth)
        phone_number = row3[1].number_input("Phone Number", value=phone)

        email = st.text_input("Email", value=email)

        updated = st.form_submit_button("Update")

        if updated:
            validate_form(first_name, last_name, email)

            update_customer(customer_id, first_name, last_name, gender, household_income, birthdate, phone_number,
                            email)
            st.rerun()
