import streamlit as st
import pandas as pd

st.title("Login Anomaly Detection System")

@st.cache_data
def load_data():
    return pd.read_csv("top_alerts.csv")

data = load_data()

st.write("Top Alerts")
st.dataframe(data)

user = st.text_input("Enter User ID")

if user:
    filtered = data[data["User ID"].astype(str) == user]
    st.write(filtered)