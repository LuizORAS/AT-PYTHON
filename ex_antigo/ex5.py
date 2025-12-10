from ex2 import raspar_imdb

class TV:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year})"

class Movie(TV):
    def __init__(self, title, year, rating):
        super().__init__(title, year)
        self.rating = rating

    def __str__(self):
        return f"{self.title} ({self.year}) – Nota: {self.rating}"

class Series(TV):
    def __init__(self, title, year, seasons, episodes):
        super().__init__(title, year)
        self.seasons = seasons
        self.episodes = episodes

    def __str__(self):
        return f"{self.title} ({self.year}) – Temporadas: {self.seasons}, Episódios: {self.episodes}"

if __name__ == "__main__":
    print("Iniciando Scraping e montando o Catálogo...")

    catalog = []

    dados_brutos = raspar_imdb()

    for item in dados_brutos:
        filme_obj = Movie(item['titulo'], item['ano'], item['nota'])
        catalog.append(filme_obj)

    serie1 = Series("Breaking Bad", "2008", 5, 62)
    serie2 = Series("Game of Thrones", "2011", 8, 73)

    catalog.append(serie1)
    catalog.append(serie2)
    print(f"\n--- Catálogo Completo ({len(catalog)} itens) ---\n")

    for media in catalog[:5]: 
        print(media) 
    print("...") 
    for media in catalog[-2:]: 
        print(media) 