import streamlit as st

from modules.create_form import create_form
from modules.header import header
from modules.view_data import view_data


# Starting the app
def main():
    ## Modals
    @st.dialog("Add Customer", width="large")
    def create_modal():
        create_form()

    ## Display
    header()

    ## Create Customer
    if st.button("Add Customer"):
        create_modal()

    ## Data View
    view_data()


if __name__ == '__main__':
    main()
