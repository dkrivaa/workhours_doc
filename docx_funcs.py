import streamlit as st
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from datetime import date, datetime
from io import BytesIO

def one_docx(df):
    # Create Document
    document = Document()

    # Set RTL for the document
    section = document.sections[0]
    section._sectPr.xpath('./w:bidi')[0].set(qn('w:val'), '1')

    # Todays date in format dd/mm/yyyy
    today = date.today().strftime("%d/%m/%Y")

    # Add date to doc
    add_date = document.add_paragraph(today)
    add_date.space_after = Pt(20)

    # Add subject
    add_subject = document.add_paragraph('הנדון: דיווח')
    add_subject.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_subject._p.get_or_add_pPr().set(qn('w:bidi'), '1')

    # Save the document in a BytesIO object
    buffer = BytesIO()
    document.save(buffer)
    buffer.seek(0)
    return buffer


def download_docx():
    pass



