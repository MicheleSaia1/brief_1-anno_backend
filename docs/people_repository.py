from sqlalchemy import select

from model.people import People




def get_all(session):
    return session.execute(select()).scalars().all() #di questa tabella mi devi prendere tutti i dati



def get_by_id (session,):
    return session.get()# veicolo id è la PK






#create
def create(session,):
    session.add()
    session.commit()
    return 


#DELETE
def delete_by_id(session, ):
    session.delete()
    session.commit



#PUT
def update(session,):
    session.commit()
    return  #aggiorna automaticamente , ci pensa il session 