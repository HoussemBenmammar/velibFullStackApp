# Projet Python Velib FullStack App 💬

Ce projet est une application Python qui explore plusieurs fonctionnalités de manipulation de données, notamment via une API, une base de données, et des interfaces HTML pour la visualisation.

---

## Description du Projet 📖

Ce projet est divisé en plusieurs étapes mettant en œuvre des technologies courantes dans le développement Python. Il vous permettra de :

- Gérer une base de données MONGO.
- Interagir avec une API externe pour récupérer et afficher des données.
- Afficher des résultats dans une interface utilisateur simple grâce à Flask et des fichiers HTML.

Chaque script du projet est conçu pour remplir une tâche spécifique et est lié aux autres via une structure claire et modulaire.

---

## Fonctionnalités principales 🚀

### 1️⃣ Insertion de données dans une base de données (tp1_inserer_date.py)

- **But** : Ajouter des données utilisateur dans une base mongo locale.
- **Description** :
  - Utilise Mongo pour créer ou insérer des données dans une table.
  - Vérifie et nettoie les entrées avant de les insérer dans la base.

---

### 2️⃣ Affichage des données depuis une API (tp2_display_from_api.py)

- **But** : Récupérer des données dynamiques depuis une API externe.
- **Description** :
  - Utilise des requêtes HTTP pour interagir avec une API publique ou privée.
  - Affiche les résultats formatés dans une structure lisible.

---

### 3️⃣ Affichage des données depuis une base de données (tp3_display_from_bd.py)

- **But** : Lire et afficher des données stockées localement.
- **Description** :
  - Effectue des requêtes mongo pour récupérer des données à partir d'une base existante.
  - Affiche les résultats de manière organisée.

---

### 4️⃣ Interfaces utilisateur en HTML

- **Fichiers concernés** : `index.html` et `results.html`.
- **Description** :
  - `index.html` : Fournit une interface utilisateur pour interagir avec l'application.
  - `results.html` : Utilisé pour afficher les résultats obtenus depuis la base de données ou l'API.

---

## Structure du Projet 📂

├── tp1_inserer_date.py # Script pour insérer des données dans une base de données
├── tp2_display_from_api.py # Script pour afficher des données récupérées via une API
├── tp3_display_from_bd.py # Script pour afficher des données depuis une base de données
tp4/ ├── templates/ │
  ├── index.html # Page d'accueil de l'application │
  ├── results.html # Page d'affichage des résultats
  ├── Api.py # Script principal pour gérer l'API et le serveur

---

## Prérequis 🔧

Avant d'exécuter ce projet, vous devez installer et configurer les éléments suivants :

- **Python 3.7+**
- **Bibliothèques Python nécessaires** :
  - Flask
  - Mongo (intégré avec Python)
  - Requests (pour les appels API)

---

## Installation et Exécution 🖥️

### Étape 1 : Cloner le projet

Clonez ce dépôt Git en local avec la commande suivante :

```bash
git clone <url-du-repo>
cd tp4
```

### Étape 2 : Installer les dépendances

```bash
pip install flask requests
```

### Étape 3 : Lancer l'application

```bash
python Api.py
Ouvrez votre navigateur et accédez à l'application via l'URL suivante : http://127.0.0.1:5000

```

## Technologies utilisées 🛠️

Python : Langage de programmation principal.
Flask : Utilisé pour créer le serveur backend et gérer les routes.
Mongo : Base de données locale pour stocker et récupérer les données.
HTML/CSS : Pour construire une interface utilisateur simple.

## Améliorations possibles 🔧

**Ajout de nouvelles fonctionnalités API :**
Intégrer une API plus complexe ou ajouter une API RESTful interne.
**Amélioration de l'interface utilisateur :**
Utiliser un framework CSS comme Bootstrap pour rendre les pages plus attrayantes.
Validation des données :
**Ajouter plus de vérifications côté serveur et client pour valider les entrées utilisateur.**

## Auteur ✍️

Nom : BENMAMMAR HOUSSAM

## Licence 📜

Ce projet est sous licence libre. Vous êtes libre de le copier, le modifier, et de l'utiliser à votre convenance.
