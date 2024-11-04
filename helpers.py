import streamlit as st


@st.dialog('Number of Docx')
def number_docx():
    docx_option = st.radio('Choose an option',
                           options=['One docx for all unreported hours',
                                    'One docx for each month'],
                           index=None)

    st.write(docx_option)
    if docx_option == 'One docx for all unreported hours':
        st.session_state['docx_option'] = 1
    elif docx_option == 'A docx for each month containing unreported hours':
        st.session_state['docx_option'] = 2
    st.write('---')
    submit = st.button('Submit')
    if submit:
        st.rerun()
