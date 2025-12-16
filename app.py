import pandas as pd 
import streamlit as st
 # Sample data 
data = {'Product': ['A', 'B', 'C'], 'Sales': [1200, 850, 950], 'Customers': [300, 400, 350]}
df = pd.DataFrame(data) 
# Show data with Streamlit elements 
st.dataframe(df) # Interactive table -> data needs to exploration and larger 
st.data_editor(df) # Editable table
st.table(df) # Static table  -> no interactive <100 rows for displaying final result
# Customize columns directly in the dataframe display 
st.dataframe(df.style.format({'Sales': '${:,.0f}', 'Customers': '{:,.0f}'})) # sales will have dollar sign , customer will not have dollar sign


import streamlit as st
import pandas as pd 
import os 
# Get the current working directory 
current_directory = os.getcwd() 
 # Define the file path 
file_path = os.path.join(current_directory, 'winequality-red.csv') 
# Read the CSV file into a DataFrame df = pd.read_csv(file_path, delimiter=';')
 # Display the DataFrame in an interactive table
st.write("Wine Quality Data") 
st.dataframe(df)
