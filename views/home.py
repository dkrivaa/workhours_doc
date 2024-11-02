import streamlit as st
import os
from google_funcs import google_client, google_sheet_list

encoded_credentials = os.getenv("GOOGLE_CREDENTIALS_BASE64")
st.write(encoded_credentials)

# # Defining Google client and saving to session state
# google_client()
# # Getting client
# client = st.session_state['client']
# # Get list of sheets
# sheet_list = google_sheet_list()
#
# st.selectbox('Choose sheet', options=sheet_list, index=None)
