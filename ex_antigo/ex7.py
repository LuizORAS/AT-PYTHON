import pandas as pd
from sqlalchemy import create_engine
import os

DB_NAME = 'imdb.db'

def carregar_dados():
    print("--- Tentando conectar ao banco de dados ---")
    
    if not os.path.exists(DB_NAME):
        print(f"Erro: O arquivo '{DB_NAME}' não foi encontrado. Rode o ex6.py primeiro.")
        return

    try:

        engine = create_engine(f'sqlite:///{DB_NAME}', echo=False)


        print("\nLendo tabela 'movies'...")

        df_movies = pd.read_sql_table('movies', con=engine)

        print("Lendo tabela 'series'...")
        df_series = pd.read_sql_table('series', con=engine)


        print("\n" + "="*40)
        print(" FILMES (Top 5 registros) ")
        print("="*40)

        print(df_movies.head())

        print("\n" + "="*40)
        print(" SÉRIES (Top 5 registros) ")
        print("="*40)
        print(df_series.head())
        

        print("\n--- Info do DataFrame de Filmes ---")
        print(df_movies.info())

    except ValueError as ve:

        print(f"Erro de Valor (Tabela não encontrada?): {ve}")
    except Exception as e:

        print(f"Ocorreu um erro inesperado ao ler o banco: {e}")

if __name__ == "__main__":
    carregar_dados()