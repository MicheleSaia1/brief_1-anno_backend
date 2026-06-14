from repository import car_configuration_repository




def get_all(session) -> list:
    return car_configuration_repository.get_all(session)


def get_by_id(session, id_configuration: int):
  
    config = car_configuration_repository.get_by_id(session, id_configuration)
    if config is None:
        raise ValueError(f"configuration {id_configuration} not found")
    return config


def get_by_user(session, user_id: int) -> list:

    return car_configuration_repository.get_by_user(session, user_id)


def delete(session, id_configuration: int) -> bool:
   
    return car_configuration_repository.delete_by_id(session, id_configuration)