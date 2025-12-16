# Step 1: Install Streamlit (run in terminal: pip install streamlit)
# This command installs the Streamlit library to create web apps

# Step 2: Import Necessary Libraries
import streamlit as st  # Main library for creating the web dashboard
import pandas as pd     # For data manipulation and analysis

# Step 3: Load Superstore Dataset
df = pd.read_csv('superstore_dataset.csv')  
# Reads the CSV file into a pandas DataFrame called 'df'

# Step 4: Convert 'order_date' to datetime
df['order_date'] = pd.to_datetime(df['order_date'])  
# Converts the 'order_date' column from string to datetime format
# This enables date-based operations like .dt.year, .dt.month, etc.

# Step 5: Create a Selectbox for Year Selection
year = st.selectbox(
    'Select the year',  # Label shown above the dropdown
    ('2019', '2020', '2021', '2022')  # Available options
)
# Creates an interactive dropdown menu
# Selected value is stored in 'year' variable as a string

# Step 6: Filter Data Based on Selected Year
df_filtered = df[df['order_date'].dt.year == int(year)]
# Filters the DataFrame to keep only rows where:
# - df['order_date'].dt.year extracts the year from each date
# - int(year) converts the selected year string to integer
# - '==' compares and keeps matching rows

# Step 7: Select Relevant Columns 
# Adjust column names based on your actual dataset:
df_selected = df_filtered[['product_name', 'sales', 'profit', 'order_date', 'customer']]
# Creates a new DataFrame with only specified columns
# Common Superstore column names might be: 
# 'Product Name', 'Sales', 'Profit', 'Order Date', 'Customer Name'

# Step 8: Visualize Sales Data

# Create two columns for the first row of charts
col1, col2 = st.columns(2)
# Creates a 2-column layout for better organization

# ------------------- COLUMN 1: Line Chart -------------------
with col1:
    st.markdown("### Sales Over Time")  # Creates H3 heading
    df_sorted = df_selected.sort_values(by='order_date')  # Sort by date (ascending)
    # Group by date and sum sales for each date:
    sales_over_time = df_sorted.groupby('order_date')['sales'].sum()
    st.line_chart(sales_over_time)  # Creates interactive line chart

# ------------------- COLUMN 2: Area Chart -------------------
with col2:
    st.markdown("### Cumulative Sales")  # Creates H3 heading
    df_sorted['Cumulative Sales'] = df_sorted['sales'].cumsum()
    # '.cumsum()' calculates running total of sales
    st.area_chart(
        df_sorted[['order_date', 'Cumulative Sales']].set_index('order_date')
    )  # Creates filled area chart

# Create two columns for the second row of charts
col3, col4 = st.columns(2)
# Second row of 2-column layout

# ------------------- COLUMN 3: Bar Chart -------------------
with col3:
    st.markdown("### Sales by Product")
    # Group by product and sum sales for each product:
    sales_by_product = df_selected.groupby('product_name')['sales'].sum()
    st.bar_chart(sales_by_product)  # Creates bar chart

# ------------------- COLUMN 4: Scatter Chart -------------------
with col4:
    st.markdown("### Customer Engagement by Product")
    # Count unique customers per product:
    engagement_by_product = df_selected.groupby('product_name')['customer'].nunique()
    # '.nunique()' counts distinct customers
    st.scatter_chart(engagement_by_product)  # Creates scatter chart

# Step 9: Run the Streamlit App (run in terminal: streamlit run app.py)
