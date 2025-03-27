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
    #return " Bonjour et bienvenue sur l'API de Viken !"
    # HTML pour le message de bienvenue avec du style et une image
    html_content = f"""
        <!DOCTYPE html>
        <html lang="fr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Bienvenue sur l'API</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f9;
                    text-align: center;
                    color: #333;
                }}
                .welcome-message {{
                    margin-top: 50px;
                    padding: 20px;
                    background-color: #4CAF50;
                    color: white;
                    border-radius: 10px;
                    font-size: 24px;
                }}
                img {{
                    max-width: 300px;
                    margin-top: 30px;
                    border-radius: 10px;
                }}
                .container {{
                    padding: 20px;
                    max-width: 800px;
                    margin: 0 auto;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="welcome-message">
                    <h1>Bonjour et bienvenue sur l'API de Viken !</h1>
                    <p>Cette API permet de prédire la classe d'une fleur d'Iris en fonction des caractéristiques de ses sépales et pétales.</p>
                </div>
                <!-- Utilisation de Flask pour servir l'image -->
                <img src="static/VKpic.jpg" alt="Logo ou image de l'API">
            </div>
        </body>
        </html>
        """
    return html_content

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
    # le code ci-dessous fonctionne pour lancement en local ou en mode service web avec plateforme cloud render
    port = os.getenv("PORT", 5000)
    app.run(host="0.0.0.0", port=port, debug=True)
