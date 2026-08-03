from flask import Flask, jsonify

app = Flask(__name__)

NOMBRE = "David Fabro"
CANCION_FAVORITA = "Gladiador - Eladio Carrion"


@app.route("/api/favorito", methods=["GET"])
def favorito():
    return jsonify({
        "Nombre": NOMBRE,
        "Cancion Favorita": CANCION_FAVORITA
    })


@app.route("/", methods=["GET"])
def home():
    return jsonify({"mensaje": "API activa. Consulta /api/favorito"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
