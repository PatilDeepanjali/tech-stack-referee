from flask import Flask, request, jsonify, send_from_directory
from referee.compare import compare_stacks
from referee.explain import generate_explanation

app = Flask(__name__, static_folder="web", static_url_path="")

@app.route("/")
def index():
    return send_from_directory("web", "index.html")

@app.route("/compare", methods=["POST"])
def compare():
    user_input = request.json
    result = compare_stacks(user_input)
    explanation = generate_explanation(result)
    return jsonify(explanation)

if __name__ == "__main__":
    app.run(debug=True)
