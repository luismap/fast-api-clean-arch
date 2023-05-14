from datetime import timedelta
import datetime
from typing import Union

from jose import JWTError
from pydantic import BaseModel
from core.utils.MyUtils import MyUtils

SECRET_KEY = MyUtils.loadProperties("secret_key")
ALGORITHM = MyUtils.loadProperties("algorithm")

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = JWTError.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt