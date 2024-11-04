import streamlit as st
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from datetime import date, datetime

def one_docx(df):
    # Create Document
    document = Document()
    # Todays date in format dd/mm/yyyy
    today = date.today().strftime("%d/%m/%Y")
    # Adding date to doc
    add_date = document.add_paragraph(today)
    document.save('test.docx')



