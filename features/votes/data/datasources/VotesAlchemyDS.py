
import logging
from typing import List
from core.db.AlchemySql import Base, SqlAlchemyAccessLayer
from core.db.Postgres import PostgresConn
from core.db.models.AlchemyModels import Votes
from features.votes.data.datasources.api.VotesDataSource import VotesDataSource
from features.votes.data.models.VotesModel import VoteReadModel, VoteResponseModel


class VotesAlchemyDS(VotesDataSource):

    def __init__(self, postgres_conn: PostgresConn) -> None:
        self.sqlal = SqlAlchemyAccessLayer(postgres_conn.get_uri_conn())
        Base.metadata.create_all(bind=self.sqlal.engine)
        self.SessionLocal = self.sqlal.SessionLocal
        self.logger = logging.getLogger("api_dev")
        self.logger.info("Alchemy VoteDatasource initialized")

    def get_votes(self) -> List[VoteResponseModel]:
        with self.SessionLocal() as session:
            votes = session.query(Votes).all()
        return votes

    def delete_vote(post_id: int) -> VoteResponseModel:
        return super().delete_vote()
    
    def get_my_votes(self, user_id: int) -> List[VoteReadModel]:
        with self.SessionLocal() as session:
            votes = session.query(Votes).filter(Votes.user_id == user_id).all()
        return votes