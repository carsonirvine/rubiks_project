from flask import Flask, render_template, request, jsonify
from Solvers.blind_solver import Blind_Solver

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
    # Fails if scramble is invalid
    try:
        output = solver.solve()
    # catch invalid scramble and output scramble outline
    except:
        output = "Invalid scramble, can only include:\
        \n1. Normal moves like F, R', U2\
        \n2. Wide moves like Lw, Rw', Uw2\
        \n3. Rotations like X, Z', Y2\
        \n(Solution will result in incorrect centers)\
        \n4. Center moves like M, E', S2\
        \n(Solution will result in incorrect centers)"

    return jsonify({"result": output})

if __name__ == "__main__":

    port = 5000
    
    app.run(port = port, debug=True)