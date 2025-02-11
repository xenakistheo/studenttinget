import streamlit as st
import requests
import pandas as pd

FASTAPI_URL = "http://localhost:8000"

st.title("Search PDFs in Supabase")

query = st.text_input("Enter search term")

if st.button("Search"):
    response = requests.get(f"{FASTAPI_URL}/search_pdfs", params={"query": query})
    
    if response.status_code == 200:
        results = response.json().get("results", [])
        
        if results:
            st.subheader("Search Results:")
            df = pd.DataFrame(results)
            st.dataframe(df)
        else:
            st.write("No matches found.")
