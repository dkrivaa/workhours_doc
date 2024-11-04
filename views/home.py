import streamlit as st

from google_funcs import google_client, google_sheet_list, read_sheet
from docx_funcs import one_docx


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
    with st.container(border=True):
        st.subheader('Workhours to report:')
        df = read_sheet(sheet_name)

        if len(df) > 0:
            st.dataframe(df)
            st.write('---')
            prepare_one_docx = st.button('Prepare a Docx for all unreported hours')
            prepare_many_docx = st.button('Prepare docx for each month with unreported hours')

            if prepare_one_docx:
                one_docx(df)

        else:
            st.write(':blue[No Hours to report]')






