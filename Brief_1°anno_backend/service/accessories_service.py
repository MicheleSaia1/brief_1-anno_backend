from model.accessories import Accessories
from repository import accessories_repository





def get_all(session) -> list:
    return accessories_repository.get_all(session)


def get_by_id(session, id_accessories: int) -> Accessories:
    accessory = accessories_repository.get_by_id(session, id_accessories)
    if accessory is None:
        raise ValueError(f"Accessorio #{id_accessories} non trovato")
    return accessory


def get_compatible_with_car(session, car) -> list:
    
    return car.accessories


def create(session, data: dict) -> Accessories:
    for field in ['accessories_brand', 'price']:
        if field not in data:
            raise ValueError(f"empty field, write something: {field}")

    new_accessory = Accessories(
        accessories_brand=data['accessories_brand'],
        price=data['price'],
        year_production=data.get('year_production')  # opzionale
    )

    return accessories_repository.create(session, new_accessory)


def delete(session, id_accessories: int) -> bool:
    return accessories_repository.delete_by_id(session, id_accessories)