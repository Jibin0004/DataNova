from flask import Flask, request, jsonify, render_template
from PIL import Image
import base64
import io
import google.generativeai as genai

# 🔑 Use your Google API Key here
# Replace with your actual key
GOOGLE_API_KEY = "AIzaSyBMSfuMK8d992t6pMp5HDaMprI5_EM1IX4"

# Init Gemini with the correct API key
genai.configure(api_key=GOOGLE_API_KEY)

# Use a currently available and supported multimodal model
# `gemini-pro-vision` is deprecated, using `gemini-1.5-flash` instead
model = genai.GenerativeModel('gemini-2.5-flash')

app = Flask(__name__)

@app.route('/')
def index():
    """Serves the main HTML page."""
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_image():
    """Handles the image capture and processing request."""
    try:
        # Get the JSON data from the request
        data = request.get_json()
        
        # Extract and decode the base64 image data
        image_data = data['image'].split(',')[1]
        image_bytes = base64.b64decode(image_data)
        
        # Open the image using the Pillow library
        image = Image.open(io.BytesIO(image_bytes))

        # Convert the PIL image to bytes in PNG format for Gemini
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        # Prompt Gemini to solve the aptitude question from the image
        response = model.generate_content(
            [
                "You are an aptitude solving assistant. Extract the question from the image and give a clear answer. If it's a math problem, provide the final answer and a step-by-step solution.",
                {
                    "mime_type": "image/png",
                    "data": img_byte_arr
                }
            ]
        )
        answer = response.text
    except Exception as e:
        # Return a helpful error message if something goes wrong
        answer = f"Error: {str(e)}"

    return jsonify({'answer': answer})

if __name__ == '__main__':
    # Run the Flask app
    # host='0.0.0.0' makes the server publicly accessible on your network (useful for mobile testing)
    app.run(debug=True, host='0.0.0.0')