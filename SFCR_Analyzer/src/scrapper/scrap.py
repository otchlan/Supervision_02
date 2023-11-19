import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, urlparse
import queue

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

    links = queue.Queue()
    links.put(base_url)
    
    while links.empty() == False:
        try:
        #print(visited)


            #print(links)
            url=links.get()

            # Sprawdź, czy URL został już odwiedzony
            if url in visited:
                continue
            visited.add(url)
            # Wykonaj zapytanie HTTP GET do podanej strony
            response = requests.get(url)
            response.raise_for_status()
            # Użyj BeautifulSoup do parsowania HTML
            soup = BeautifulSoup(response.text, 'html.parser')  


            # Znajdź wszystkie linki (tagi 'a')
            if urlparse(url).netloc == urlparse(base_url).netloc:  # Sprawdź, czy url jest w obrębie tej samej domeny
                # Wyświetl URL i wszystkie linki na tej stronie
                print(f"{url} zawiera linki do:")
                try:
                    newlinks = [urljoin(base_url, url.get('href')) for url in soup.find_all('a')] #znajdź linki na stronie
                    for i in newlinks:
                        if urlparse(i).netloc == urlparse(base_url).netloc:
                            if not i in visited:
                                print (f" - {i}")
                                links.put(i)
                except:
                    pass
                

        except requests.RequestException as e:
            print(f'Błąd podczas łączenia z {url}: {e}')
            continue
        except Exception as e:
            print(f'Wystąpił błąd: {e}')
            continue

# Użyj funkcji do przeszukania strony
base_url = 'https://www.allianz.pl/'  # Zmień to na faktyczny URL
build_site_map(base_url, base_url)
#todo: przeszukać zawartości stron w poszukiwaniu nazw: 
#"SFCR", 
#"Sprawozdanie o wypłacalności finansowej",
#"sprawozdanie na temat wypłacalności finansowej"
# bo np pzu nie ma pliku który miał by to w nazwie
