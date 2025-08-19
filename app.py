import streamlit as st

st.title("Demo App")

name = st.text_input("Write your name:")
if st.button("Submit"):
    st.write(f"Hello, {name}!")
