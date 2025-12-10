import json
import os
import scraper
import database
import analysis

CONFIG_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'config.json')

def main():
    # 1. Ler Configuração
    if not os.path.exists(CONFIG_FILE):
        print("Erro: config.json não encontrado.")
        return

    with open(CONFIG_FILE, 'r') as f:
        config = json.load(f)

    url = config['url']
    limite = config['n_filmes']
    db_name = config['db_name']

    print(f"Configuração carregada. Alvo: {url}")

    # 2. Executar Scraping
    dados = scraper.raspar_imdb(url, limite)

    if not dados:
        print("Nenhum dado coletado. Encerrando.")
        return

    # 3. Configurar Banco e Salvar
    engine = database.configurar_banco(db_name)
    database.salvar_dados(engine, dados)
    database.salvar_series_manuais(engine)

    # 4. Análise e Exportação
    analysis.gerar_relatorios(engine)

    print("\n--- Fluxo Finalizado com Sucesso! ---")

if __name__ == "__main__":
    main()