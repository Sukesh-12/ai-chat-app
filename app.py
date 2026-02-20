import requests
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"

HF_TOKEN = os.environ.get("HF_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

@app.route("/")
def home():
    return "Server is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    payload = {
        "inputs": user_message
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        result = response.json()

        if isinstance(result, list) and len(result) > 0:
            reply = result[0].get("generated_text", "🤖")
        else:
            reply = "🤖"
    else:
        reply = "AI service error"

    return jsonify({"reply": reply})
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
