from flask import Flask, render_template, request, jsonify
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from pymongo import MongoClient

app = Flask(__name__)

# Configuration MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['tp1']
collection = db['apiVelib']

# Fonction pour convertir une adresse en coordonnées
def get_coordinates(address):
    geolocator = Nominatim(user_agent="velib_locator")
    location = geolocator.geocode(address)
    if location:
        return location.latitude, location.longitude
    return None

# Fonction pour trouver les stations à moins de 500 m avec des vélos électriques disponibles
def find_nearby_stations(coords, radius=0.5):
    nearby_stations = []
    for station in collection.find():
        station_coords = station.get('coordonnees_geo', None)
        if station_coords:
            station_location = (station_coords['lat'], station_coords['lon'])
            distance = geodesic(coords, station_location).km
            if distance <= radius and station.get('ebike', 0) > 0:
                nearby_stations.append({
                    "name": station.get('name', 'Unknown Station'),
                    "distance": round(distance, 3),
                    "ebike": station.get('ebike', 0),
                    "lat": station_coords['lat'],
                    "lon": station_coords['lon']
                })
    return nearby_stations

# Page principale avec formulaire
@app.route('/')
def home():
    return render_template('index.html')

# Route pour traiter l'adresse et afficher les résultats
@app.route('/search', methods=['POST'])
def search():
    address = request.form['address']
    coords = get_coordinates(address)
    if not coords:
        return jsonify({"error": "Adresse non trouvée. Veuillez réessayer."}), 400

    nearby_stations = find_nearby_stations(coords)
    return render_template('results.html', address=address, stations=nearby_stations)

if __name__ == '__main__':
    app.run(debug=True)
