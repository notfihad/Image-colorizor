import streamlit as st
import requests
from io import BytesIO

# Set up the FastAPI URL for the colorization service
api_url = "http://localhost:8000/colorize"  # Ensure this matches your FastAPI server URL

# Streamlit UI
st.set_page_config(page_title="AI Image Colorizer", page_icon="🎨", layout="centered")

# Header and description
st.title("🎨 AI-Powered Image Colorizer")
st.markdown("""
    **Breathe new life into your black-and-white photos with AI colorization.**  
    This tool uses a state-of-the-art DeOldify model to add vibrant colors to your images.
    Just upload a black-and-white image, set a render factor, and let the AI work its magic!
""")

# File upload widget
uploaded_file = st.file_uploader("Upload your black-and-white image", type=["jpg", "jpeg", "png"])

# Model selection toggle
model_type = st.radio("Choose Colorization Model", ["Artistic", "Stable"], index=0)
use_artistic = model_type == "Artistic"

# Render factor input widget
render_factor = st.slider("Select Render Factor (1-50)", min_value=1, max_value=50, value=35, step=1)

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width="always")

    # Button to process the image
    if st.button("✨ Colorize Image"):
        files = {"image": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        data = {
            "render_factor": str(render_factor),
            "artistic": "true" if use_artistic else "false"
        }

        try:
            response = requests.post(api_url, files=files, data=data)

            if response.status_code == 200:
                colorized_image = response.content
                st.image(colorized_image, caption="Colorized Image", use_column_width="always")

                buffer = BytesIO(colorized_image)
                buffer.name = "colorized_image.png"

                st.download_button(
                    label="💾 Download Colorized Image",
                    data=buffer,
                    file_name="colorized_image.png",
                    mime="image/png"
                )
            else:
                st.error(f"Error: {response.json().get('error', 'Unknown error occurred.')}")
        except Exception as e:
            st.error(f"An error occurred while processing the image: {str(e)}")
else:
    st.info("Please upload an image to get started.")
