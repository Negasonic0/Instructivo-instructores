from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "No se envió mensaje"}), 400
    

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # o usa "gpt-3.5-turbo" si quieres algo más barato
            messages=[
                {"role": "system", "content": "Eres un asistente experto en reglamentos académicos y disciplinarios del SENA."},
                {"role": "user", "content": user_message}
            ],
            temperature=0.5,
            max_tokens=500
        )
        reply = response.choices[0].message.content
        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
