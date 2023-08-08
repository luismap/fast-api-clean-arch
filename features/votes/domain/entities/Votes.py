
from pydantic import BaseModel


class VoteBase(BaseModel):
    """common attributes while creating or reading data.
    """
    user_id: int
    post_id: int

class Vote(VoteBase):
    pass

class VoteRead(VoteBase):
    pass

class VoteResponse(BaseModel):
    user_id: int
    post_id: int

    class Config:
        orm_mode=True