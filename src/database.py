from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError

Base = declarative_base()

# Modelos do SQLAlchemy (Tabelas)
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

def configurar_banco(nome_db):
    engine = create_engine(f'sqlite:///{nome_db}', echo=False)
    Base.metadata.create_all(engine)
    return engine

def salvar_dados(engine, lista_filmes):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    print("--- Salvando no Banco de Dados ---")
    count_novos = 0
    
    for item in lista_filmes:
        try:
            nota_float = float(item['nota'])
        except:
            nota_float = 0.0

        novo_filme = MovieModel(
            title=item['titulo'],
            year=item['ano'],
            rating=nota_float
        )
        
        try:
            session.add(novo_filme)
            session.commit()
            count_novos += 1
        except IntegrityError:
            session.rollback()
            # print(f"Duplicado ignorado: {item['titulo']}")
    
    print(f"Total de novos filmes inseridos: {count_novos}")
    session.close()

def salvar_series_manuais(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Criando 2 séries de exemplo para ter dados na tabela de séries
    series = [
        SeriesModel(title="Breaking Bad", year="2008", seasons=5, episodes=62),
        SeriesModel(title="Game of Thrones", year="2011", seasons=8, episodes=73)
    ]
    
    for s in series:
        try:
            session.add(s)
            session.commit()
        except IntegrityError:
            session.rollback()
    session.close()