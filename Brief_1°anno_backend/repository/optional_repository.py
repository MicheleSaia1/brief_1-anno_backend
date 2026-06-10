from sqlalchemy import select
from model.optional import Optional


def get_all(session):
    return session.execute(select(Optional)).scalars().all()


def get_by_id(session, id_optional):
    return session.get(Optional, id_optional)


def create(session, optional):
    session.add(optional)
    session.commit()
    session.refresh(optional)
    return optional


def update(session, optional):
    session.commit()
    session.refresh(optional)
    return optional


def delete_by_id(session, id_optional):
    opt = session.get(Optional, id_optional)
    if opt is None:
        return False
    session.delete(opt)
    session.commit()
    return True