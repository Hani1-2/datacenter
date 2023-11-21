import pandas as pd
from dataprep.eda import create_report
import streamlit as st
import tempfile

# Load your dataset
df = pd.read_csv('PinellasCo_DailyAttendance_September2022.xlsx - Attendance.csv')

# Generate a report using the create_report() function
report = create_report(df, title='My Report')

# Export the report to HTML
temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.html')
report.save(temp_file.name)

# Display the HTML report using an iframe
st.title('DataPrep Report Analysis')
st.components.v1.html(temp_file, width=None, height=None, scrolling=False)
# st.markdown(f'<iframe src="{temp_file.name}" width="100%" height="600"></iframe>', unsafe_allow_html=True)