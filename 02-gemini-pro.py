import streamlit as st
import google.generativeai as genai

genai.configure()
model = genai.GenerativeModel('gemini-pro')

st.title("Gemini Chat Interface")

user_input = st.text_input("Enter your question or statement:", value="Explain computer to a 2 year old")

if st.button('Send'):
    if 'chat' not in st.session_state:
        st.session_state.chat = model.start_chat(history=[])

    response = st.session_state.chat.send_message(user_input)
    response_text = response.text if hasattr(response, 'text') else str(response)
    st.write("AI Response: ", response_text)