import streamlit as st
import requests

prompt = st.text_input("Type a message...")
if st.button("Send"):
    response = requests.post("https://api-cloud-g3-8a6978b4682d.herokuapp.com/")
    st.write(response.text)
                             