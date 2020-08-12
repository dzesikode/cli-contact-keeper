from models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def db_connect():
    # Connect to the engine.
    engine = create_engine('sqlite:///contact_book.db', echo=False)


    # Create a schema
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)

    # Instantiate when you need to connect with the database
    session = Session()

    return session
