import requests
from pymongo import MongoClient

# URL de l'API Velib
url = 'https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records'

# Paramètres pour la requête
params = {
    'limit': 1000  # Limite ajustée pour récupérer plus de stations
}

# Faire la requête GET
response = requests.get(url, params=params)

# Vérifier si la requête a réussi
if response.status_code == 200:
    data = response.json()

    # Afficher la réponse complète pour comprendre la structure
    print("Réponse complète de l'API :")
    print(data)

    # Vérifier la présence de 'records'
    if 'records' in data:
        print("Enregistrements trouvés.")

        # Connexion à MongoDB (localhost:27017)
        client = MongoClient('mongodb://localhost:27017/')

        # Accéder à la base de données "tp1" et à la collection "apiVelib"
        db = client['tp1']
        collection = db['apiVelib']

        # Insérer les enregistrements dans MongoDB
        collection.insert_many(data['records'])
        print("Données insérées avec succès dans MongoDB.")
    else:
        print("Aucun enregistrement à insérer.")
else:
    print(f"Erreur lors de la requête : {response.status_code}")
