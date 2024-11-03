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
            st.session_state['docx_option'] = 0
        if docx_option == 1:
            st.session_state['docx_option'] = 0
        st.rerun()

