from flask import Flask, request, jsonify
from algo.algorithm import chat_bot
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/request": {"origins": "*"}})


@app.route("/request", methods=["POST"])
def post_question():
    data = request.get_json()
    if "question" not in data:
        return jsonify({"error": "Missing 'question' parameter"}), 400
    question = data["question"]
    response = chat_bot(question)
    return jsonify(response)


@app.route("/hello", methods=["GET"])
def hello():
    return "hello"


if __name__ == "__main__":
    app.run()
