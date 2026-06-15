from model.engine import Engine
from repository import engine_repository




def get_all(session) -> list:
    return engine_repository.get_all(session)


def get_by_id(session, id_engine: int) -> Engine:
    engine = engine_repository.get_by_id(session, id_engine)
    if engine is None:
        raise ValueError(f"engine {id_engine} not found")
    return engine


def get_compatible_with_car(session, car) -> list:
   
    return car.engine


def create(session, data: dict) -> Engine:
    for field in ['brand_engine', 'price']:
        if field not in data:
            raise ValueError(f"empty field, write something: {field}")

    new_engine = Engine(
        brand_engine=data['brand_engine'],
        price=data['price'],
        horsepower=data.get('horsepower'),      
        displacement_cc=data.get('displacement_cc'),  
        production_year=data.get('production_year')   
    )

    return engine_repository.create(session, new_engine)


def delete(session, id_engine: int) -> bool:
    return engine_repository.delete_by_id(session, id_engine)