import streamlit as st

def require_login():
    """
    Redirects users to login page if they are not authenticated.
    """
    if "logged_in" not in st.session_state or not st.session_state.logged_in:
        st.warning("Please log in to access this page.")
        st.switch_page("pages/login.py")
        st.stop()
