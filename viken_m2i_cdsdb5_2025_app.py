from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Charger le modèle et le scaler
model = joblib.load("knn_model.pkl")
scaler = joblib.load("scaler.pkl")


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
    app.run(debug=True)
