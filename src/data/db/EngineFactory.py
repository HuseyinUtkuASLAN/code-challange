from sqlalchemy import Column, Text, create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SessionFactory:
    def __init__(self) -> None:
        # this is just for the sake of example. Dont leave credentials in the source code
        self._userName = "postgres"
        self._password = "postgres"
        self._database = "email_events"
        self._ip = "localhost"

    def create(self): 

        url = f'postgresql+psycopg2://{self._userName}:{self._password}@{self._ip}/{self._database}'
        if not database_exists(url):
            create_database(url)
        engine = create_engine(url, pool_size = 50, echo=False)

        Base.metadata.create_all(engine)

        session = sessionmaker()
        session.configure(bind=engine)
        return session()


class EmailEvents(Base):
    __tablename__ = "EmailEvents"
    
    id = Column(Text, primary_key=True, nullable=False)
    event = Column(Text)
    content = Column(Text)
