import streamlit as st

from google_funcs import google_client, google_sheet_list, read_sheet


# Defining Google client and saving to session state
google_client()
# Getting client
client = st.session_state['client']

# Get list of sheets
sheet_list = google_sheet_list()
# Choose one of sheets
sheet_name = st.selectbox('Choose sheet', options=sheet_list, index=None)
# Getting the data from relevant sheet that hasn't been reported
if sheet_name is not None:
    df = read_sheet(sheet_name)
    st.dataframe(df)

