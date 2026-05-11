from flask import Flask, render_template, request, jsonify
from knapsack import fractional_knapsack

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calcular", methods=["POST"])
def calcular():
    data = request.get_json()
    capacity = float(data["capacity"])
    materials = data["materials"]

    for m in materials:
        m["stock"] = float(m["stock"])
        m["price_per_ton"] = float(m["price_per_ton"])

    selected, total_value = fractional_knapsack(capacity, materials)

    return jsonify({
        "selected": selected,
        "total_value": total_value,
        "total_weight": sum(s["taken"] for s in selected),
        "capacity": capacity,
    })


if __name__ == "__main__":
    app.run(debug=True)
