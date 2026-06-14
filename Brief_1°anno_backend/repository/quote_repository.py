from sqlalchemy import select
from model.quote import Quote


def get_all(session) -> list:
    return session.execute(select(Quote)).scalars().all()


def get_by_id(session, quote_id: int) -> Quote | None:
    return session.get(Quote, quote_id)


def get_by_user(session, user_id: int) -> list:
    return session.execute(
        select(Quote).filter_by(user_id=user_id)
    ).scalars().all()


def create(session, quote: Quote) -> Quote:
    session.add(quote)
    session.commit()
    session.refresh(quote)
    return quote


def delete_by_id(session, quote_id: int) -> bool:
    quote = session.get(Quote, quote_id)
    if quote is None:
        return False
    session.delete(quote)
    session.commit()
    return True