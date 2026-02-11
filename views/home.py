import streamlit as st

from google_funcs import google_client, google_sheet_list, read_sheet, update_sheet
from docx_funcs import one_docx


# Defining Google client
google_client()
# Getting client
client = st.session_state['client']

# Get list of sheets
sheet_list = google_sheet_list()
# Choose one of sheets
sheet_name = st.selectbox('Choose sheet', options=sheet_list, index=None)

# Initialize variables
docx_buffer = None
# Initialize a flag in session_state to track download action
if "downloaded" not in st.session_state:
    st.session_state.downloaded = False

# Getting the data from relevant sheet that hasn't been reported
if sheet_name is not None:
    # Assign sheet_name to session_state
    st.session_state['sheet_name'] = sheet_name

    with st.container(border=True):
        st.subheader('Workhours to report:')
        df = read_sheet(sheet_name)

        # If there are hours to report
        if len(df) > 0:
            st.dataframe(df)
            st.write('---')
            prepare_one_docx = st.button('Prepare docx for all unreported hours')
            prepare_many_docx = st.button('Prepare docx for each month with unreported hours',
                                          disabled=True)
            st.write('---')
            # Check if "Prepare docx" button was clicked
            if prepare_one_docx:
                try:
                    # Generate document buffer
                    docx_buffer = one_docx(df)

                    # Ensure the buffer was created
                    if docx_buffer is not None:
                        st.download_button(
                            label="Download Word Document",
                            data=docx_buffer,
                            file_name="my_document.docx",
                            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                        )

                    else:
                        st.error("Failed to create document. `docx_buffer` is None.")

                except Exception as e:
                    # Log the exception if document creation fails
                    st.error(f"Error creating document: {e}")

                # Update Google sheet so unreported hours become reported
                new_df = update_sheet(sheet_name)

        # If there are no hours to report
        else:
            st.write(':blue[No Hours to report]')






