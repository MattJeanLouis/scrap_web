# Web Scraper avec Streamlit

Ce projet est un web scraper construit avec Streamlit, une bibliothèque Python pour créer des applications web rapidement. Il permet d'extraire le texte de n'importe quelle page web et de ses sous-pages, puis de convertir le contenu HTML en Markdown pour un affichage facile à lire.

## Fonctionnalités

- Extraction du texte de n'importe quelle page web et de ses sous-pages.
- Conversion du contenu HTML en Markdown pour un affichage facile à lire.
- Exploration récursive des sous-pages d'une URL donnée.
- Affichage du contenu Markdown extrait dans un format lisible.
- Affichage d'un sommaire des URL visitées dans un volet déroulant.

## Installation

1. Clonez ce dépôt sur votre machine locale.
2. Installez les dépendances en exécutant `pip install -r requirements.txt` dans votre terminal.
3. Exécutez l'application en tapant `streamlit run app.py` dans votre terminal.

## Utilisation

1. Entrez l'URL de la page web dont vous voulez extraire le texte dans le champ de saisie.
2. L'application extrait le texte de l'URL principale et de toutes ses sous-URLs, et convertit le contenu HTML en Markdown.
3. Le contenu Markdown extrait est affiché dans un format facile à lire.
4. Un sommaire des URL visitées est affiché dans un volet déroulant.
5. Tout le contenu extrait est affiché dans un volet déroulant.

## Dépendances

- streamlit
- requests
- beautifulsoup4
- html2text

## Auteur

[Matt Pasquier]
