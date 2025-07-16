# Déploiement d'une API de machine learning avec Flask, Streamlit et Render.

Ce projet implémente une API **Flask** pour déployer un modèle de machine learning (KNN) capable de prédire la classe d'une fleur d'Iris en fonction de ses caractéristiques.  
Une interface utilisateur via un navigateur web a aussi été développée avec **Streamlit**.  
L'API et l'interface sont ensuite hebergées sur la plateforme de cloud computing **Render** pour pouvoir être accessibles par n'importe quel utilisateur sur internet.

Ci-dessous lien vidéo de présentation du projet
https://1drv.ms/v/c/1e2a60e1c2caff68/EWvJuW1dXw5Hj0mL9dkqix4BGz_qL3rI8HihHaFFv6vwfg?e=LHYokR

## Prérequis
Créer un environnement virtuel avec **Python 3.11.9** et les dépendances suivantes pouvant être sauvegardées dans un fichier.txt puis installées avec pip depuis un terminal sous un IDE comme ***PyCharm***:
```
altair==5.5.0
attrs==25.1.0
blinker==1.9.0
cachetools==5.5.2
certifi==2025.1.31
charset-normalizer==3.4.1
click==8.1.8
colorama==0.4.6
Flask==3.1.0
gitdb==4.0.12
GitPython==3.1.44
gunicorn==23.0.0
idna==3.10
itsdangerous==2.2.0
Jinja2==3.1.5
joblib==1.4.2
jsonschema==4.23.0
jsonschema-specifications==2024.10.1
markdown-it-py==3.0.0
MarkupSafe==3.0.2
mdurl==0.1.2
narwhals==1.27.1
numpy==2.2.3
packaging==24.2
pandas==2.2.3
pillow==11.1.0
protobuf==5.29.3
pyarrow==19.0.1
pydeck==0.9.1
Pygments==2.19.1
python-dateutil==2.9.0.post0
pytz==2025.1
referencing==0.36.2
requests==2.32.3
rich==13.9.4
rpds-py==0.23.0
scikit-learn==1.6.1
scipy==1.15.2
six==1.17.0
smmap==5.0.2
streamlit==1.42.2
tenacity==9.0.0
threadpoolctl==3.5.0
toml==0.10.2
tornado==6.4.2
typing_extensions==4.12.2
tzdata==2025.1
urllib3==2.3.0
watchdog==6.0.0
Werkzeug==3.1.3
```
## Structure du Projet
Le dossier du projet respectera l'arborescence ci-dessous :
```
/
│── viken_m2i_cdsdb5_2025_app.py                # Code pour l'API Flask
│── viken_m2i_cdsdb5_2025_interface.py          # Code pour l'interface utilisateur Streamlit
│── viken_m2i_cdsdb5_2025_train_model.py        # Script d'entraînement du modèle de prédiction de la fleur d'Iris
│── knn_model.pkl                               # Modèle de prédiction sauvegardé
│── scaler.pkl                                  # Scaler sauvegardé pour normaliser les données lors de la prédiction de la même manière que celles utilisées à l'entraînement
│── static/
│   └── VKpic.jpg                               # Photo d'illustration de la page web d'accueil de l'API 
│── images/
│   └── iris.jpg                                # Photo d'illustration de la page web de l'interface utilisateur
│── dependances_projet_b5.txt                   # Liste des dépendances
│── viken_m2i_cdsdb5_2025_README.md             # Documentation du projet
```

## Utilisation

### 1. Entraînement du Modèle
Lancer le script viken_m2i_cdsdb5_2025_train_model.py pour générer les fichiers `knn_model.pkl` et `scaler.pkl`.

### 2. Lancement et test de l'API Flask en local
#### a-ouvrir un premier terminal sous PyCharm et écrire:

```bash
python .\viken_m2i_cdsdb5_2025_app.py
```
<u>Résultat attendu:</u>
```
 * Serving Flask app 'viken_m2i_cdsdb5_2025_app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with watchdog (windowsapi)
 * Debugger is active!
 * Debugger PIN: 276-960-467
127.0.0.1 - - [21/Feb/2025 10:04:33] "POST /predict HTTP/1.1" 200 -
```
#### b-ouvrir un deuxième terminal sous PyCharm et écrire:
```bash
Invoke-WebRequest -Uri http://127.0.0.1:5000/predict -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"features": [5.1, 3.5, 1.4, 0.2]}'
```
<u>Résultat attendu:</u>
```
StatusCode        : 200
StatusDescription : OK
Content           : {
                      "prediction": 0
                    }

RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 22
                    Content-Type: application/json
                    Date: Fri, 21 Feb 2025 09:04:33 GMT
                    Server: Werkzeug/3.1.3 Python/3.11.9

                    {
                      "prediction": 0
                    }

Forms             : {}
Headers           : {[Connection, close], [Content-Length, 22], [Content-Type, application/json], [Date, Fri, 21 Feb 2025 09:04:33 GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 22
```

