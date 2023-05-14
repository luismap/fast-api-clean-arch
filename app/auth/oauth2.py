from datetime import timedelta, datetime
from typing import Union

from jose import jwt
from core.utils.MyUtils import MyUtils

SECRET_KEY = MyUtils.loadProperties("secret_key")
ALGORITHM = MyUtils.loadProperties("algorithm")

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt