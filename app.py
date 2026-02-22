from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

@app.route("/")
def home():
    return "Server is running!"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_message = data.get("message", "")

        payload = {"inputs": user_message}

        response = requests.post(API_URL, headers=HEADERS, json=payload)

        print("HF STATUS:", response.status_code)
        print("HF RESPONSE:", response.text)

        if response.status_code != 200:
            return jsonify({"reply": "AI service error. Check token or model."})

        try:
            result = response.json()
        except:
            return jsonify({"reply": "Invalid response from AI service."})

        if "error" in result:
            return jsonify({"reply": "Model loading... please wait."})

        reply = result[0]["generated_text"]

        return jsonify({"reply": reply})

    except Exception as e:
        print("SERVER ERROR:", str(e))
        return jsonify({"reply": "Server error."})
