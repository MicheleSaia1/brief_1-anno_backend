from sqlalchemy import select
from model.car import Car
 
 
 
 
def get_all(session):
    return session.execute(select(Car)).scalars().all()
 
 
def get_by_id(session, car_id):
   
    return session.get(Car, car_id)
 
 
def get_by_brand(session, brand):
  
    return session.execute(select(Car).filter_by(car_brand=brand)).scalars().all()
 
 
def create(session, car):
    session.add(car)     
    session.commit()     
    session.refresh(car) 
    return car
 
 
def delete_by_id(session, car_id):
    car = session.get(Car, car_id)
    if car is None:
        return False       
    session.delete(car)
    session.commit()
    return True
 
 
def update(session, car):
    
    session.commit()
    session.refresh(car)
    return car



#PUT
def update(session,):
    session.commit()
    return 