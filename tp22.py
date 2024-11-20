import requests
import folium
import webbrowser

# URL de l'API Velib
url = 'https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records'

# Paramètres pour la requête
params = {
    'rows': 1000
}

# Faire la requête GET
response = requests.get(url, params=params)

# Vérifier si la requête a réussi
if response.status_code == 200:
    data = response.json()

    # Créer la carte centrée sur Paris
    m = folium.Map(location=[48.8566, 2.3522], tiles="OpenStreetMap", zoom_start=13)

    # Vérifier la présence de 'records'
    if 'records' in data:
        for record in data['records']:
            # Récupération des informations nécessaires
            fields = record['fields']
            name = fields.get('name', 'Unknown Station')
            capacity = fields.get('capacity', 0)
            available_bikes = fields.get('numbikesavailable', 0)
            coords = fields.get('coordonnees_geo', [48.8566, 2.3522])

            # Créer un texte pour le popup
            popup_text = f"<b>{name}</b><br>Capacity: {capacity}<br>Bikes Available: {available_bikes}"

            # Ajouter un marqueur sur la carte
            folium.Marker(coords, popup=popup_text).add_to(m)

        # Sauvegarder la carte dans un fichier HTML
        m.save("velib_map_api.html")

        # Ouvrir la carte dans le navigateur
        webbrowser.open("velib_map_api.html")
    else:
        print("Aucun enregistrement trouvé dans l'API.")
else:
    print(f"Erreur lors de la requête : {response.status_code}")
