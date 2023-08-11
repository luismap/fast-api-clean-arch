
from pydantic import BaseModel

from features.votes.domain.entities.Vote import Vote


class VoteModel(Vote):
    pass

class VoteReadModel(Vote):
    pass

class VoteResponseModel(BaseModel):
    user_id: int
    post_id: int

    class Config:
        orm_mode=True