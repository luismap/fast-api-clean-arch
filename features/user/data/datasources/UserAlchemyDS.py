import logging
from core.db.AlchemySql import SqlAlchemyAccessLayer, Base
from core.db.Postgres import PostgresConn
from features.user.data.datasources.api.UserDataSource import UserDataSource

from core.db.models.AlchemyModels import UserAlmy
import features.user.data.models.UserModel as um

class UserAlchemyDS(UserDataSource):
        
    def __init__(self, postgres_conn: PostgresConn) -> None:
        self.sqlal = SqlAlchemyAccessLayer(postgres_conn.get_uri_conn())
        Base.metadata.create_all(bind=self.sqlal.engine)
        self.SessionLocal = self.sqlal.SessionLocal
        self.logger = logging.getLogger("api_dev")
        self.logger.info("Alchemy UserDatasource initialized")

    def get_user(self, id: int) -> um.UserRead:
        with self.SessionLocal() as session:
            user = session.query(UserAlmy).filter(UserAlmy.user_id == id).first()
        return user
    
    def is_available() -> bool:
        return True

    def create_user(self, payload: um.UserCreate) -> um.UserRead :
        inserted = None
        with self.SessionLocal() as session:
            try:
                session.add(UserAlmy(**payload.dict()))
                session.commit()
                session.flush()
                inserted = session.query(UserAlmy).filter(UserAlmy.email==payload.email).first()
            except Exception as e:
                self.logger.error(f"exception: {e}")
                session.rollback()
                session.flush()
        return inserted

    def get_user_by_email(self,email: str) -> um.UserRead:
        with self.SessionLocal() as session:
            try:
                user = session.query(UserAlmy).filter(UserAlmy.email == email).first()
                self.logger.info(f"retrieved user {user}")
            except Exception as e:
                self.logger.error(f"exception: {e}")
            return user if user else None

 