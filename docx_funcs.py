import streamlit as st
import pandas as pd
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches
from datetime import date, datetime
from io import BytesIO
import os
import base64

from helpers import months, month_names_dict


def reorder_dataframe(df):
    # Reset index
    df = df.reset_index(drop=True)
    # Change order of columns
    column_order = ['total', 'End Hour', 'Start Hour', 'Comments', 'Date']
    df = df[column_order]
    # Rename columns to hebrew
    df.columns = ['סך הכל שעות', 'שעת סיום', 'שעת התחלה', '', 'תאריך']
    return df


def calc_total_hours(df):
    # Calculate total hours without modifying the DataFrame
    total_time = pd.to_timedelta(df['total'] + ':00').sum()  # Adds ":00" for seconds if necessary
    total_hours = total_time.total_seconds() / 3600  # Convert total seconds to hours
    return total_hours

def one_docx(df):

    title_text = ''
    month_list, year_list = months(df)
    month_dict = month_names_dict()

    if len(month_list) == 1:
        month_name = month_dict[str(month_list[0])]
        year = year_list[0]
        st.write(month_name)
        hebrew_text = 'דיווח שעות לחודש'
        title_text = f'{hebrew_text} {month_name} {year} '

    elif len(month_list) > 1:
        min_month = month_dict[str(month_list[0])]
        max_month = month_dict[str(month_list[-1])]
        hebrew_text = 'דיווח שעות לחודשים'
        if len(list(set(year_list))) == 1:
            year = year_list[0]
            title_text = f'{hebrew_text} {min_month}-{max_month} {year} '
        elif len(list(set(year_list))) > 1:
            title_text = f'{hebrew_text} {min_month}-{max_month} {year_list[0]}-{year_list[-1]} '

    total_hours = calc_total_hours(df)
    hebrew_total = 'סך שעות בדוח'
    total_hours_text = f'{hebrew_total} {total_hours} :'

    df = reorder_dataframe(df)

    # CREATE DOCUMENT
    document = Document()

    # Set RTL for the document
    section = document.sections[0]
    # Create bidi element if it doesn't exist
    bidi = OxmlElement('w:bidi')
    bidi.set(qn('w:val'), '1')
    section._sectPr.append(bidi)

    # Todays date in format dd/mm/yyyy
    today = date.today().strftime("%d/%m/%Y")

    # Add DATE to doc
    add_date = document.add_paragraph(today)
    # Set spacing after date paragraph
    add_date.paragraph_format.space_after = Pt(20)

    # Add SUBJECT
    add_subject = document.add_paragraph()
    add_subject.style = 'Heading1'
    add_subject.alignment = WD_ALIGN_PARAGRAPH.CENTER
    # Set RTL for this paragraph
    pPr = add_subject._element.get_or_add_pPr()
    bidi = OxmlElement('w:bidi')
    bidi.set(qn('w:val'), '1')
    pPr.append(bidi)
    # Add subject text
    add_subject.add_run(title_text)
    add_subject.paragraph_format.space_after = Pt(30)

    # Add TABLE
    table = document.add_table(rows=df.shape[0] + 1, cols=df.shape[1])
    table.style = 'Table Grid'
    # Add headers
    for j, column_name in enumerate(df.columns):
        cell = table.cell(0, j)
        cell.text = str(column_name)
        # Set RTL for header cells
        pPr = cell.paragraphs[0]._element.get_or_add_pPr()
        bidi = OxmlElement('w:bidi')
        bidi.set(qn('w:val'), '1')
        pPr.append(bidi)
    # Add data rows
    for i, row in df.iterrows():
        for j, value in enumerate(row):
            cell = table.cell(i + 1, j)
            cell.text = str(value)
            # Set RTL for each cell in the row
            pPr = cell.paragraphs[0]._element.get_or_add_pPr()
            bidi = OxmlElement('w:bidi')
            bidi.set(qn('w:val'), '1')
            pPr.append(bidi)

    # Add a space below the table
    document.add_paragraph()

    # Add TOTAL hours
    add_total_hours = document.add_paragraph()
    add_total_hours.style = 'Heading1'
    add_total_hours.alignment = WD_ALIGN_PARAGRAPH.LEFT
    # Set RTL for this paragraph
    pPr = add_total_hours._element.get_or_add_pPr()
    bidi = OxmlElement('w:bidi')
    bidi.set(qn('w:val'), '1')
    pPr.append(bidi)
    # Add subject text
    add_total_hours.add_run(total_hours_text)
    add_total_hours.paragraph_format.space_after = Pt(20)

    # Add BLESS
    add_bless = document.add_paragraph()
    add_bless.style = 'Heading2'
    add_bless.alignment = WD_ALIGN_PARAGRAPH.CENTER
    # Set RTL for this paragraph
    pPr = add_bless._element.get_or_add_pPr()
    bidi = OxmlElement('w:bidi')
    bidi.set(qn('w:val'), '1')
    pPr.append(bidi)
    # Add bless text
    add_bless.add_run('בברכה')
    add_bless.paragraph_format.space_after = Pt(20)

    # Add PICTURE
    # Get image from secrets
    encoded_image = os.getenv("BOOK_ID")
    image_path = "temp_image.png"

    # Decode the base64 image and save it temporarily
    with open(image_path, "wb") as f:
        f.write(base64.b64decode(encoded_image))

    # Add the image to the document
    document.add_picture(image_path)  # Specify width

    # Clean up the temporary image file
    os.remove(image_path)



    # Save the document in a BytesIO object
    buffer = BytesIO()
    document.save(buffer)
    buffer.seek(0)

    return buffer





