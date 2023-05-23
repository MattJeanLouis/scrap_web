import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import html2text

def crawl(url, base_url):
    # Récupérer le contenu du site
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Rechercher tous les liens
    sub_urls = []
    for link in soup.find_all('a'):
        href = link.get('href')
        # Ignorer les liens qui n'ont pas d'attribut href ou qui sont des ancres
        if href is None or href.startswith('#'):
            continue

        # Joindre l'URL du lien avec l'URL de base du site pour obtenir un lien complet
        full_url = urljoin(base_url, href)

        # Vérifier si le lien est sur le même domaine
        if urlparse(full_url).netloc == urlparse(base_url).netloc:
            if full_url not in visited_urls:
                visited_urls.add(full_url)
                sub_urls.append(full_url)
    return sub_urls

def url_to_markdown(url):
    # Récupérer le contenu du site
    response = requests.get(url)
    response.encoding = 'utf-8'  # Spécifiez l'encodage si nécessaire
    html_content = response.text

    # Utiliser BeautifulSoup pour analyser le contenu HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Utiliser html2text pour convertir le contenu HTML en Markdown
    h = html2text.HTML2Text()
    # Ignorer les liens dans le document
    h.ignore_links = True
    markdown_content = h.handle(soup.prettify())

    return markdown_content

def main():
    base_url = st.text_input("Veuillez entrer l'URL : ")
    if base_url:
        global visited_urls
        visited_urls = set()  # Pour garder une trace des URL visitées

        # Utilisation des nouvelles méthodes
        markdown_content = url_to_markdown(base_url)
        st.markdown(markdown_content)  # Utilisation de st.markdown pour afficher le contenu

        sub_urls = crawl(base_url, base_url)

        st.write("\nListe des sous-URLs :")
        for sub_url in sub_urls:
            with st.expander(sub_url):  # Utilisation de st.expander pour créer un volet déroulant pour chaque sous-URL
                markdown_content = url_to_markdown(sub_url)
                st.markdown(markdown_content)  # Utilisation de st.markdown pour afficher le contenu

if __name__ == "__main__":
    main()
