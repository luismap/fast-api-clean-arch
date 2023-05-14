from datetime import timedelta, datetime
from typing import Union
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt
from core.utils.MyUtils import MyUtils
from features.user.data.models.TokenModel import TokenData

SECRET_KEY = MyUtils.loadProperties("secret_key")
ALGORITHM = MyUtils.loadProperties("algorithm")
oauth2_scheme= OAuth2PasswordBearer("login")

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=[ALGORITHM])
    return encoded_jwt

def verify_access_token(token: str, credentials_exception: Exception):
    try:
        payload = jwt.decode(token,SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        if not id:
            raise credentials_exception
        token_data = TokenData(user_id=user_id)
    except JWTError:
        raise credentials_exception
    return token_data

def get_current_user(token: str = Depends(oauth2_scheme) ):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_access_token(token,credentials_exception)