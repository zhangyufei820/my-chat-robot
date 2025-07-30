import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


# 初始化 Gemini API
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("请设置 GEMINI_API_KEY 环境变量。")

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")
    if not message:
        return jsonify({"error": "消息不能为空"}), 400

    try:
        response = model.generate_content(message)
        reply = response.text if hasattr(response, "text") else response.parts[0].text
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)










