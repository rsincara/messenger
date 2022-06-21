from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

USER = getenv("POSTGRES_USER", "postgres")
PASSWORD = getenv("POSTGRES_PASSWORD", "postgres")
DB_PORT = getenv("DB_PORT", "5432")
DB_NAME = getenv("POSTGRES_DB", "messenger")

db_url = f"postgresql://{USER}:{PASSWORD}@localhost:{DB_PORT}/{DB_NAME}"
# sqllite_url = "sqlite://"
engine = create_engine(db_url)
session = sessionmaker(engine)
