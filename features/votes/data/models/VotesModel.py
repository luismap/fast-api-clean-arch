
from pydantic import BaseModel

from features.votes.domain.entities.Vote import Vote


class VoteModel(Vote):
    class Config:
        orm_mode=True

class VoteReadModel(Vote):
    class Config:
        orm_mode=True

class VoteResponseModel(BaseModel):
    user_id: int
    post_id: int

    class Config:
        orm_mode=True