import requests
from bs4 import BeautifulSoup

def raspar_imdb():
    """
    Função que acessa o IMDb e retorna uma lista de dicionários.
    """
    url = "https://www.imdb.com/chart/top/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    dados_filmes = []

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        filmes_containers = soup.select("li.ipc-metadata-list-summary-item")
        
        for filme in filmes_containers:
            tag_titulo = filme.select_one("h3.ipc-title__text")
            titulo_limpo = tag_titulo.get_text(strip=True).split('. ', 1)[-1]
            

            metadados = filme.select("span.cli-title-metadata-item")
            ano = metadados[0].get_text(strip=True) if metadados else "N/A"
            
            tag_nota = filme.select_one("span.ipc-rating-star--rating")
            nota = tag_nota.get_text(strip=True) if tag_nota else "N/A"
            
            dados_filmes.append({
                "titulo": titulo_limpo,
                "ano": ano,
                "nota": nota
            })
            
    except Exception as e:
        print(f"Erro no scraping: {e}")
        
    return dados_filmes