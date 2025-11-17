import streamlit as st
import pandas as pd
st.header("Muti-domain Intelligence Application")
st.subheader("welcome back!")


st.markdown("""
<style>
.stApp { background-color: #5C4033; color: #FFFDD0; }
</style>
""", unsafe_allow_html=True)
st.write(""" Here you can access your 4 databases one is the users one containing number of uses their names and their passwords the the cyber incident and there is also the dataset one and lastly the the the it tickets one. 
before we are just going to ask you to login cause these information can only be accessed by people who have access just to prevent unauthorised users 
to gain access to our data just to keep data integrity for our users. 
""")
st.caption("log in to access the data and start working ")

with st.expander("see app details"):
    st.write("this is a the welcome screen!")
    st.write("continue to see data ")

st.divider()
if st.button("click to go to the login page"):
    st.switch_page("../../pages/login.py")


