import streamlit as st
import requests

# Funktion zur Vorhersage des Gehaltsbereichs
def get_salary_prediction(job_description, api_url):
    params = {"input": job_description}
    response = requests.get(f"{api_url}/predict", params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# API-URL
api_url = "https://salary-ranges-api-zk7itojyoa-ew.a.run.app"

# Seitenlayout
st.set_page_config(
    page_title="Gehaltsspannen Vorhersage",
    page_icon=":chart_with_upwards_trend:",
    layout="centered",
)

# Seitentitel und Einleitung
st.title("Vorhersage von Gehaltsspannen im Data Science Bereich")
st.write(
    """
    Willkommen auf der Vorhersageplattform für Gehaltsspannen.
    Fügen Sie unten den Text der Stellenausschreibung ein, und wir sagen Ihnen die Gehaltsspanne voraus.
    """
)

# Benutzerinput
st.header("Stellenausschreibung")
input_txt = st.text_area("Fügen Sie hier den gesamten Text der Stellenausschreibung ein:", height=250)

# Schaltfläche für Vorhersage
if st.button("Vorhersagen!"):
    if input_txt.strip() == "":
        st.error("Bitte geben Sie eine gültige Stellenausschreibung ein.")
    else:
        with st.spinner("Vorhersage wird berechnet..."):
            prediction = get_salary_prediction(input_txt, api_url)
            if prediction:
                range_min = prediction["range_min"]
                range_max = prediction["range_max"]
                st.success(f"## Gehaltsspanne: {range_min}.000€ - {range_max}.000€")
            else:
                st.error("Fehler bei der Vorhersage. Bitte versuchen Sie es später erneut.")

# Styling mit CSS
st.markdown(
    """
    <style>
    .reportview-container {
        background: #f0f2f6;
    }
    .stTextArea textarea {
        background: #ffffff;
        border-radius: 8px;
    }
    .stButton button {
        background: #4caf50;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
