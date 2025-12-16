import streamlit as st
import time

# -------------------------------
# 1. Dashboard Title and Objective
# -------------------------------
st.title("Business Performance Dashboard")
st.write("Objective: This dashboard provides insights into revenue, customer feedback, and market trends for better business decisions.")

# -------------------------------
# 2. Columns Layout for Quarterly Revenue
# -------------------------------
st.subheader("Quarterly Revenue Overview")
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Q1 2024")
    st.write("Revenue: $1.2M")
with col2:
    st.header("Q2 2024")
    st.write("Revenue: $1.5M")
with col3:
    st.header("Q3 2024")
    st.write("Revenue: $1.3M")

# -------------------------------
# 3. Tabs for Different Business Sections
# -------------------------------
tab1, tab2, tab3 = st.tabs(["Sales Data", "Customer Insights", "Market Trends"])

with tab1:
    st.write("### Sales Data")
    sales_data = {
        "Q1 2024": "$1.2M",
        "Q2 2024": "$1.5M",
        "Q3 2024": "$1.3M",
        "Q4 2024": "$1.6M"
    }
    for quarter, revenue in sales_data.items():
        st.write(f"{quarter}: {revenue}")
    st.bar_chart({"Revenue (in M$)": [1.2, 1.5, 1.3, 1.6]}, height=200)

with tab2:
    st.write("### Customer Insights")
    customer_feedback = [
        "Great service!",
        "Very satisfied with the product quality.",
        "Quick delivery and excellent support."
    ]
    for feedback in customer_feedback:
        st.write(f"- {feedback}")

with tab3:
    st.write("### Market Trends")
    market_trends = {
        "Eco-friendly products": "Increasing demand",
        "Online shopping": "Continued growth",
        "Subscription services": "Rising popularity"
    }
    for trend, status in market_trends.items():
        st.write(f"{trend}: {status}")

# -------------------------------
# 4. Expander for Additional Information
# -------------------------------
with st.expander("More Information"):
    st.write("Data was collected through surveys, customer feedback forms, and official sales reports.")


# -------------------------------
# 5. Dynamic Loading Simulation
# -------------------------------

# Create a placeholder
placeholder = st.empty()

# Simulate loading data with progress messages
for i in range(6):  # 0%, 20%, 40%, 60%, 80%, 100%
    placeholder.write(f"Loading data... {i * 20}% complete")
    time.sleep(1)

# Replace placeholder with business insights after loading
placeholder.write("Data loading complete. Displaying business insights.")

business_insights = [
    "Revenue increased by 15% in Q1 2024.",
    "Customer satisfaction improved by 10%.",
    "Market trends show a growing demand for eco-friendly products."
]

# Display insights one by one with delay
for insight in business_insights:
    placeholder.write(insight)
    time.sleep(1)

# -------------------------------
# 6. Add Interactivity
# -------------------------------
st.subheader("Interactive Revenue Checker")
quarters = ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"]
selected_quarter = st.selectbox("Select a quarter:", quarters)

# Display revenue dynamically
st.write(f"Revenue for {selected_quarter}: {sales_data[selected_quarter]}")

# Bonus: Growth adjustment
growth = st.slider("Adjust growth percentage:", 0, 50, 10)
base_revenue = float(sales_data[selected_quarter].strip("$M"))
adjusted_revenue = base_revenue * (1 + growth / 100)
st.write(f"Adjusted Revenue for {selected_quarter}: ${adjusted_revenue:.2f}M")

# -------------------------------
# 7. Motivational Button
# -------------------------------
if st.button("Show Motivation"):
    st.success("Keep pushing for growth! 🚀")
