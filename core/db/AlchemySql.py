from core.db.Postgres import PostgresConn
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

class SqlAlchemyAccessLayer:
    def __init__(self, conn: str) -> None:
        self.sqlAlchemyDatabaseUrl = conn
        self.engine = create_engine(self.sqlAlchemyDatabaseUrl)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

Base = declarative_base()