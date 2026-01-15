import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Data Analytics", layout="wide")

st.title("📊 AI-Powered Data Analytics Chat App")
st.write("Upload a CSV file and explore your data.")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    st.subheader("📈 Basic Statistics")
    st.write(df.describe())
