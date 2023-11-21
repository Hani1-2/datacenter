import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from mitosheet.streamlit.v1 import spreadsheet
import pygwalker as pyg
from dtale.views import startup

# Read the data
df = pd.read_csv("supermarket_sales - Sheet1.csv")

# Set the layout to wide
st.set_page_config(layout="wide")

# Custom Styling
st.markdown(
    """
    <style>
    .css-1sbuyq9 { /* Customize Streamlit main title font */
        font-family: 'Times New Roman', sans-serif !important;
        font-size: 2.5rem !important; /* Adjust font size as needed */
        color: #333333; /* Customize title color */
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Sidebar with tabs
selected_tab = st.sidebar.selectbox(
    "Select Tab",
    ["D-Tale Profiling Report", "Mito Sheet", "Pygwalker Analysis"]
)

# Main content
st.title("Data Analysis App")

# Introduction
st.write(
    "Welcome to the Data Analysis App! 📊🔍 Explore the power of data with these amazing tools."
)

# Profiling Report Tab
if selected_tab == "D-Tale Profiling Report":
    st.header("D-Tale Report")
    st.write(
        "Dive deep into your data with D-Tale! 🚀 Uncover hidden patterns, outliers, and insights. "
        "Visualize your data like never before and gain a comprehensive understanding of its structure."
    )
    
    # Use D-Tale to generate and display the report
    dtale_app = startup(data_id="1", data=df)
    components.html('<iframe src="/dtale/main/1" width="100%" height="600"></iframe>', height=600, scrolling=True)
    st.video("recording.mkv")

# Mito Sheet Tab
elif selected_tab == "Mito Sheet":
    st.header("Mito Sheet")
    st.write(
        "Mito Sheet brings your data to life! 🎨 Edit and interact with your dataset in a spreadsheet format. "
        "Effortlessly manipulate and explore your data, making analysis a breeze."
    )
    
    # Display the dataframe in a Mito spreadsheet
    final_dfs, code = spreadsheet(df)
    
    # Display the final dataframes created by editing the Mito component
    st.write(final_dfs)
    st.video("mito_sheet.mp4")

# Pygwalker Analysis Tab
elif selected_tab == "Pygwalker Analysis":
    st.header("Pygwalker Analysis")
    st.write(
        "Analyze your data with Pygwalker! 👣 Take a step-by-step journey through your dataset, "
        "exploring each feature and discovering valuable insights. Pygwalker makes data analysis an exciting adventure!"
    )
    
    # Generate the HTML using Pygwalker
    pyg_html = pyg.to_html(df)
    
    # Embed the HTML into the Streamlit app
    components.html(pyg_html, height=800, scrolling=True)
    st.video("pygwalker.mp4")
