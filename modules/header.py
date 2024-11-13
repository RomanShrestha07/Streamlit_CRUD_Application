import streamlit as st


def header():
    st.set_page_config(layout="wide")

    ## Title & details
    st.title("Assignment 3")
    st.subheader("Roman Shrestha | 100414361 | CPSC-4820-001")
    st.write(
        "A simple application made with Streamlit to perform CRUD operations on the Customer table of a Car database.")
