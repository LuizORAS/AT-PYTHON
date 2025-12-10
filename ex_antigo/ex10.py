import pandas as pd
from sqlalchemy import create_engine

def classificar_nota(nota):
    if nota >= 9.0:
        return "Obra-prima"
    elif nota >= 8.0:
        return "Excelente"
    elif nota >= 7.0:
        return "Bom"
    else:
        return "Mediano"

def gerar_resumo():
    db_name = 'imdb.db'
    engine = create_engine(f'sqlite:///{db_name}', echo=False)
    try:

        print("--- Carregando dados... ---")
        df_movies = pd.read_sql_table('movies', con=engine)
        df_movies['categoria'] = df_movies['rating'].apply(classificar_nota)
        resumo = pd.crosstab(
            index=df_movies['year'], 
            columns=df_movies['categoria'],
            margins=True,
            margins_name="Total"
        )
        print("\n--- Resumo: Quantidade de Filmes por Ano e Categoria ---")
        print(resumo.tail(20))
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    gerar_resumo()