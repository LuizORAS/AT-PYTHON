import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:

    print("Baixando o HTML do IMDb...")
    response = requests.get(url, headers=headers)
    response.raise_for_status() 

    soup = BeautifulSoup(response.text, "html.parser")
    tags_titulos = soup.select("h3.ipc-title__text")
    
    lista_filmes = []

    for tag in tags_titulos:
        texto = tag.get_text(strip=True)
        lista_filmes.append(texto)

    print("\n--- Top 10 Filmes do IMDb ---")

    for filme in lista_filmes[:10]:
        print(filme)
except Exception as e:
    print(f"Ocorreu um erro: {e}")