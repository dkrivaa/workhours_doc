import streamlit as st
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from datetime import date, datetime
from io import BytesIO

from helpers import months, month_names_dict

def one_docx(df):
    month_code = months(df)[0]
    month_dict = month_names_dict()
    month_name = month_dict[month_code]

    # Create Document
    document = Document()

    # Set RTL for the document
    section = document.sections[0]
    # Create bidi element if it doesn't exist
    bidi = OxmlElement('w:bidi')
    bidi.set(qn('w:val'), '1')
    section._sectPr.append(bidi)

    # Todays date in format dd/mm/yyyy
    today = date.today().strftime("%d/%m/%Y")

    # Add date to doc
    add_date = document.add_paragraph(today)
    # Set spacing after date paragraph
    add_date.paragraph_format.space_after = Pt(30)

    # Add subject
    add_subject = document.add_paragraph()
    add_subject.alignment = WD_ALIGN_PARAGRAPH.CENTER
    # Set RTL for this paragraph
    pPr = add_subject._element.get_or_add_pPr()
    bidi = OxmlElement('w:bidi')
    bidi.set(qn('w:val'), '1')
    pPr.append(bidi)

    # Add text
    add_subject.add_run(f'דיווח שעות לחודש {month_name}')  # "This is Arabic text"
    add_subject.space_after = Pt(12)


    # Save the document in a BytesIO object
    buffer = BytesIO()
    document.save(buffer)
    buffer.seek(0)
    return buffer





