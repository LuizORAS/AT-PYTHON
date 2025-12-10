import pandas as pd

def classificar_nota(nota):
    if nota >= 9.0: return "Obra-prima"
    elif nota >= 8.0: return "Excelente"
    elif nota >= 7.0: return "Bom"
    else: return "Mediano"

def gerar_relatorios(engine):
    print("\n--- Iniciando Análise de Dados ---")
    try:
        df = pd.read_sql_table('movies', con=engine)
        
        # 1. Criar categoria
        df['categoria'] = df['rating'].apply(classificar_nota)
        
        # 2. Filtrar Top Filmes
        top_filmes = df[df['rating'] > 9.0].sort_values(by='rating', ascending=False)
        print("Top 3 Filmes encontrados:")
        print(top_filmes[['title', 'rating']].head(3))
        
        # 3. Gerar CSV
        df.to_csv('relatorio_completo.csv', index=False)
        print("Arquivo 'relatorio_completo.csv' gerado com sucesso.")
        
        # 4. Tabela Cruzada
        resumo = pd.crosstab(df['year'], df['categoria'])
        print("\nResumo por Ano (últimos 5 anos presentes):")
        print(resumo.tail(5))
        
    except Exception as e:
        print(f"Erro na análise: {e}")