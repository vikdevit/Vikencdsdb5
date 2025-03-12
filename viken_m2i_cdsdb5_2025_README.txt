A-cas d'utilisation en local
0-Installation des dépendances
création environnement virtuel bloc5-env
(bloc5-env) PS C:\Users\vkhat\PycharmProjects\VikenCDSDB5Project> pip list
Package                   Version
------------------------- -----------
altair                    5.5.0
attrs                     25.1.0
blinker                   1.9.0
cachetools                5.5.2
certifi                   2025.1.31
charset-normalizer        3.4.1
click                     8.1.8
colorama                  0.4.6
Flask                     3.1.0
gitdb                     4.0.12
GitPython                 3.1.44
idna                      3.10
itsdangerous              2.2.0
Jinja2                    3.1.5
joblib                    1.4.2
jsonschema                4.23.0
jsonschema-specifications 2024.10.1
markdown-it-py            3.0.0
MarkupSafe                3.0.2
mdurl                     0.1.2
narwhals                  1.27.1
numpy                     2.2.3
packaging                 24.2
pandas                    2.2.3
pillow                    11.1.0
pip                       24.0
protobuf                  5.29.3
pyarrow                   19.0.1
pydeck                    0.9.1
Pygments                  2.19.1
python-dateutil           2.9.0.post0
pytz                      2025.1
referencing               0.36.2
requests                  2.32.3
rich                      13.9.4
rpds-py                   0.23.0
scikit-learn              1.6.1
scipy                     1.15.2
setuptools                65.5.0
six                       1.17.0
smmap                     5.0.2
streamlit                 1.42.2
tenacity                  9.0.0
threadpoolctl             3.5.0
toml                      0.10.2
tornado                   6.4.2
typing_extensions         4.12.2
tzdata                    2025.1
urllib3                   2.3.0
watchdog                  6.0.0
Werkzeug                  3.1.3

pip freeze > requirements.txt

(bloc5-env) PS C:\Users\vkhat\PycharmProjects\VikenCDSDB5Project> python --version
Python 3.11.9

1-Lancement api flask
a-ouvrir un premier terminal sous PyCharm et écrire:
python .\viken_m2i_cdsdb5_2025_app.py
résultat attendu:
 * Serving Flask app 'viken_m2i_cdsdb5_2025_app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with watchdog (windowsapi)
 * Debugger is active!
 * Debugger PIN: 276-960-467
127.0.0.1 - - [21/Feb/2025 10:04:33] "POST /predict HTTP/1.1" 200 -

b-ouvrir un deuxième terminal sous PyCharm et écrire:
Invoke-WebRequest -Uri http://127.0.0.1:5000/predict -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"features": [5.1, 3.5, 1.4, 0.2]}'
résultat attendu:

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

ci-dessous autre test pour vérifier prédictions du modèle
(bloc5-env) PS C:\Users\vkhat\PycharmProjects\VikenCDSDB5Project> Invoke-WebRequest -Uri http://127.0.0.1:5000/predict -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"features": [7.0, 3.2, 4.7, 1.4]}'


StatusCode        : 200
StatusDescription : OK
Content           : {
                      "prediction": 1
                    }

RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 22
                    Content-Type: application/json
                    Date: Fri, 21 Feb 2025 09:11:52 GMT
                    Server: Werkzeug/3.1.3 Python/3.11.9

                    {
                      "prediction": 1
                    }

