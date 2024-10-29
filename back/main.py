import requests
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response

app = FastAPI()

COLAB_COLORIZE_URL = "https://3da7-34-16-197-118.ngrok-free.app/colorize"  # Replace with your actual ngrok URL

@app.post("/colorized")
async def colorize_image(file: UploadFile = File(...)):
    try:
        # Send the file to the Colab server
        files = {"image": (file.filename, await file.read(), file.content_type)}
        response = requests.post(COLAB_COLORIZE_URL, files=files)

        # Check for errors
        response.raise_for_status()

        # Return the image back to the client
        return Response(content=response.content, media_type="image/jpeg")

    except Exception as e:
        print(f"Error: {e}")
        return {"error": "Failed to process the image. Check server logs for details."}
