
import logging
from typing import List
from core.db.AlchemySql import Base, SqlAlchemyAccessLayer
from core.db.Postgres import PostgresConn
from core.db.models.AlchemyModels import Votes
from features.votes.data.datasources.api.VotesDataSource import VotesDataSource
from features.votes.domain.entities.Votes import VoteRead, VoteResponse


class VotesAlchemyDS(VotesDataSource):

    def __init__(self, postgres_conn: PostgresConn) -> None:
        self.sqlal = SqlAlchemyAccessLayer(postgres_conn.get_uri_conn())
        Base.metadata.create_all(bind=self.sqlal.engine)
        self.SessionLocal = self.sqlal.SessionLocal
        self.logger = logging.getLogger("api_dev")
        self.logger.info("Alchemy VoteDatasource initialized")

    def get_votes(self) -> List[VoteResponse]:
        with self.SessionLocal() as session:
            votes = session.query(Votes).all()
            for vote in votes:
                print(vote.user_id)
        return votes

    def delete_vote(post_id: int) -> VoteResponse:
        return super().delete_vote()
    
    def get_user_votes(user_id: int) -> List[VoteRead]:
        return super().get_user_votes()