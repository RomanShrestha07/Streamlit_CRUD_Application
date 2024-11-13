import streamlit as st


def header():
    st.set_page_config(layout="wide")

    ## Title & details
    st.title("Assignment 3")
    st.subheader("A simple application to perform CRUD operations on the Customer table of a Car database.")
