from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Server is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "").lower()

    if "hi" in message:
        reply = "Hello! I am Jarvis. How can I help you?"
    elif "how are you" in message:
        reply = "I am just code, but I am functioning perfectly!"
    elif "your name" in message:
        reply = "I am Jarvis, your AI assistant."
    else:
        reply = "Interesting... tell me more."

    return jsonify({"reply": reply})
