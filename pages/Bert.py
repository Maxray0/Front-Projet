import streamlit as st
import requests

prompt = st.text_input("Type a message...")

data =  {
    "text" : prompt+"[MASK]",
    "top_k" : 5
}
if st.button("Send"):
    response = requests.post("https://api-cloud-g3-8a6978b4682d.herokuapp.com/fill_mask", json=data)
    st.write(response.text)
                             