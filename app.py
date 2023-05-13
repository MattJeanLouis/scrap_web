import streamlit as st
import requests
from bs4 import BeautifulSoup
import pyperclip

import os
import pkg_resources

REQUIRED_PACKAGES = [
    'protobuf==3.20.0'
]

os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'


def get_sub_urls(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        st.write(f"Erreur lors de la récupération de l'URL : {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')

    sub_urls = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.startswith('http'):  # Vérifier si l'URL est absolue
            sub_urls.append(href)

    return sub_urls

def extract_text(url):
    try:
        response = requests.get(url, max_redirects=10)  # Augmenter la limite de redirections
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            return soup.get_text()
        else:
            return None
    except requests.exceptions.TooManyRedirects:
        st.write(f"Trop de redirections lors de la tentative d'accès à l'URL : {url}")
        return None


def main():
    url = st.text_input("Veuillez entrer l'URL : ")
    if url:
        visited_urls = set()  # Pour garder une trace des URL visitées
        summary = []  # Liste pour stocker le sommaire
        all_content = []  # Liste pour stocker tout le contenu

        main_text = extract_text(url)
        visited_urls.add(url)

        summary.append(f"URL principale : {url}")  # Ajouter l'URL principale au sommaire
        all_content.append(main_text)  # Ajouter le contenu principal à all_content

        st.write(f"Texte extrait de l'URL principale : {url}\n{main_text}\n")

        sub_urls = get_sub_urls(url)

        st.write("\nListe des sous-URLs :")
        for sub_url in sub_urls:
            if sub_url not in visited_urls:  # Vérifier si l'URL a déjà été visitée
                with st.expander(sub_url):  # Utilisation de st.expander pour créer un volet déroulant pour chaque sous-URL
                    text = extract_text(sub_url)
                    if text:
                        st.write(f"Texte extrait de l'URL : {sub_url}\n{text}\n")
                        all_content.append(text)  # Ajouter le contenu de la sous-URL à all_content
                    else:
                        st.write(f"Échec de l'extraction du texte à partir de l'URL : {sub_url}\n")
                visited_urls.add(sub_url)  # Ajouter l'URL à la liste des URL visitées

                summary.append(f"Sous-URL : {sub_url}")  # Ajouter la sous-URL au sommaire

        with st.expander("Sommaire"):  # Afficher le sommaire dans un volet déroulant
            for item in summary:
                st.write(item)

        with st.expander("Tout le contenu"):  # Afficher tout le contenu dans un volet déroulant
            all_content_str = "\n".join(all_content)
            st.write(all_content_str)
            if st.button('            Copier tout le contenu'):
                pyperclip.copy(all_content_str)
                st.success('Contenu copié dans le presse-papiers !')

if __name__ == "__main__":
    main()
