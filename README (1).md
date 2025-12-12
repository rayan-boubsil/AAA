
# Challenge Triple A - Dashboard de Monitoring



## Description

Un outil simple pour surveiller une machine virtuelle Linux en temps réel. Il combine :

Administration : gestion d’une VM Ubuntu

Python : collecte des infos système

Web : affichage clair sur un dashboard HTML/CSS

Vous pouvez voir l’état du CPU, de la RAM, du réseau, des processus et des fichiers en un coup d’œil.
## Prérequis
Ubuntu Desktop 22.04+

Python 3

2 GB RAM, 15 GB stockage

Droits sudo


## Installation

git clone https://github.com/votre-utilisateur/challenge-triple-a.git
cd challenge-triple-a
pip install -r requirements.txt
# Commandes pour installer les dépendances
# Comment lancer le script

Lancer le script :

python monitor.py


Ouvrir template.html dans un navigateur pour voir le dashboard.
# Ouvrir index.html dans le navigateur
## Fonctionnalités

Infos système : CPU, RAM, uptime, utilisateurs

Top 3 des processus les plus gourmands

Analyse simple de fichiers (.txt, .py, .pdf, .jpg)

Dashboard clair et léger
## Captures d'écran
## Difficultés rencontrées

Synchroniser Python et HTML en temps réel

Garder le dashboard léger et lisible
## Améliorations possibles

Rafraîchissement automatique

Graphiques dynamiques

Alertes pour seuils critiques
## Auteur

Noé Adouane
Rayan Boubsil
Warchy Assoumani