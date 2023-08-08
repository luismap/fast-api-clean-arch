
from typing import List
import logging
from fastapi import APIRouter, HTTPException,status
from core.db.Postgres import PostgresConn
from core.utils.MyUtils import MyUtils

from features.votes.data.controller.VotesHandler import VotesHandler
from features.votes.data.datasources.VotesAlchemyDS import VotesAlchemyDS
from features.votes.domain.entities.Votes import VoteResponse
from features.votes.domain.usecase.VotesCrud import VotesCrud

canlog = True
appProps = MyUtils.loadProperties("general")["app"]
logger = logging.getLogger(appProps["logger"])

#db conn
postgreConn = PostgresConn()

#votes handler
votes_alchemy_ds = VotesAlchemyDS(postgreConn)
votes_handler = VotesHandler(votes_alchemy_ds)

router = APIRouter(
    prefix="/votes",
    tags=["votes"]
)

#votes section
@router.get("/",response_model=List[VoteResponse], status_code=status.HTTP_202_ACCEPTED)
def get_votes():
    logger.info(f"retriving votes")
    votes = VotesCrud(votes_handler).get_votes()
    if not votes:
        raise HTTPException(404, detail=f"no votes found")
    return votes