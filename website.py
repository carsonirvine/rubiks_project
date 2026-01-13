from flask import Flask, render_template, request, jsonify
from blind_solver import Blind_Solver

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("webpage.html")

@app.route("/solve", methods=["POST"])
def solve():
    data = request.json
    if not data:
        return jsonify({"error": "JSON missing"}), 400
    elif "mode" not in data:
        return jsonify({"error": "mode missing"}), 400
    elif "scramble" not in data:
        return jsonify({"error": "data missing"}), 400
    

    mode = data["mode"]
    scramble = data["scramble"]

    solver = Blind_Solver(mode, scramble)
    output = solver.solve()

    return jsonify({"result": output})

if __name__ == "__main__":
    app.run(debug=True)