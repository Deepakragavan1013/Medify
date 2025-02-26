import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template

# Configure Gemini API
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

genai.configure(api_key=API_KEY)

# Create the model
generation_config = {
    "temperature": 1.0,  # Adjusted for better response quality
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

# Flask App
app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze_sentiment():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Invalid request. Ensure Content-Type is application/json and a 'text' field is provided."}), 400

    user_input = data["text"].strip()

    if not user_input:
        return jsonify({"error": "Text input cannot be empty."}), 400

    try:
        chat_session = model.start_chat(history=[{"role": "user", "parts": [user_input]}])
        response = chat_session.send_message(user_input)
        sentiment = response.text.strip() if response.text else "Error analyzing sentiment"
    except Exception as e:
        sentiment = f"Error: {str(e)}"

    return jsonify({"sentiment": sentiment})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)