# Utilisation de l'image officielle de Cassandra
FROM cassandra:latest

# Installation des dépendances Python
RUN apt-get update && apt-get install -y python3 python3-pip

# Installation du pilote Cassandra pour python
RUN pip3 install cassandra-driver

# Copie du fichier Python dans le conteneur
COPY ./gen_file.py  /app/gen_file.py

# Définition du répertoire de travail
WORKDIR /app

# Définition de la variable d'environnement pour l'adresse du cluster Cassandra
ENV CASSANDRA_CLUSTER 127.0.0.1

# Commande par défaut pour éxectuer le script Python avec la variable d'environnement
CMD ["python3", "-e", "CASSANDRA_CLUSTER", "gen_file.py"]
