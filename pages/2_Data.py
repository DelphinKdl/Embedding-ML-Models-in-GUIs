#libraries
import streamlit as st
import pandas as pd

st.title("Data Page")

#load data
@st.cache_data(persist=True)
def load_data():
    data = pd.read_csv()
    return data

st.dataframe(load_data())
    
