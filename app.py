import streamlit as st
import pandas as pd
import plotly.express as px
st.title("📊 Data Sweeper App")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
     df = pd.read_csv(uploaded_file)
     st.write("### Raw Data", df)

# Simple Plotly Chart
     st.write("### Data Visualization")

     fig = px.histogram(df, x=df.columns[0]) # Histogram for first column
     st.plotly_chart(fig)
else:
     st.warning("CSV file is empty. Please upload a valid CSV file.")