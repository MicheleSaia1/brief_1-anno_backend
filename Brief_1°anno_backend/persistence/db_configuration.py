from sqlalchemy.orm import DeclarativeBase,sessionmaker
from sqlalchemy import create_engine

class Base(DeclarativeBase):
    pass


engine = create_engine("postgresql://postgres:postgres@localhost/configuratore_auto", echo=True)

SessionLocal=sessionmaker (bind=engine)

def init_db():
    
    print('[LOG]-creazione DATABASE')

    import model.user
    import model.car
    import model.accessories
    import model.engine
    import model.optional
    import model.quote           
    import model.car_configuration


    # Base.metadata.drop_all(bind=engine) #didattico
    Base.metadata.create_all(bind=engine)

def get_session():
    return SessionLocal()