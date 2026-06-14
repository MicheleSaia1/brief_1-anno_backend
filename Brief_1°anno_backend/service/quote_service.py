from model.quote import Quote
from repository import quote_repository



def create_quote(session, car_id: int, user_id: int) -> Quote:
   

    
    new_quote = Quote(
        car_id=car_id,
        user_id=user_id
    )

    return quote_repository.create(session, new_quote)


def get_user_quotes(session, user_id: int) -> list:
    """
    Restituisce tutte le Quote di un utente (bozze e finalizzate).
    """
    return quote_repository.get_by_user(session, user_id)


def get_quote_by_id(session, quote_id: int) -> Quote:
    """
    Restituisce una Quote specifica. Lancia errore se non esiste.
    """
    quote = quote_repository.get_by_id(session, quote_id)
    if quote is None:
        raise ValueError(f"Quote #{quote_id} non trovata")
    return quote