import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Image Colorization Tool", layout="centered")

# Title and description
st.title("AI-Powered Image Colorization Tool")
st.write("Upload a black-and-white image and enter a text prompt to guide the colorization.")

# Image Upload Component
uploaded_image = st.file_uploader("Upload your black-and-white image here", type=["jpg", "jpeg", "png"])

# Display uploaded image preview if available
if uploaded_image:
    st.image(Image.open(uploaded_image), caption="Uploaded Image", use_column_width=True)

# Prompt Input for User Text
prompt_text = st.text_input("Enter a description or specific colors to guide the colorization:")

# Placeholder button for triggering colorization (backend logic will be added later)
if st.button("Colorize Image"):
    if uploaded_image and prompt_text:
        st.write("Processing...")  # Temporary feedback while implementing backend
    elif not uploaded_image:
        st.error("Please upload an image.")
    elif not prompt_text:
        st.error("Please enter a colorization prompt.")

# Footer or instructions (if necessary)
st.write("Provide descriptive prompts such as 'sunset colors', 'vintage sepia', or 'realistic skin tones' to guide the AI.")
