import streamlit as st
import google.generativeai as genai

genai.configure()
model = genai.GenerativeModel('gemini-pro')

st.title("Prompt Embedding")

user_input = st.text_input("Enter your question or statement:", value="Explain computer to a 2 year old")

if st.button('Show Embeddings'):
    result = genai.embed_content(
        model="models/embedding-001",
        content=[user_input],
        task_type="retrieval_document",
        title="Embedding of Prompt")

    for v in result['embedding']:
        st.write(str(v)[:50], '... TRIMMED ...')