Forms             : {}
Headers           : {[Connection, close], [Content-Length, 22], [Content-Type, application/json], [Date, Fri, 21 Feb 2025 09:11:52 GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 22


(bloc5-env) PS C:\Users\vkhat\PycharmProjects\VikenCDSDB5Project> Invoke-WebRequest -Uri http://127.0.0.1:5000/predict -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"features": [6.3, 3.3, 6.0, 2.5]}'


StatusCode        : 200
StatusDescription : OK
Content           : {
                      "prediction": 2
                    }

RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 22
                    Content-Type: application/json
                    Date: Fri, 21 Feb 2025 09:13:48 GMT
                    Server: Werkzeug/3.1.3 Python/3.11.9

                    {
                      "prediction": 2
                    }

Forms             : {}
Headers           : {[Connection, close], [Content-Length, 22], [Content-Type, application/json], [Date, Fri, 21 Feb 2025 09:13:48 GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 22



(bloc5-env) PS C:\Users\vkhat\PycharmProjects\VikenCDSDB5Project>

2-Lancement de l'interface utilisateur Streamlit
Ouvrir un troisième terminal sous PyCharm et écrire:
streamlit run .\viken_m2i_cdsdb5_2025_interface.py

On obtient ci-dessous
 Welcome to Streamlit!

      If you’d like to receive helpful onboarding emails, news, offers, promotions,
      and the occasional swag, please enter your email address below. Otherwise,
      leave this field blank.

      Email:

  You can find our privacy policy at https://streamlit.io/privacy-policy

  Summary:
  - This open source library collects usage statistics.
  - We cannot see and do not store information contained inside Streamlit apps,
    such as text, charts, images, etc.
  - Telemetry data is stored in servers in the United States.
  - If you'd like to opt out, add the following to %userprofile%/.streamlit/config.toml,
    creating that file if necessary:

    [browser]
    gatherUsageStats = false


  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.20:8501

Pour vérifier le fonctionnement de l'interface web, possibilité d'ouvrir une page web et d'écrire:
  Local URL: http://localhost:8501
ou
 Network URL: http://192.168.1.20:8501

3-Fermer l'API Flask
taper ctrl + C dans le premier terminal ouvert
on obtient alors ci-dessous et retrouve le chemin du répertoire du projet avec l'environnement virtuel utilisé
KeyboardInterrupt
(bloc5-env) PS C:\Users\vkhat\PycharmProjects\VikenCDSDB5Project>

4- Fermer simplement le deuxième terminal qui était utilisé plus haut pour envoyer la commande
Invoke-WebRequest -Uri http://127.0.0.1:5000/predict -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"features": [5.1, 3.5, 1.4, 0.2]}'

5- Fermer l'application Streamlit
taper ctrl + c dans le troisième terminal
on obtient alors le résultat ci-dessous dans le terminal avec récupération du chemin où se trouve le projet avec l'environnement virtuel
 Stopping...
(bloc5-env) PS C:\Users\vkhat\PycharmProjects\VikenCDSDB5Project>

6- On peut ensuite refaire un essai de lancement en suivant dans l'ordre les étapes 1 et 2 ci-dessus

B-cas d'utilisation avec Render (plateforme de déploiement cloud pour héberger l'API et son interface utilisateur)

0- Mettre à jour le fichier dependances_projet_b5.txt pour installer gunicorn

1-Se connecter à Render avec https://render.com
Créer un compte en s'identifiant avec son compte Github
Choisir profil student

2-Créer un service web pour l'api flask
-CLiquer sur Create Web Service
-Choisir le langage Python
-Nom du service : viken-cdsdm2i-bloc5-2025-api-flask
-Region : Frankfurt (EU Central)
-Indiquer l'url du repository où sont hébergés les scripts et leurs dépendances
(ici https://github.com/vikdevit/Vikencdsdb5)
-Indiquer le nom de la branche (ici master)
-Renseigner pour build command: pip install -r dependances_projet_b5.txt
-Renseigner pour start command: gunicorn viken_m2i_cdsdb5_2025_app:app
-Pour l'auto-déploiement suite à push des commits git vers Github choisir Yes (les services se mettent automatiquement à jour)
-Pour tester cliquer sur start service et ouvrir une page html avec l'url:
https://viken-cdsdm2i-bloc5-2025-api-flask.onrender.com
Suivre les logs dans la rubrique Monitor/logs  et la rubrique Events qui permet aussi de suivre le déploiement des commits
Remarque: en cas de maj du code via git/github laisser render déployer les commit en suivant la rubrique event
(possibilité d'arrêter le service puis de déclencher manuellement le commit puis de relancer le service après la fin du déploiement)

3-Créer un service web pour l'interface utilisateur Streamlit
-CLiquer sur Create Web Service
-Choisir le langage Python
-Nom du service : viken-cdsdm2i-bloc5-2025-interface-streamlit
-Region : Frankfurt (EU Central)
-Indiquer l'url du repository où sont hébergés les scripts et leurs dépendances
(ici https://github.com/vikdevit/Vikencdsdb5)
-Indiquer le nom de la branche (ici master)
-Renseigner pour build command: pip install -r dependances_projet_b5.txt
-Renseigner pour start command: streamlit run viken_m2i_cdsdb5_2025_interface.py --server.port $PORT --server.address 0.0.0.0
-Pour l'auto-déploiement suite à push des commits git vers Github choisir Yes (les services se mettent automatiquement à jour)
-Pour tester cliquer sur start service et ouvrir une page html avec l'url:
https://viken-cdsdm2i-bloc5-2025-interface.onrender.com
Suivre les logs dans la rubrique Monitor/logs  et la rubrique Events qui permet aussi de suivre le déploiement des commits
Remarque: en cas de maj du code via git/github laisser render déployer les commit en suivant la rubrique event
(possibilité d'arrêter le service puis de déclencher manuellement le commit puis de relancer le service après la fin du déploiement)

Remarque:
-arrêter les services si non utilisés pour ne pas atteindre la limite maximum mensuelle liée au profil student de Render
-si besoin d'utilisation, activer les deux services ("Resume Web Service" dans la rubrique settings du service, pas besoin de cliquer sur restart service en haut à droite dans la rubrique event)
-la relance des services se fait après s'être reconnecté à Render avec ses identifiants Github via https://dashboard.render.com/login
(patienter environ 1 minute après avoir relancé les services pour qu'ils soient disponibles dans un navigateur).
-lors de cette relance pas besoin de se connecter à son compte Github et/ou d'ouvrir son projet sous PyCharm (le faire que si on met à jour le code puis pusher les commits vers Github ce qui sera ensuite détecté par Render qui à son tour déployera les commits pushés sur les services web)
