import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib

# Charger les données
iris = load_iris()
X, y = iris.data, iris.target

# Séparer les données en train et test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardisation des données
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Entraîner le modèle KNN
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Évaluer les performances
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

#penser à rajouter avec l'entrainement et la séparation du modèle
# ajouter des courbes illustrant les métriques et mes soavegarder dans mon projet sous forme png
# tester aussi si c'est du surapprentissage

# Sauvegarde du modèle et du scaler
joblib.dump(model, "knn_model.pkl")
joblib.dump(scaler, "scaler.pkl")

