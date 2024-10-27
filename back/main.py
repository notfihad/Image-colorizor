# main.py

from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from pydantic import BaseModel
from typing import Optional
from PIL import Image
import io

app = FastAPI()

@app.post("/colorize")
async def colorize_image(image: UploadFile = File(...), prompt: Optional[str] = Form(None)):
    # Validate file type
    if not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an image file.")

    # Load image to confirm it is valid (optional, but good practice)
    try:
        img = Image.open(io.BytesIO(await image.read()))
        img.verify()  # Check if it is a valid image
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image file.")

    # Mock colorization process - in a real scenario, apply your colorization algorithm here
    colorized_image_url = "https://example.com/processed_image.png"  # Replace with actual URL if image is saved

    # Prepare response directly within the async function
    response = {
        "message": "Image colorization in progress. Download link will be available shortly.",
        "colorized_image_url": colorized_image_url
    }

    return response

