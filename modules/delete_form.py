import streamlit as st

from database_functions.delete import delete_customer


def delete_form(customer_id, first_name, last_name):
    ## Delete Customer Form
    st.write(f"Are you sure you want to delete customer {first_name} {last_name}?")

    if st.button("Delete"):
        delete_customer(customer_id)
        st.rerun()
