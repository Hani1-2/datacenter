import pandas as pd
import streamlit as st
from mitosheet.streamlit.v1 import spreadsheet

# Call set_page_config as the first Streamlit command
st.set_page_config(layout="wide")

# Create a dataframe with pandas (you can pass any pandas dataframe)
dataframe = pd.read_csv("PinellasCo_DailyAttendance_September2022.xlsx - Attendance.csv")

# Display the dataframe in a Mito spreadsheet
final_dfs, code = spreadsheet(dataframe)

# Display the final dataframes created by editing the Mito component
# This is a dictionary from dataframe name -> dataframe
st.write(final_dfs)
