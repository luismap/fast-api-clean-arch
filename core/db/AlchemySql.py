from core.db.Postgres import PostgresConn
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sqlAlchemyDatabaseUrl = PostgresConn().get_uri_conn()

engine = create_engine(sqlAlchemyDatabaseUrl)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()