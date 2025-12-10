# Projeto de Scraping e Análise do IMDb Top 250

Este projeto realiza a extração automática (web scraping) de dados do ranking Top 250 filmes do IMDb, armazena as informações em um banco de dados relacional e gera relatórios analíticos em CSV e JSON.

Desenvolvido como parte do Assessment de Python (TP3).

## 🚀 Funcionalidades

1.  **Scraping**: Coleta títulos, anos e notas do IMDb.
2.  **Modelagem**: Utiliza Programação Orientada a Objetos (Classes Movie, Series, TV).
3.  **Persistência**: Salva os dados em banco SQLite usando SQLAlchemy.
4.  **Análise**: Processa os dados com Pandas para gerar classificações e estatísticas.

## 📦 Estrutura do Projeto

- `src/`: Contém todo o código fonte modularizado.
- `data/`: Armazena o banco de dados (`imdb.db`) e os arquivos exportados.
- `exercicios_antigos/`: Contém a evolução do código (exercícios 1 ao 10).

## 🛠️ Instalação

1. Clone o repositório:
   ```bash
   git clone [https://github.com/LuizORAS/TP3-PYTHON_2.git](https://github.com/LuizORAS/TP3-PYTHON_2.git)
2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
3. Execute:
    ```bash
    cd src
    python main.py