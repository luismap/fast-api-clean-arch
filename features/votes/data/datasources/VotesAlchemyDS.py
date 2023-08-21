
import logging
from typing import List

from fastapi import HTTPException, status
from sqlalchemy import delete
from core.db.AlchemySql import Base, SqlAlchemyAccessLayer
from core.db.Postgres import PostgresConn
from core.db.models.AlchemyModels import Votes
from features.votes.data.datasources.api.VotesDataSource import VotesDataSource
from features.votes.data.models.VotesModel import VoteModel, VoteReadModel, VoteResponseModel


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

    def delete_vote(self, post_id: int, user_id: int) -> bool:
        with self.SessionLocal() as session:
            try:
                session.query(Votes).filter(
                    Votes.user_id==user_id, Votes.post_id==post_id
                ).delete()
                session.commit()
                return True
            except Exception as e:
                logging.info(e)
                return False
    
    def get_my_votes(self, user_id: int) -> List[VoteReadModel]:
        with self.SessionLocal() as session:
            votes = session.query(Votes).filter(Votes.user_id == user_id).all()
        return votes
    
    def create_vote(self,vote:VoteModel)-> VoteReadModel:
        with self.SessionLocal() as session:
            try:
                session.add(Votes(**vote.dict()))
                session.commit()
            except Exception as e:
                logging.info(e)
                raise HTTPException(status.HTTP_409_CONFLICT, "conflict while adding vote")

        return vote
    
    def vote(self, post_id: int, user_id: int, direction: bool) -> VoteReadModel:
        find_post = lambda vote: vote.post_id == post_id
        voted = list(filter(find_post, self.get_my_votes(user_id)))
        vote_model = VoteModel.from_orm(voted[0]) if voted else None
        logging.info(f"found vote {vote_model}")
        ans = None
        if(direction):
            logging.info("upvoting")
            if (not vote_model):
                logging.info("creating vote")
                ans = self.create_vote(VoteModel(user_id=user_id, post_id=post_id))
            else:
                raise HTTPException(status.HTTP_409_CONFLICT, f"vote already exist for post_id {post_id}")
        else:
            logging.info("downvoting")
            if (not vote_model):
                raise HTTPException(status.HTTP_404_NOT_FOUND, f"post_id {post_id} not found for user {user_id}")
            else:
                deleted = self.delete_vote(post_id, user_id)
                if (deleted):
                    ans = VoteReadModel(user_id=user_id, post_id=post_id)

        return ans