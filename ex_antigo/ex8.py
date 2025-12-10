import pandas as pd
from sqlalchemy import create_engine

def analisar_e_exportar():

    db_name = 'imdb.db'
    engine = create_engine(f'sqlite:///{db_name}', echo=False)

    try:
        print("--- Lendo dados do banco ---")
        df_movies = pd.read_sql_table('movies', con=engine)
        df_series = pd.read_sql_table('series', con=engine)
        df_ordenado = df_movies.sort_values(by='rating', ascending=False)
        df_top_tier = df_ordenado[df_ordenado['rating'] > 9.0]
        print("\n--- Top 5 Filmes (Nota > 9.0) ---")
        print(df_top_tier[['title', 'year', 'rating']].head(5))

        print("\n--- Iniciando Exportação ---")

        df_top_tier.to_csv('movies.csv', index=False, encoding='utf-8')
        df_series.to_csv('series.csv', index=False, encoding='utf-8')
        print("Arquivos CSV gerados: 'movies.csv' e 'series.csv'")

 
        df_top_tier.to_json('movies.json', orient='records', indent=4, force_ascii=False)
        df_series.to_json('series.json', orient='records', indent=4, force_ascii=False)
        print("Arquivos JSON gerados: 'movies.json' e 'series.json'")

    except PermissionError:
        print("Erro: Permissão negada. Verifique se o arquivo já está aberto em outro programa (como Excel).")
    except Exception as e:
        print(f"Ocorreu um erro durante o processo: {e}")

if __name__ == "__main__":
    analisar_e_exportar()