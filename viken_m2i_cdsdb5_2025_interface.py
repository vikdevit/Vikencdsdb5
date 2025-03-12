import streamlit as st
import requests

st.title("Prédiction de la fleur d'Iris")

sepal_length = st.slider("Longueur du sépale", 4.0, 8.0, 5.1)
sepal_width = st.slider("Largeur du sépale", 2.0, 4.5, 3.5)
petal_length = st.slider("Longueur du pétale", 1.0, 7.0, 1.4)
petal_width = st.slider("Largeur du pétale", 0.1, 2.5, 0.2)

if st.button("Prédire"):
    input_data = {"features": [sepal_length, sepal_width, petal_length, petal_width]}
    # ligne ci-dessous utilisée si déploiement en local sans Render
    #response = requests.post("http://127.0.0.1:5000/predict", json=input_data)
    response = requests.post("https://viken-cdsdm2i-bloc5-2025-api-flask.onrender.com/predict", json=input_data)

    if response.status_code == 200:
        st.write(f"Classe prédite : {response.json()['prediction']}")
    else:
        st.write("Erreur lors de la prédiction")
