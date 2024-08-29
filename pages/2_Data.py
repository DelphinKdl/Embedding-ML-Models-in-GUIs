#libraries
import streamlit as st
import pandas as pd


st.title("Customer Churn data")

# Load data with caching and type conversion
def load_data():
    data = pd.read_excel('data/Telco-churn-last-2000.xlsx')
    data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
    return data

st.dataframe(load_data())

