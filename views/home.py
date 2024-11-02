import streamlit as st

from google_funcs import google_client, google_sheet_list


# Defining Google client and saving to session state
google_client()
# Getting client
client = st.session_state['client']
# Get list of sheets
sheet_list = google_sheet_list()

st.selectbox('Choose sheet', options=sheet_list, index=None)
