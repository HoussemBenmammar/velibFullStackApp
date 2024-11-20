import threading
import requests
import time

class VelibThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.data = None

    def run(self):
        url = "https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel"
        response = requests.get(url)
        self.data = response.json()
        print("Données Vélib récupérées")


class BelibThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.data = None

    def run(self):
        url = "https://opendata.paris.fr/api/records/1.0/search/?dataset=belib-points-de-recharge-pour-vehicules-electriques-disponibilite-temps-reel"
        response = requests.get(url)
        self.data = response.json()
        print("Données Bélib récupérées")

def main():
    start_time = time.time()

    velib_thread = VelibThread()
    belib_thread = BelibThread()

    velib_thread.start()
    belib_thread.start()

    velib_thread.join()
    belib_thread.join()

    print(f"Temps d'exécution total : {time.time() - start_time:.2f} secondes")

    print(f"Nombre de stations Vélib : {len(velib_thread.data['records'])}")
    print(f"Nombre de bornes Bélib : {len(belib_thread.data['records'])}")

if __name__ == "__main__":
    main()