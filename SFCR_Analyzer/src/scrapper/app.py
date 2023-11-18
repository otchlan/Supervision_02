import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse

def find_pdf_links(url, base_url):
    try:
        # Wykonaj zapytanie HTTP GET do podanej strony
        response = requests.get(url)
        response.raise_for_status()  # Sprawdź, czy odpowiedź jest poprawna

        # Użyj BeautifulSoup do parsowania HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Znajdź wszystkie linki (tagi 'a') i filtruj te, które prowadzą do 'example.pdf'
        pdf_links = [urljoin(base_url, link.get('href')) for link in soup.find_all('a', href=re.compile('example\.pdf$'))]

        return pdf_links
    except requests.RequestException as e:
        print(f'Błąd podczas łączenia z {url}: {e}')
        return []
    except Exception as e:
        print(f'Wystąpił błąd: {e}')
        return []

def build_site_map(url, base_url, visited=None):
    if visited is None:
        visited = set()

    try:
        # Sprawdź, czy URL został już odwiedzony
        if url in visited:
            return
        visited.add(url)

        # Wykonaj zapytanie HTTP GET do podanej strony
        response = requests.get(url)
        response.raise_for_status()

        # Użyj BeautifulSoup do parsowania HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Znajdź wszystkie linki (tagi 'a')
        links = [urljoin(base_url, link.get('href')) for link in soup.find_all('a')]

        # Wyświetl URL i wszystkie linki na tej stronie
        print(f"{url} zawiera linki do:")
        for link in links:
            if urlparse(link).netloc == urlparse(base_url).netloc:  # Sprawdź, czy link jest w obrębie tej samej domeny
                print(f"  - {link}")
                build_site_map(link, base_url, visited)  # Rekurencyjne przeszukiwanie linków

    except requests.RequestException as e:
        print(f'Błąd podczas łączenia z {url}: {e}')
    except Exception as e:
        print(f'Wystąpił błąd: {e}')

# Użyj funkcji do przeszukania strony
base_url = 'https://www.allianz.pl'  # Zmień to na faktyczny URL

