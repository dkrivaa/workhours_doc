import streamlit as st

from google_funcs import google_client, google_sheet_list, read_sheet


# Defining Google client and saving to session state
google_client()
# Getting client
client = st.session_state['client']

# Get list of sheets
sheet_list = google_sheet_list()

sheet_name = st.selectbox('Choose sheet', options=sheet_list, index=None)
st.write(sheet_name)
if sheet_name is not None:
    df = read_sheet(sheet_name)
    st.dataframe(df)
    st.write(df.dtypes)

