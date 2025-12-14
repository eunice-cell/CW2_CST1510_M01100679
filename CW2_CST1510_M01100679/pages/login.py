import streamlit as st
from services.database_manager import DatabaseManager
from services.auth_manager import AuthManager

st.set_page_config(page_title="Login")
DB_PATH = r"C:\Users\HP\PycharmProjects\CW2_CST1510_M01100679\database\intelligence_platform.db"

db = DatabaseManager(DB_PATH)
auth = AuthManager(db)
#logging in first
if "auth_error" in st.session_state:
    st.warning(st.session_state.auth_error)
    del st.session_state.auth_error

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None

st.markdown("""
<style>
.stApp { background-color: #5C4033; color: #FFFDD0; }
</style>
""", unsafe_allow_html=True)

st.title("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    user = auth.login_user(username, password)

    if user:
        st.session_state.logged_in = True
        st.session_state.user = user
        st.success(f"Welcome {user.get_username()}!")
        st.switch_page("pages/1_Dashboard.py")
    else:
        st.error("Invalid username or password")

st.divider()
st.subheader("Register")

new_username = st.text_input("New username")
new_password = st.text_input("New password", type="password")
confirm_password = st.text_input("Confirm password", type="password")

if st.button("Register"):
    if not new_username or not new_password:
        st.warning("Fill all fields")
    elif new_password != confirm_password:
        st.error("Passwords do not match")
    else:
        success = auth.register_user(new_username, new_password)
        if success:
            st.success("Account created! You can now log in.")
        else:
            st.error("Username already exists")
