


import logging
from core.db.AlchemySql import SqlAlchemyAccessLayer, Base
from core.db.Postgres import PostgresConn
from features.posts.data.datasources.api.UserDataSource import UserDataSource
from features.posts.domain.entities.User import UserModel
from core.db.models.AlchemyModels import UserAlmy

class UserAlchemyDS(UserDataSource):
        
    def __init__(self, postgres_conn: PostgresConn) -> None:
        self.sqlal = SqlAlchemyAccessLayer(postgres_conn.get_uri_conn())
        Base.metadata.create_all(bind=self.sqlal.engine)
        self.SessionLocal = self.sqlal.SessionLocal
        self.logger = logging.getLogger("api_dev")
        self.logger.info("Alchemy UserDatasource initialized")    


    def get_user(self, id: int) -> UserModel:
        with self.SessionLocal() as session:
            user = session.query(UserAlmy).filter(UserAlmy.user_id == id).first()
        return user
    
    def is_available() -> bool:
        return True