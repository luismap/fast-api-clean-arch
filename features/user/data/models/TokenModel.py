from typing import Union
from pydantic import BaseModel
from features.user.domain.entities.Token import Token


class TokenModel(Token):
    pass

class TokenData(BaseModel):
    user_id: Union[str, None] = None