import streamlit as st


home_page = st.Page(
    page='views/home.py',
    title='Home',
    default=True
)

docx_page = st.Page(
    page='views/docx.py',
    title='Docx'
)


pg = st.navigation([home_page, docx_page], )

pg.run()

