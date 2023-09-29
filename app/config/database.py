"""Load Database."""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config import config

settings = config.get_settings()

engine = create_engine(settings.sqlalchemy_database_uri)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def create_db():
    """Create database from models."""
    Base.metadata.create_all(bind=engine)


def get_db():
    """Return DB Session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
