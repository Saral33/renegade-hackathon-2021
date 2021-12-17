from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()


SQLALCHEMY_URL = 'postgresql://postgres:Python123@localhost/fast_api'

engine = create_engine(SQLALCHEMY_URL)

session_local = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()