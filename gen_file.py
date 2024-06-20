import os
import uuid
import random
import json
from datetime import datetime, timedelta

# Créer une session à partir du cluster
from cassandra.cluster import Cluster

cluster = Cluster(['localhost'], port=9042)
session = cluster.connect()

# Créer un keyspace si nécessaire
session.execute(
    "CREATE KEYSPACE IF NOT EXISTS vision112 WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 3}")

# Utiliser le keyspace
session.set_keyspace('vision112')

# Créer une table si nécessaire
session.execute("""
    CREATE TABLE IF NOT EXISTS fiche_accident (
        uuid text PRIMARY KEY,
        event_date_time timestamp,
        source text,
        type_data text,
        coordonnee_lat FLOAT,
        coordonnee_long FLOAT,
        code_postal text,
        type_alerte text,
        type_vehicule text,
        accident_date_time timestamp
    )
""")


def generate_gaussian_coordinates(points):
    # Choisir une coordonnée de base et un code postal aléatoires
    base_coord, base_cp = random.choice(points)
    # Convertir la coordonnée de base en un tuple de floats
    base_coord = tuple(map(float, base_coord.split(',')))
    # Générer une nouvelle coordonnée en ajoutant un bruit gaussien
    new_coord = tuple(coord + random.gauss(0, 0.1) for coord in base_coord)
    # Retourner la nouvelle coordonnée et le code postal associé
    return new_coord[0], new_coord[1], base_cp


# Liste des sources possibles
sources = ["ArcEuropeFrance", "AllianzPartners", "AxaPartners", "EuropAssistance", "FideliaAssistance", "IMA",
           "Filassistance", "Mutuaide", "Opteven"]

# Liste des types d'alerte possibles
types_alerte = ["appelUrgence", "appelAssistanceAccident", "appelAssistancePanne", "erreurAppel", "autre"]

# Liste des types de véhicules possibles
types_vehicule = ["moto", "poidLourd", "voiture", "vehiculeAutonome", "transportCommun", "autre"]

# Coordonnées GPS et codes postaux pré-sélectionnés
points = [
    ("46.31955,-0.55214", "77200"),
    ("48.074999,-1.642846", "35135"),
    ("47.958926,0.231581", "72230"),
    ("43.573534,3.918011", "34970"),
    ("47.23765,5.898973", "25770"),
    ("46.009448,5.439697", "01640"),
    ("45.0016798,-0.4704463", "33240"),
    ("43.4760699,-1.4450623", "64990"),
    ("50.5391184,3.0705097", "59710"),
    ("48.6331705,5.8660407", "54113"),
    ("45.9342397,3.1249977", "63200"),
    ("43.57725,1.6283889", "31570"),
    ("45.3215827,3.3680877", "43100"),
    ("48.4196515,-4.4428013", "29490"),
    ("48.8047765,2.2721267", "92140"),
    ("48.2869925,4.1244487", "10410"),
    ("48.0881857,5.0900005", "52000"),
    ("46.8083276,0.5234867", "86100"),
    ("45.1755208,5.7660277", "38400"),
    ("43.7109788,7.1800987", "06700")
]

# Chemin du dossier où enregistrer les fichiers
output_dir = "resources/ficheAccident"

start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
time_between_dates = end_date - start_date
days_between_dates = time_between_dates.days

for i in range(1000):
    # Générer des coordonnées aléatoires selon une distribution gaussienne
    coordonnee_lat, coordonnee_long, code_postal = generate_gaussian_coordinates(points)
    random_number_of_days = random.randrange(days_between_dates)
    random_date = (start_date + timedelta(days=random_number_of_days)).isoformat()

    data = {
        "FicheAccident": {
            "uuid": str(uuid.uuid4()),
            "event_date_time": random_date,
            "source": random.choice(sources),
            "type_data": "ficheEcall112BI"
        },
        "payload": {
            "descriptionAccident": {
                "coordonnee_lat": coordonnee_lat,
                "coordonnee_long": coordonnee_long,
                "code_postal": code_postal,
                "type_alerte": random.choice(types_alerte),
                "type_vehicule": random.choice(types_vehicule),
                "accident_date_time": random_date
            }
        }
    }

    print(data["FicheAccident"])

    # Insérer les données dans la table Cassandra
    session.execute("""
        INSERT INTO fiche_accident (uuid, event_date_time, source, type_data, coordonnee_lat, coordonnee_long, code_postal, type_alerte, type_vehicule, accident_date_time)
        VALUES (%(uuid)s, %(event_date_time)s, %(source)s, %(type_data)s, %(coordonnee_lat)s, %(coordonnee_long)s, %(code_postal)s, %(type_alerte)s, %(type_vehicule)s, %(accident_date_time)s)
    """, data["FicheAccident"] | data["payload"]["descriptionAccident"])
