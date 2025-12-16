import os
import streamlit as st
import pandas as pd
import numpy as py

sales_data = np.random.rand(100) * 1000
 # Step 4: Create a DataFrame
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = np.random.rand(5) * 1000
customers = np.random.randint(1, 100, size=5)
df = pd.DataFrame({
    'Product': products,
    'Sales': sales,
    'Customers': customers
})


# Step 4: Convert 'order_date' to datetime
df['order_date'] = pd.to_datetime(df['order_date'])  # Convert to datetime if not already

# Step 5: Create a Selectbox for Year Selection
year = st.selectbox(
    'Select the year',
    ('2019', '2020', '2021', '2022')
)

# Step 6: Filter Data Based on Selected Year
df_filtered = df[df['order_date'].dt.year == int(year)]

# Step 7: Select Relevant Columns (e.g., 'Product', 'Sales', 'Customers', etc.)
df_selected = df_filtered[['product_name', 'sales', 'profit', 'order_date', 'customer']]  # Modify this based on your dataset's actual column names

# Step 8: Visualize Sales Data

# Create columns for the first row of charts
col1, col2 = st.columns(2)

# Line Chart - Sales Over Time
with col1:
    st.markdown("### Sales Over Time")
    df_sorted = df_selected.sort_values(by='order_date')
    st.line_chart(df_sorted.groupby('order_date')['sales'].sum())  # Sales over time

# Area Chart - Cumulative Sales
with col2:
    st.markdown("### Cumulative Sales")
    df_sorted['Cumulative Sales'] = df_sorted['sales'].cumsum()
    st.area_chart(df_sorted[['order_date', 'Cumulative Sales']].set_index('order_date'))

# Create columns for the second row of charts
col3, col4 = st.columns(2)

# Bar Chart - Sales by Product
with col3:
    st.markdown("### Sales by Product")
    sales_by_product = df_selected.groupby('product_name')['sales'].sum()
    st.bar_chart(sales_by_product)

# Scatter Chart - Customer Engagement by Product
with col4:
    st.markdown("### Customer Engagement by Product")
    engagement_by_product = df_selected.groupby('product_name')['customer'].nunique()  # Unique customers per product
    st.scatter_chart(engagement_by_product)
