import streamlit as st
import pandas as pd
import sqlite3
import os

st.set_page_config(page_title="Dashboard")


# 1. USE ABSOLUTE PATH

databaseLoc = r"C:\Users\HP\PycharmProjects\CW2_CST1510_M01100679\DATA\intelligence_platform.db"

st.write("DB Exists:", os.path.exists(databaseLoc))

# LOAD TABLE

def load_table(table_name):
    try:
        conn = sqlite3.connect(databaseLoc)
        df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        conn.close()
        return df
    except Exception as e:
        st.error(f"Error reading {table_name}: {e}")
        return None

# SHOW ALL TABLES IN THE DATABASE
def show_tables():
    conn = sqlite3.connect(databaseLoc)
    tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
    conn.close()
    return tables

# DASHBOARD UI
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
