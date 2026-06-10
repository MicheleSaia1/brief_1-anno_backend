from sqlalchemy import select
from model.car_configuration import Car_Configuration


def get_all(session):
    return session.execute(select(Car_Configuration)).scalars().all()


def get_by_id(session, id_configuration):
    return session.get(Car_Configuration, id_configuration)

# Restituisce tutte le configurazioni di un utente specifico
def get_by_user(session, user_id):
     return session.execute(
        select(Car_Configuration).filter_by(user_id=user_id)
    ).scalars().all()
   


def create(session, config):
    session.add(config)
    session.commit()
    session.refresh(config)
    return config


def delete_by_id(session, id_configuration):
    config = session.get(Car_Configuration, id_configuration)
    if config is None:
        return False
    session.delete(config)
    session.commit()
    return True