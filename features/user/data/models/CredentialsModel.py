

from pydantic import BaseModel, EmailStr
from features.user.domain.entities.Credentials import Credentials


class CredentialsModel(Credentials):
    pass

class CredentialsResponse(BaseModel):
    email: EmailStr

    class Config:
        orm_mode = True