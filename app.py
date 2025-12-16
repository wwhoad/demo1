import streamlit as st
import pandas as pd
 # Sample Data
data = {
    'Product': ['A', 'B', 'C', 'D', 'E'],
    'Sales': [1200, 850, 950, 1100, 1300],
    'Customers': [300, 400, 350, 450, 500]
}
df = pd.DataFrame(data)
 # Display Sample Data
st.write("### Sales Data")
st.write(df)
 # Slider for Sales Range
sales_range = st.slider("Select Sales Range", min_value=0, max_value=1500, value=(500, 1000))
 # Filter Data Based on Sales Range
filtered_df = df[(df['Sales'] >= sales_range[0]) & (df['Sales'] <= sales_range[1])]
st.write("### Filtered Data")
st.write(filtered_df)
 # Selectbox for Product Choice
product_choice = st.selectbox("Select Product", filtered_df['Product'].unique()) #return all the unique values in a column
 # Text Input for User Name
user_name = st.text_input("Enter your name")
 # Text Area for Feedback
feedback = st.text_area("Enter your feedback")
 # Checkbox for Agreement
agree = st.checkbox("I agree to the terms and conditions")
 # File Uploader for Uploading Files
uploaded_file = st.file_uploader("Upload a relevant file")
 # Button to Submit Feedback
if st.button("Submit Feedback"):
    if agree:
        st.write("### Submitted Feedback")
        st.write(f"**Name:** {user_name}")
        st.write(f"**Product:** {product_choice}")
        st.write(f"**Sales Range:** {sales_range}")
        st.write(f"**Feedback:** {feedback}")
        if uploaded_file is not None:
            st.write("File uploaded successfully!")
    else:
        st.write("You must agree to the terms and conditions to submit feedback.")
