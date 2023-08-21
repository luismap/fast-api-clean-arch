
from typing import Annotated, List
import logging
from fastapi import APIRouter, Depends, HTTPException,status
from app.auth.oauth2 import get_current_user
from core.db.Postgres import PostgresConn
from core.utils.MyUtils import MyUtils
from features.user.data.models.TokenModel import TokenModel

from features.votes.data.controller.VotesHandler import VotesHandler
from features.votes.data.datasources.VotesAlchemyDS import VotesAlchemyDS
from features.votes.data.models.VotesModel import VoteResponseModel
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
@router.get("/",response_model=List[VoteResponseModel], status_code=status.HTTP_202_ACCEPTED)
def get_votes(token_model: Annotated[TokenModel, Depends(get_current_user)]):
    logger.info(f"retriving votes as user {token_model.user_id}")
    votes = VotesCrud(votes_handler).get_votes()
    if not votes:
        raise HTTPException(404, detail=f"no votes found")
    return votes

@router.get("/my", response_model=List[VoteResponseModel], status_code=status.HTTP_202_ACCEPTED)
def get_my_votes(token_model: Annotated[TokenModel, Depends(get_current_user)]):
    logger.info(f"retriving votes of user {token_model.user_id}")
    votes = VotesCrud(votes_handler).get_my_votes(token_model.user_id)
    if not votes:
        raise HTTPException(404, detail=f"no votes found")
    return votes

@router.get("/vote", response_model=VoteResponseModel, status_code=status.HTTP_200_OK)
def vote(post_id:int, 
         direction:bool, 
         token_model: Annotated[TokenModel, Depends(get_current_user)]):
    user_id = token_model.user_id
    logger.info(f"user f{user_id} voting {direction} for post {post_id}")
    vote = VotesCrud(votes_handler).create_vote(post_id, user_id,direction)

    if (not vote):
        raise HTTPException(status.HTTP_409_CONFLICT, "received None from backend")
    return vote