from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Coordonnées de la station Vélib "Square Boucicaut"
station_coords = (48.851296433665276, 2.325061820447445)  # Lat, Lon

# Rayon en kilomètres (500 mètres = 0.5 km)
radius = 0.5

# Initialisation du géolocaliseur Nominatim
geolocator = Nominatim(user_agent="velib_locator")

# Trouver une rue proche à moins de 500 mètres
def get_nearby_street(station_coords, radius=0.5):
    # Calculer les coordonnées d'un point proche (ici, on déplace légèrement les coordonnées)
    # pour simuler une recherche dans le voisinage de la station.
    # (Dans un cas réel, on pourrait utiliser une API de recherche géospatiale ou une base de données spatialement indexée)
    
    # Pour l'exemple, nous allons déplacer légèrement les coordonnées de la station
    lat, lon = station_coords
    nearby_coords = (lat + 0.001, lon + 0.001)  # Déplacer légèrement pour obtenir une adresse proche

    # Obtenir l'adresse via Nominatim (API de géocodage)
    location = geolocator.reverse(nearby_coords, language="fr", timeout=10)
    
    if location:
        print(f"Adresse proche : {location.address}")
    else:
        print("Aucune adresse trouvée à proximité.")
    
# Appel de la fonction pour obtenir la rue proche
get_nearby_street(station_coords)
