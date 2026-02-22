from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)

# Get Gemini API key from Render environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Load model
model = genai.GenerativeModel("gemini-1.5-flash-latest")

@app.route("/")
def home():
    return "Jarvis AI Server is running!"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({"reply": "Please send a message."})

        # Generate AI response
        response = model.generate_content(user_message)

        return jsonify({"reply": response.text})

    except Exception as e:
        print("SERVER ERROR:", str(e))
        return jsonify({"reply": "AI service error."})
