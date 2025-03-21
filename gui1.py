import streamlit as st

st.title("First app with streamlit")
st.write("Welcome to your order management app")

uploaded_file = st.file_uploader("Upload your spreadsheet here")
if uploaded_file:
    st.write("File uploaded successfully!")

# Simulate getting customers
customers = ["Alice", "Bob", "Charlie"]
selected_customer = st.selectbox("Choose a customer", customers)

st.write(f"Selected customer: {selected_customer}")
