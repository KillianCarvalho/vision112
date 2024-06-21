# VISION112

Vision112 est une application web développée pour un cours de Python avancé et Cassandra. Elle a été conçue et développée par deux étudiants : <a href='https://github.com/KillianCarvalho'>Killian</a> et <a href='https://github.com/Septsept'>Mohamed</a>.

## Description

Vision112 est une application web utilisant des données anonymisées de l'eCall112, permettant de visualiser les localisations d'accidents routiers sur une période définie. Cette application servira les besoins de la Direction Départementale de l'Équipement (DDE) ainsi que des statisticiens de l'INRETS (Institut National de Recherche sur les Transports et leur Sécurité).

## Installation

Pour installer et exécuter l'application, suivez les étapes suivantes :

1. Clonez le dépôt GitHub sur votre machine locale.
2. Installez un serveur local (comme XAMPP, WAMP, MAMP ou LAMP) si vous n'en avez pas déjà un.
3. Placez le dossier cloné dans le répertoire de votre serveur local.
4. Créez votre base de données avec cette commande à la racine du projet (cette commande permettra aussi de générer des données) :
```sh
python gen_file.py
```
5. Démarrez votre serveur en local avec cette commande à partir de la racine du projet :
```sh
python db.py
```

## Utilisation

L'application est très simple à utiliser. Une fois que vous avez ouvert l'application dans votre navigateur, Vous n'avez qu'à choisir vos filtres sur la partie gauche de votre écran puis cliquer sur le bouton "FILTRER", les données d'afficheront directement sur la partie droite. Vous pouvez afficher les données soit sur une map soit en tableau en cliquant sur le bouton switch.

## Versions nécessaires

Pour exécuter l'application, vous aurez besoin des versions suivantes des logiciels :

- Apache 2.4
- Python 3.12
- Cassandra 6.1
- HTML 5
- CSS 3

## Contact

Si vous avez des questions ou des commentaires, n'hésitez pas à nous contacter :

- Killian : killian.carvalho@edu.ecole-89.com
- Mohamed : mohamed.benyamina@edu.ecole-89.com

Nous espérons que vous apprécierez l'utilisation de Vision112 autant que nous avons apprécié le développer !
