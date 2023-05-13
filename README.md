# Web Scraper avec Streamlit

Ce projet est un web scraper construit avec Streamlit, une bibliothèque Python pour créer des applications web rapidement. Il permet d'extraire le texte de n'importe quelle page web et de ses sous-pages.

## Fonctionnalités

- Extraction du texte de n'importe quelle page web et de ses sous-pages.
- Affichage du texte extrait dans un format facile à lire.
- Affichage d'un sommaire des URL visitées.
- Affichage de tout le contenu extrait dans un volet déroulant.
- Option pour copier tout le contenu extrait dans le presse-papiers.

## Installation

1. Clonez ce dépôt sur votre machine locale.
2. Installez les dépendances en exécutant `pip install -r requirements.txt` dans votre terminal.
3. Exécutez l'application en tapant `streamlit run app.py` dans votre terminal.

## Utilisation

1. Entrez l'URL de la page web dont vous voulez extraire le texte dans le champ de saisie.
2. L'application extrait le texte de l'URL principale et de toutes ses sous-URLs.
3. Le texte extrait est affiché dans un format facile à lire.
4. Un sommaire des URL visitées est affiché dans un volet déroulant.
5. Tout le contenu extrait est affiché dans un volet déroulant. Vous pouvez copier ce contenu dans votre presse-papiers en cliquant sur le bouton "Copier tout le contenu".

## Dépendances

- streamlit
- requests
- beautifulsoup4
- pyperclip

## Auteur

[Matt Pasquier]
