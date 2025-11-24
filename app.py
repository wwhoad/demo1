import streamlit as st
import pandas as pd

# Step 1: Generate Sample Data with 5 Items
data = {'Product': ['A', 'B', 'C', 'D', 'E'], 
        'Sales': [1200, 850, 950, 1100, 1300], 
        'Customers': [300, 400, 350, 450, 500]}
df = pd.DataFrame(data)

# Step 2: Display the Sample Data at the Top
st.write("### Sample Data")
st.write(df)

# Step 3: Create a Slider for Selecting a Sales Range
sales_range = st.slider("Select Sales Range", min_value=0, max_value=1500, value=(500, 1000))

# Step 4: Filter Products Based on Selected Sales Range
filtered_df = df[(df['Sales'] >= sales_range[0]) & (df['Sales'] <= sales_range[1])]

# Step 5: Create a Dropdown for Selecting a Product from Filtered Data
product_choice = st.selectbox("Select Product", filtered_df['Product'].unique())

# Step 6: Create a Form for Feedback Submission
with st.form(key="feedback_form"):
    product_id = st.text_input("Enter Product ID")
    feedback = st.text_area("Enter your feedback")
    submit_button = st.form_submit_button("Submit Feedback")

# Step 7: Define a Callback Function to Submit Feedback
def submit_feedback():
    st.write("### Submitted Feedback")
    st.write(f"**Product:** {product_choice}")
    st.write(f"**Sales Range:** {sales_range}")
    st.write(f"**Product ID:** {product_id}")
    st.write(f"**Feedback:** {feedback}")

# Step 8: Check if the Submit Button is Clicked
if submit_button:
    submit_feedback()
