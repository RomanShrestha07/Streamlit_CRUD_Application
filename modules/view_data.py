import streamlit as st

from database_functions.read import get_customers_data
from modules.delete_form import delete_form
from modules.update_form import update_form


def view_data():
    ## Modals
    @st.dialog("Delete Customer")
    def delete_modal(selected_customer):
        customer_id = selected_customer['Customer Id'].squeeze()
        customer_fname = selected_customer['First Name'].squeeze()
        customer_lname = selected_customer['Last Name'].squeeze()

        delete_form(int(customer_id), customer_fname, customer_lname)

    @st.dialog("Update Customer", width="large")
    def update_modal(selected_customer):
        update_form(selected_customer)

    ## Customer Data
    customer_df = get_customers_data()

    event = st.dataframe(
        data=customer_df,
        hide_index=True,
        on_select="rerun",
        selection_mode="single-row",
        column_config={
            "Customer Id": "ID"
        }
    )

    ## Update/Delete Buttons
    if len(event.selection["rows"]) > 0:
        selected_key = event.selection["rows"][0]
        selected_row = customer_df.iloc[[selected_key]]

        left, middle, _ = st.columns(3)

        if left.button("Update Customer", use_container_width=True):
            update_modal(selected_row)

        if middle.button("Delete Customer", use_container_width=True):
            delete_modal(selected_row)
