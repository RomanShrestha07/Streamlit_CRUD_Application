import re
from datetime import datetime

import streamlit as st

from database_functions.create import create_customer


def validate_form(first_name, last_name, email):
    ## Validate Values
    if first_name.strip() == "":
        st.warning("First Name cannot be empty.")
        st.stop()

    if last_name.strip() == "":
        st.warning("Last Name cannot be empty.")
        st.stop()

    if email.strip() == "":
        st.warning("Email cannot be empty.")
        st.stop()

    valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email.strip())
    if not valid:
        st.warning("Invalid email address.")
        st.stop()


def create_form():
    gender_options = ["Male", "Female"]
    min_date = datetime.strptime('1900-01-01', '%Y-%m-%d')

    ## Create Customer Form
    with st.form("create_form", enter_to_submit=False, border=False):
        row1 = st.columns([1, 1])
        first_name = row1[0].text_input("First Name")
        last_name = row1[1].text_input("Last Name")

        row2 = st.columns([1, 1])
        gender = row2[0].selectbox("Gender", gender_options)
        household_income = row2[1].number_input("Household Income", value=0)

        row3 = st.columns([1, 1])
        birthdate = row3[0].date_input("Birthdate", min_value=min_date, max_value=datetime.today())
        phone_number = row3[1].number_input("Phone Number", value=0)

        email = st.text_input("Email")

        submitted = st.form_submit_button("Submit")

        if submitted:
            validate_form(first_name, last_name, email)

            create_customer(first_name, last_name, gender, household_income, birthdate, phone_number, email)
            st.rerun()
