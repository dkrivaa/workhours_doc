import os
import json
import base64
from google.oauth2.service_account import Credentials
import gspread
import pandas as pd
import streamlit as st


# Defining Google client and saving to session state
def google_client():
    # Get the Base64-encoded secret from the environment variable
    encoded_credentials = os.getenv("GOOGLE_CREDENTIALS_BASE64")
    # Decode it back to JSON format
    decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8")
    # Load the credentials as a dictionary
    creds_dict = json.loads(decoded_credentials)
    # Define scope
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    # Authenticate using the credentials dictionary and defined scopes
    creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
    # Connect to the Google Sheets API
    client = gspread.authorize(creds)
    # Save client to session state
    st.session_state['client'] = client


# Getting list of all sheets
def google_sheet_list():
    client = st.session_state['client']
    book_id = os.getenv("BOOK_ID")
    book = client.open_by_key(book_id)

    return [sheet.title for sheet in book.worksheets()]


def read_sheet(sheet_name):
    # Getting Google spreadsheet (book)
    client = st.session_state['client']
    book_id = os.getenv("BOOK_ID")
    book = client.open_by_key(book_id)
    # Reading data from relevant sheet
    sheet = book.worksheet(sheet_name)
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    df = df[df['reported'] != 1]

    return df
