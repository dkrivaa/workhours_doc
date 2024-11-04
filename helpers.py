import streamlit as st


def months(df):
    months_set = set()

    def row_month(date_str):
        # Parse the date parts from the string
        day, month, year = map(int, date_str.split("/"))
        return month

    for index, row in df.iterrows():
        month = row_month(row['date'])
        months_set.add(month)

    return months_set


def month_names_dict():
    return {
        '1': 'ינואר',
        '2': 'פברואר',
        '3': 'מרץ',
        '4': 'אפריל',
        '5': 'מאי',
        '6': 'יוני',
        '7': 'יולי',
        '8': 'אוגוסט',
        '9': 'ספטמבר',
        '10': 'אוקטובר',
        '11': 'נובמבר',
        '12': 'דצמבר',
    }


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
