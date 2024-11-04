import streamlit as st


def months(df):
    months_list = []
    year_list = []

    def row_month(date_str):
        # Parse the date parts from the string
        day, month, year = map(int, date_str.split("/"))
        return month, year

    for index, row in df.iterrows():
        month, year = row_month(row['Date'])
        months_list.append(month)
        year_list.append(year)

    return months_list, year_list


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

