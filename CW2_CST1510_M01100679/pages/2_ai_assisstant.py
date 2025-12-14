import streamlit as st
from openai import OpenAI
from services.auth_guard import require_login
require_login()# if not logged in no access
st.set_page_config(page_title="AI Assistant")

st.subheader(" AI Assistant")

# Creates a client object that will allow your app to send requests to OpenAI.
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Initialise session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system", # it tells the AI what kind of assistant it should be.
            "content": "You are an AI assistant helping users analyse datasets, cybersecurity incidents, and IT tickets."
        }
    ]

# Display previous chat messages
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# create a user input box
prompt = st.chat_input("Ask the AI about your data...")

if prompt:
    # Show user message in the chat interface
    with st.chat_message("user"):
        st.markdown(prompt)
   #Adds the user message to the messages list so the AI knows the chat history.
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Send message to OpenAI (streaming)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=st.session_state.messages,
        stream=True #allows the AI response to appear like real-time typing instead of waiting for the full answer.
    )

    # Display streaming response
    with st.chat_message("assistant"):
        container = st.empty()
        full_reply = ""
        for chunk in response:
            delta = chunk.choices[0].delta
            if delta.content:
                full_reply += delta.content
                container.markdown(full_reply)

    # Save assistant message to chat history
    st.session_state.messages.append({
        "role": "assistant",
        "content": full_reply
    })
