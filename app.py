import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import os

st.title('Hello, Students!')
st.write('This is your Python Programming course.')

with st.sidebar:
    selected=option_menu(
        menu_title = "Menu",
        options = ["ISOM3400", "About", "Contact"],
        icons = ["house","cloud-upload","list-task"],
        menu_icon= "cast",
        default_index=0,
    )

if selected == "ISOM3400":
    st.title(f"Welcome to the {selected} page.")

if selected == "About":
    st.title(f"Welcome to the {selected} page.")

if selected == "Contact":
    st.title(f"Welcome to the {selected} page.")

# Get the current working directory
current_directory = os.getcwd()
# Define the file path
file_path = os.path.join(current_directory, 'winequality-red.csv')

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path, delimiter=';')

# Display the DataFrame in an interactive table
st.write("Wine Quality Data")
st.dataframe(df)
