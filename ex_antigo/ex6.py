import sys
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError

try:
    from ex2 import raspar_imdb
except ImportError:
    print("Erro: Certifique-se de que ex2.py está na mesma pasta.")
    sys.exit()

engine = create_engine('sqlite:///imdb.db', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class MovieModel(Base):
    __tablename__ = 'movies'
    
    id = Column(Integer, primary_key=True)

    title = Column(String, unique=True, nullable=False) 
    year = Column(String)
    rating = Column(Float)

class SeriesModel(Base):
    __tablename__ = 'series'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)
    year = Column(String)
    seasons = Column(Integer)
    episodes = Column(Integer)

Base.metadata.create_all(engine)



def popular_banco():
    print("--- Iniciando Povoamento do Banco de Dados ---")
    

    print("Obtendo dados do IMDb...")
    lista_dicionarios = raspar_imdb() 

    for item in lista_dicionarios:

        try:
            nota_float = float(item['nota'])
        except:
            nota_float = 0.0

        novo_filme = MovieModel(
            title=item['titulo'],
            year=item['ano'],
            rating=nota_float
        )
        salvar_com_seguranca(novo_filme)

    series_manuais = [
        SeriesModel(title="Breaking Bad", year="2008", seasons=5, episodes=62),
        SeriesModel(title="Game of Thrones", year="2011", seasons=8, episodes=73),
        SeriesModel(title="The Office", year="2005", seasons=9, episodes=201)
    ]

    for serie in series_manuais:
        salvar_com_seguranca(serie)

def salvar_com_seguranca(objeto):
    """
    Tenta salvar um objeto no banco. 
    Se já existir (duplicado), faz rollback e avisa.
    """
    try:
        session.add(objeto)
        session.commit()
        print(f"[SUCESSO] Inserido: {objeto.title}")
    except IntegrityError:
        session.rollback() 
        print(f"[DUPLICADO] O título já existe: {objeto.title}")
    except Exception as e:
        session.rollback()
        print(f"[ERRO] Falha ao inserir {objeto.title}: {e}")

if __name__ == "__main__":
    popular_banco()
    print("\nProcesso finalizado. Verifique o arquivo 'imdb.db'.")