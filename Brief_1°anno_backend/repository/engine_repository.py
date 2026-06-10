from sqlalchemy import select
from model.engine import Engine
 
 
def get_all(session):
    return session.execute(select(Engine)).scalars().all()
 
 
def get_by_id(session, id_engine):
    return session.get(Engine, id_engine)
 
 
def create(session, engine):
    session.add(engine)
    session.commit()
    session.refresh(engine)
    return engine
 
 
def update(session, engine):
    session.commit()
    session.refresh(engine)
    return engine
 
 
def delete_by_id(session, id_engine):
    engine = session.get(Engine, id_engine)
    if engine is None:
        return False
    session.delete(engine)
    session.commit()
    return True
 