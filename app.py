from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"].lower()

    if user_message == "hello":
        reply = "Hi there!"
    elif user_message == "how are you":
        reply = "I'm doing great!"
    elif user_message == "bye":
        reply = "Goodbye!"
    else:
        reply = "I don't understand that."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
