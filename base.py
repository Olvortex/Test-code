from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base()
metadata = Base.metadata

# db
engine = create_engine('sqlite:///database.db')
session = Session(bind = engine)