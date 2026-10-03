from status_checker.check_status import check_status
import streamlit as st

# Correct Streamlit text input syntax
st.title("Status Checker")
url = st.text_input("Enter the url")

if url:
    st.write(f"You entered: {url}")

    status_code = check_status(url)

    if status_code == 200:
        st.success('website is up.')
    else:
        st.error('website is down.')
