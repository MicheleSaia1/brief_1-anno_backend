from model.car import Car
from repository import car_repository





def get_all_cars(session) -> list:
    return car_repository.get_all(session)


def get_car_by_id(session, car_id: int) -> Car:
    car = car_repository.get_by_id(session, car_id)
    if car is None:
        raise ValueError(f"Auto #{car_id} non trovata")
    return car


def get_cars_by_brand(session, brand: str) -> list:
    return car_repository.get_by_brand(session, brand)


def create_car(session, data: dict) -> Car:
    
    for field in ['car_brand', 'car_model', 'car_start_price']:
        if field not in data:
            raise ValueError(f"empty field, write something: {field}")

    new_car = Car(
        car_brand=data['car_brand'],
        car_model=data['car_model'],
        car_start_price=data['car_start_price']
    )

    return car_repository.create(session, new_car)


def delete_car(session, car_id: int) -> bool:

    return car_repository.delete_by_id(session, car_id)