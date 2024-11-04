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
    title_text = ''
    month_list, year_list = months(df)
    month_dict = month_names_dict()

    if len(month_list) == 1:
        month_name = month_dict[str(month_list[0])]
        year = year_list[0]
        st.write(month_name)
        hebrew_text = 'דיווח שעות לחודש'
        title_text = f'{hebrew_text} {month_name} {year}'

    elif len(month_list) > 1:
        min_month = month_dict[str(month_list[0])]
        max_month = month_dict[str(month_list[-1])]
        hebrew_text = 'דיווח שעות לחודשים'
        if len(list(set(year_list))) == 1:
            year = year_list[0]
            st.write(min_month, max_month)
            title_text = f'{hebrew_text}  {min_month}-{max_month} {year}'
        elif len(list(set(year_list))) > 1:
            title_text = f'{hebrew_text}  {min_month}-{max_month} {year_list[0]}-{year_list[-1]}'

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
    add_date.paragraph_format.space_after = Pt(20)

    # Add subject
    add_subject = document.add_paragraph()
    add_subject.alignment = WD_ALIGN_PARAGRAPH.CENTER
    # Set RTL for this paragraph
    pPr = add_subject._element.get_or_add_pPr()
    bidi = OxmlElement('w:bidi')
    bidi.set(qn('w:val'), '1')
    pPr.append(bidi)

    # Add text
    add_subject.add_run(title_text)
    add_subject.space_after = Pt(20)


    # Save the document in a BytesIO object
    buffer = BytesIO()
    document.save(buffer)
    buffer.seek(0)

    return buffer





