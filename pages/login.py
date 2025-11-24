import streamlit as st
from pathlib import Path
import bcrypt

USER_FILE = "DATA/users.txt"

st.set_page_config(page_title="Login")

st.markdown("""
<style>
.stApp { background-color: #5C4033; color: #FFFDD0; }
</style>
""", unsafe_allow_html=True)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# Load users from users.txt so those only these can log in
def load_users():
    users = {}
    if Path(USER_FILE).exists():
        with open(USER_FILE, "r") as file:
            for line in file:
                username, hash_pw = line.strip().split(",")
                users[username] = hash_pw
    return users

# authenticate the user
def authenticate_user(username, password):
    users = load_users()

    if username in users:
        # Get the stored hashed password for this username and convert it to bytes
        stored_hash = users[username].encode("utf-8")
        # Check if the entered password matches the stored hashed password
        if bcrypt.checkpw(password.encode("utf-8"), stored_hash):
            st.session_state.logged_in = True
            st.success(f"Welcome {username}!")
            return

    st.error("Invalid username or password.")
    st.session_state.logged_in = False


#login tab
st.subheader("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")
# registering tab
if st.button("Register"):
   st.subheader("register")
   new_username = st.text_input("choose a new username")
   new_password = st.text_input("choose a password", type="password")
   confirm_new_password = st.text_input("confirm password", type="password")
   if not new_username or not new_password:
       st.warning("Please fill in all fields.")
   elif new_password != confirm_password:
       st.error("Passwords do not match.")
   elif new_username in st.session_state.users:
       st.error("Username already exists. Choose another one.")
   else:
       #hash the new password
       hashed_pw = bcrypt.hashpw(new_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

       # Append new users to users.txt
       with open(USER_FILE, "a") as file:
           file.write(f"{new_username},{hashed_pw}\n")

       st.success("Account created! You can now log in")
       st.info("Tip: go to the Login tab and sign in with your new account.")

if st.button("Login"):
    authenticate_user(username, password)
    st.switch_page("pages/1_Dashboard.py")


with st.expander("See details"):
    st.write("Login username and hashed password are stored in DATA/users.txt.")