### 3. Dépôt distant ***Github***
Créer un dépôt sous ***Github*** puis transférer depuis ***Pycharm*** avec ***Git*** l'ensemble des fichiers du projet.

### 4. Déploiement de l'API et de l'interface utilisateur sur ***Render***
#### a-Se connecter à Render avec https://render.com
Créer un compte en s'identifiant avec son compte ***Github***.  
Choisir le profil student.

#### b-Créer un service web pour l'api flask
-Cliquer sur Create Web Service  
-Choisir le langage Python  
-Nom du service (ici): 
```bash
viken-cdsdm2i-bloc5-2025-api-flask
```  
-Region : Frankfurt (EU Central)  
-Indiquer l'url du repository où sont hébergés les scripts et leurs dépendances (ici):  
```bash
https://github.com/vikdevit/Vikencdsdb5  
```  
-Indiquer le nom de la branche (ici):
```bash
master
```  
-Renseigner pour build command: 
```bash
pip install -r dependances_projet_b5.txt  
``` 
-Renseigner pour start command: 
```bash
gunicorn viken_m2i_cdsdb5_2025_app:app 
``` 
  
-Pour l'auto-déploiement suite à push des commits ***Git*** vers ***Github*** choisir Yes (les services se mettent automatiquement à jour).  
-Pour tester cliquer sur Start service et ouvrir une page html avec l'url:
```bash
https://viken-cdsdm2i-bloc5-2025-api-flask.onrender.com
``` 
-Suivre les logs dans la rubrique Monitor/logs et la rubrique Events qui permet aussi de suivre le déploiement des commits.  

<u>Remarque:</u>  
-En cas de mise à jour du code via ***Git/Github*** laisser ***Render*** déployer les commit en suivant la rubrique Event
(possibilité d'arrêter le service puis de déclencher manuellement le commit puis de relancer le service après la fin du déploiement).

#### c-Créer un service web pour l'interface utilisateur Streamlit

-Cliquer sur Create Web Service  
-Choisir le langage Python  
-Nom du service : 
```bash
viken-cdsdm2i-bloc5-2025-interface-streamlit
``` 
-Region : Frankfurt (EU Central)  
-Indiquer l'url du repository où sont hébergés les scripts et leurs dépendances (ici):  
```bash
https://github.com/vikdevit/Vikencdsdb5)  
``` 
-Indiquer le nom de la branche (ici):
```bash
master  
``` 
-Renseigner pour build command: 
```bash
pip install -r dependances_projet_b5.txt
``` 
-Renseigner pour start command: 
```bash
streamlit run viken_m2i_cdsdb5_2025_interface.py --server.port $PORT --server.address 0.0.0.0
``` 
-Pour l'auto-déploiement suite à push des commits ***Git*** vers ***Github*** choisir Yes (les services se mettent automatiquement à jour).  
-Pour tester cliquer sur Start service et ouvrir une page html avec l'url:
```bash
https://viken-cdsdm2i-bloc5-2025-interface.onrender.com
``` 
-Suivre les logs dans la rubrique Monitor/logs  et la rubrique Events qui permet aussi de suivre le déploiement des commits.  

<u>Remarques:</u>   
-En cas de mise à jour du code via ***Git/Github*** laisser ***Render*** déployer les commit en suivant la rubrique Event.  
(possibilité d'arrêter le service puis de déclencher manuellement le commit puis de relancer le service après la fin du déploiement)  
-Arrêter les services si non utilisés pour ne pas atteindre la limite maximum mensuelle liée au profil student de ***Render***.  
-Si besoin d'utilisation, activer les deux services ("Resume Web Service" dans la rubrique Settings du service, pas besoin de cliquer sur Restart service en haut à droite dans la rubrique Event).  
-La relance des services se fait après s'être reconnecté à ***Render*** avec ses identifiants ***Github*** via:
```bash
https://dashboard.render.com/login
```
(patienter quelques minutes après avoir relancé les services pour qu'ils soient disponibles sur internet depuis un navigateur).    
-Lors de cette relance pas besoin de se connecter à son compte ***Github*** et/ou d'ouvrir son projet sous ***PyCharm*** (le faire que si on met à jour le code puis pusher les commits vers ***Github*** ce qui sera ensuite détecté par ***Render*** qui à son tour déployera les commits pushés sur les services web)

#### d-Déploiement sur Render
L'API est déployée sur ***Render*** et accessible par internet avec l'url :
```bash
https://viken-cdsdm2i-bloc5-2025-api-flask.onrender.com
```
L'interface utilisateur est déployéé sur ***Render*** et accessible par internet avec l'url:  
```bash
https://viken-cdsdm2i-bloc5-2025-interface.onrender.com
```

## Auteur
- **Viken KHATCHERIAN** 

## Contexte 
- **préparation CDSD M2i juin 2025 Bloc 5: Industrialisation d'un algorithme d'apprentissage automatique et automatisation des processus de décision**


