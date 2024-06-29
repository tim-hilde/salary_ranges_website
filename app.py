import streamlit as st
import requests

st.write("# Vorhersage von Gehaltsspannen im Data Science Bereich")

api_url = "http://127.0.0.1:8000"

input_txt = st.text_area("Füge hier den gesamten Text der Stellenausschreibung ein:")

if st.button("Vorhersagen!"):
    params = {
        "input": input_txt
    }

    prediction = requests.get(f"{api_url}/predict", params=params).json()
    range_min = prediction["range_min"]
    range_max = prediction["range_max"]

    st.write(f"## Gehaltsspanne: {range_min}.000€ - {range_max}.000€")
