from sqlalchemy import select
from model.accessories import Accessories


def get_all(session):
    return session.execute(select(Accessories)).scalars().all()


def get_by_id(session, id_accessories):
    return session.get(Accessories, id_accessories)


def get_by_brand(session, brand):
    return session.execute(select(Accessories).filter_by(accessories_brand=brand)).scalars().all()


def create(session, accessory):
    session.add(accessory)
    session.commit()
    session.refresh(accessory)
    return accessory


def update(session, accessory):
    session.commit()
    session.refresh(accessory)
    return accessory


def delete_by_id(session, id_accessories):
    accessory = session.get(Accessories, id_accessories)
    if accessory is None:
        return False
    session.delete(accessory)
    session.commit()
    return True
