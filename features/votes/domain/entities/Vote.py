
from pydantic import BaseModel


class Vote(BaseModel):
    """common attributes while creating or reading data.
    """
    user_id: int
    post_id: int

