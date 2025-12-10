import pandas as pd
from sqlalchemy import create_engine

def classificar_nota(nota):
    """
    Recebe um valor float (ex: 9.2) e retorna uma string de categoria.
    """
    if nota >= 9.0:
        return "Obra-prima"
    elif nota >= 8.0:
        return "Excelente"
    elif nota >= 7.0:
        return "Bom"
    else:
        return "Mediano"

def processar_categorias():
    db_name = 'imdb.db'
    
    try:
        engine = create_engine(f'sqlite:///{db_name}', echo=False)
        print("--- Carregando filmes do banco ---")
        df_movies = pd.read_sql_table('movies', con=engine)
        df_movies = df_movies.sort_values(by='rating', ascending=False)
        df_movies['categoria'] = df_movies['rating'].apply(classificar_nota)
        print("\n--- Classificação dos Top 10 Filmes ---")
        colunas_para_mostrar = ['title', 'rating', 'categoria']
        
        print(df_movies[colunas_para_mostrar].head(10))

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    processar_categorias()