import requests
import folium
import webbrowser

# URL de l'API Velib
url = 'https://opendata.paris.fr/api/explore/v2.1/catalog/datasets/velib-disponibilite-en-temps-reel/records'

# Paramètres pour la requête (limite à 20 résultats pour le test)
params = {
    'limit': 20  # Ajuste cette limite selon le besoin
}

# Faire la requête GET pour récupérer les données
response = requests.get(url, params=params)

# Vérifier si la requête a réussi
if response.status_code == 200:
    data = response.json()

    # Créer la carte centrée sur Paris
    m = folium.Map(location=[48.8566, 2.3522], tiles="OpenStreetMap", zoom_start=13)

    # Vérifier la présence de 'results' dans les données retournées
    if 'results' in data:
        # Boucle à travers chaque station récupérée
        for result in data['results']:
            station = result['stationcode']
            name = result['name']
            capacity = result['capacity']
            available_bikes = result['numbikesavailable']
            geo = result['coordonnees_geo']  # Coordonnées géographiques

            # Extraire les coordonnées (lat, lon)
            lat = geo['lat']
            lon = geo['lon']

            # Créer un texte pour le popup avec des infos utiles
            popup_text = f"<b>{name}</b><br>Capacity: {capacity}<br>Bikes Available: {available_bikes}"

            # Ajouter un marqueur à la carte pour chaque station
            folium.Marker([lat, lon], popup=popup_text).add_to(m)

        # Sauvegarder la carte dans un fichier HTML
        m.save("velib_map.html")

        # Ouvrir la carte dans le navigateur
        webbrowser.open('velib_map.html')

    else:
        print("Aucun enregistrement trouvé dans l'API Velib.")
else:
    print(f"Erreur lors de la requête : {response.status_code}")
