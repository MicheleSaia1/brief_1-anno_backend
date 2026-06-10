from sqlalchemy import select
from model.user import User
 
 
def get_all(session):
    return session.execute(select(User)).scalars().all()
 
 
def get_by_id(session, id_user) :
    return session.get(User, id_user)
 
 
def get_by_email(session, email):
    return session.execute(select(User).filter_by(email=email)).scalars().first()
 
 
def get_by_username(session, username):
    return session.execute(select(User).filter_by(username=username)).scalars().first()
 
 
def create(session, user) :
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
 
 
def update(session, user):
    session.commit()
    session.refresh(user)
    return user
 
 
def delete_by_id(session, id_user):
    user = session.get(User, id_user)
    if user is None:
        return False
    session.delete(user)
    session.commit()
    return True