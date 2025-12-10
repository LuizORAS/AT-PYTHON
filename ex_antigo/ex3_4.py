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

#EX4
print("--- Testando Movie ---")
filme = Movie("The Shawshank Redemption", "1994", 9.2)
print(filme)
print("\n--- Testando Series ---")
serie = Series("Breaking Bad", "2008", 5, 62)
print(serie)

# EX3
meu_filme = TV("Breaking Bad", "2008")
print(meu_filme)