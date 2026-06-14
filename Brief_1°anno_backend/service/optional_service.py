from model.optional import Optional
from repository import optional_repository




def get_all(session) -> list:
    return optional_repository.get_all(session)


def get_by_id(session, id_optional: int) -> Optional:
    optional = optional_repository.get_by_id(session, id_optional)
    if optional is None:
        raise ValueError(f"Optional #{id_optional} non trovato")
    return optional


def get_compatible_with_car(session, car) -> list:
   
    return car.optional


def create(session, data: dict) -> Optional:
    for field in ['brand_optional', 'price']:
        if field not in data:
            raise ValueError(f"empty field, write something: {field}")

    new_optional = Optional(
        brand_optional=data['brand_optional'],
        price=data['price'],
        production_year=data.get('production_year')  # opzionale
    )

    return optional_repository.create(session, new_optional)


def delete(session, id_optional: int) -> bool:
    return optional_repository.delete_by_id(session, id_optional)