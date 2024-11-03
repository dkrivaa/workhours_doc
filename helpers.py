import streamlit as st


@st.dialog('Number of Docx')
def number_docx():
    docx_option = st.radio('Please choose an option',
                           options=['Prepare one report for all unreported hours ',
                                    'prepare separate report for each month'],
                           )
    submit = st.button('Submit')
    if submit:
        if docx_option == 0:
            return 0
        elif docx_option == 1:
            return 1
        st.rerun()

