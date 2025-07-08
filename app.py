from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__)

# 💡 Pre-set your token here or via environment variable
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN") or "your_token_here"
ENDPOINT = "https://models.github.ai/inference/chat/completions"
MODEL = "openai/gpt-4.1"

chat_history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global chat_history

    data = request.get_json()
    user_message = data.get("message", "")

    if not GITHUB_TOKEN:
        return jsonify({"reply": "❌ Error: Token is missing."}), 401

    chat_history.append({"role": "user", "content": user_message})

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GITHUB_TOKEN}"
    }

    payload = {
        "model": MODEL,
        "messages": chat_history,
        "temperature": 1.0,
        "top_p": 1.0
    }

    try:
        response = requests.post(ENDPOINT, headers=headers, json=payload)
        response.raise_for_status()
        reply = response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        reply = f"❌ Error: {str(e)}"

    chat_history.append({"role": "assistant", "content": reply})
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
