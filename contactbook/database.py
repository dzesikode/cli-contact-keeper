from config import SESSION, URI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy_utils import database_exists, create_database


def session() -> Session:
    return SESSION["session"]


def db_connect() -> Session:
    """
    Connect to the sqlite database.
    """
    from contactbook.models import Base
    
    engine = create_engine(URI, echo=False)

    if not database_exists(URI):
        create_database(URI)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)

    session = Session()
    return session
