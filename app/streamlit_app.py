import streamlit as st
import requests

st.title("Autonomous LLM Data Analyst")

file = st.file_uploader("Upload your csv file")

if file:
    st.write("Analyzing your data...")
    response = requests.post("http://localhost:8000/analyze/", files={"file": file})
    result = response.json()

    st.subheader("Insights")
    st.markdown(result["insights"])

    st.subheader("Code Snippets")
    st.code(result["code_snippets"], language = "python")