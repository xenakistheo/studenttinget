import streamlit as st
import requests
from datetime import datetime
import pandas as pd


YEAR = datetime.now().year

#Easter eggs
NS = "(\frac{\partial} {\partial t} + \mathbf{v} \cdot\nabla)\mathbf{v} = \frac{-\nabla p}{\rho} + \nu\nabla^2 \mathbf{v} + \mathbf{f}"
EULER = "e^{i\pi} + 1 = 0"

st.title("Studenttingets Vedtaksdatabase")

left_column, right_column = st.columns(2)

# Search input fields
keywords = st.text_input("Stikkord:")
casenr = st.text_input("Saksnummer:")
year = st.sidebar.multiselect("Årstall", ["Alle"] + list(range(1997,YEAR+1)))
title = st.text_input("Tittel inneholder:")
category = left_column.selectbox("Dokumenttype", ["Alle", "Plattform", "Resolusjon", "Høringssvar", "Enkeltvedtak"])
casetype = right_column.pills("Kategorier", ["Alle", "Valg", "Økonomi", "Plattform"])

archived = st.checkbox("Show archived legislations")


if st.button("Reset"):
    casenr = ""
    year = ["Alle"]
    title = ""
    category = "Alle"
    casetype = "Alle"
    keywords = ""
    archived = False




# Button to trigger the search
if st.button("Search"):

    FASTAPI_URL = "http://localhost:8000/cases/get_query"  # Change this as needed

    if title=="NavierStokes":
        st.markdown(NS)
    elif title=="Euler":
        st.latex(EULER)

    # Prepare query parameters
    year = None if "Alle" in year else ",".join(map(str, year))
    
    params = {
        "keywords": keywords if keywords else None,
        "casenr": casenr if casenr else None,
        "year": year if year else None,
        "title": title if title else None,
        "category": category if category != "Alle" else None,
        "casetype": casetype if casetype != "Alle" else None,
        #"archived": archived
    }
    
    # Remove any None values to keep the query clean
    params = {k: v for k, v in params.items() if v is not None}
    
    try:
        response = requests.get(FASTAPI_URL, params=params)
        #response = requests.get(FASTAPI_URL)
        response.raise_for_status()  # Raise an error for bad status codes
        results = response.json()
        if results:
            st.subheader("Results:")
            # Optionally, display results in a table format using pandas
            df = pd.DataFrame(results)
            st.dataframe(df)
        else:
            st.write("No legislations found with the given criteria.")
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")