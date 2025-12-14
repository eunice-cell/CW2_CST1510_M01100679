import streamlit as st
import pandas as pd
import sqlite3
import os
from services.auth_guard import require_login
require_login()# if not logged in no access

st.set_page_config(page_title="1_Dashboard")

# creating the path using absolute path

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, "database", "intelligence_platform.db"))

# load the table

def load_table(table_name):
    try:
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Error reading {table_name}: {e}")
        return None

# show all tables in the database

def show_tables():
    conn = sqlite3.connect(DB_PATH )
    tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
    conn.close()
    return tables

# creating the dashboard user interface

st.title("Intelligence Platform Dashboard")
st.write("These are the database tables inside intelligence_platform.db")

st.subheader("Tables found in database:")
st.dataframe(show_tables())

st.divider()

st.subheader("Users")
st.dataframe(load_table("users"))

st.subheader("Cyber Incidents")
st.dataframe(load_table("cyber_incidents"))

st.subheader("Datasets Metadata")
st.dataframe(load_table("datasets"))

st.subheader("IT Tickets")
st.dataframe(load_table("tickets"))

# LOGOUT BUTTON
st.divider()
if st.button("Log out"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.info("Logged out.")
    st.switch_page("pages/login.py")
