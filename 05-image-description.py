import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

genai.configure()
model = genai.GenerativeModel('gemini-pro-vision')

def generate_response(image_data):
    try:
        image = Image.open(io.BytesIO(image_data))
        response = model.generate_content(image)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

st.title('Gemini Pro Vision Image Captioning')
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

    if st.button('Generate'):
        generated_text = generate_response(uploaded_file.getvalue())
        st.write(generated_text)
else:
    st.write('Please upload an image file to generate content.')