import streamlit as st
import google.generativeai as genai

genai.configure()

def get_gemini_models():
    gemini_models = []
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            gemini_models.append(model.name)
    return gemini_models

st.title('Google Gemini Models')
gemini_models = get_gemini_models()

default_index = gemini_models.index('/models/gemini-pro') if '/models/gemini-pro' in gemini_models else 0

selected_model = st.selectbox('Select a Gemini model:', gemini_models, index=default_index)