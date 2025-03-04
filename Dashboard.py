import streamlit as st
import requests

# Configuration de la page
st.set_page_config(
    page_title="ChatBert",
    page_icon="🤖",
    layout="wide", # wide
)

st.title("ChatBert")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to call the API
def get_assistant_response(user_input):
    api_url = "https://api-cloud-g3-8a6978b4682d.herokuapp.com/"
    response = requests.post(api_url, json={"message": user_input})
    if response.status_code == 200:
        return response.json()
    else:
        return {"title": "Error", "image": "", "link": ""}

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant":
            columns1, columns2 = st.columns(2)
            with columns1:
                if message["content"][1]:  # Check if image exists
                    st.image(message["content"][1])
            with columns2:
                st.subheader(message["content"][0])
                st.link_button("Go to gallery", message["content"][2])
        else:
            st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Type a message..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get assistant response from API
    assistant_response = get_assistant_response(prompt)
    titre = assistant_response["title"]
    img = assistant_response["image"]
    link = assistant_response["link"]

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        col1, col2 = st.columns(2)
        with col1:  
            st.subheader(titre)
        with col2:
            if img:  # Check if image exists
                st.image(img)
            st.link_button("Go to gallery", link)

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": (titre, img, link)})