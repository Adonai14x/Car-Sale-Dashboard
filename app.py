import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Car Sales - Dashboard")

# Load the dataset
df = pd.read_csv("vehicles_us.csv")

#Histogram
px.histogram(df)
st.plotly_chart(px.histogram(df, x='price', nbins=50), use_container_width=True)

#Sctter Plot
px.scatter(df)
st.plotly_chart(px.scatter(df, x='odometer', y='price', color='year', hover_data=['make', 'model']), use_container_width=True)

#Data Filtering
if st.checkbox()
    df = df[df]'odometer', y='price' < [100000, 50000, 20000, 10000]]
    st.write(df.head())

##Interactivity Checkbox
st.checkbox("Show Data", value=True)
st.write(df.head())