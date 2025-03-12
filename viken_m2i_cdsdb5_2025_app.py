import os
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Charger le modèle et le scaler
model = joblib.load("knn_model.pkl")
scaler = joblib.load("scaler.pkl")

# Route pour la page d'accueil
@app.route("/", methods=["GET"])
def home():
    return "Bienvenue sur l'API !"

# Route pour la prédiction
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if "features" not in data:
        return jsonify({"error": "Données invalides, clé 'features' requise"}), 400

    features = np.array(data["features"]).reshape(1, -1)
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)

    return jsonify({"prediction": int(prediction[0])})


if __name__ == "__main__":
    port = os.getenv("PORT", 5000)
    app.run(host="0.0.0.0", port=port, debug=True)
