from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from sqlalchemy import create_engine

engine = create_engine('sqlite:////tmp/test.db')
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # we import our db models so they will be registered properly on the metadata
    # before calling init_db()
    import app.models
    Base.metadata.create_all(bind=engine)