

from pydantic import BaseModel
from pydantic import EmailStr


class Credentials(BaseModel):
    email: EmailStr