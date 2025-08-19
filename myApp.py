import streamlit as st
import pandas as pd
import numpy as np

# Title and Description
st.title("Simple Streamlit Demo App")
st.write("This is a simple demo where user input and data visualization are shown.")

# User input section
name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 1, 100, 25)
hobby = st.selectbox("Choose your favorite hobby:", ["Reading", "Gaming", "Sports", "Music"])

# Display user input
if st.button("Show My Info"):
    st.success(f"Hello {name}, you are {age} years old and you like {hobby}!")

# Random Data Visualization
st.subheader("Random Data Chart")
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(data)
