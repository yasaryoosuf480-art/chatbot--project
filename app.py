from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"].lower()

    reply = """Initializing… ⚡
Connection established.
I am an AI system created by Yasar Yoosuf—ready to assist, answer, and adapt.

⚠️ This system is currently under development.
Responses to your input may not be available yet.

Thank you for your patience. 🚀"""

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)