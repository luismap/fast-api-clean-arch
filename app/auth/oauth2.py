from datetime import timedelta, datetime
import logging
from typing import Annotated, Union
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt
from core.utils.MyUtils import MyUtils
from features.user.data.models.TokenModel import TokenData, TokenModel

SECRET_KEY = MyUtils.loadProperties("secret_key")
ALGORITHM = MyUtils.loadProperties("algorithm")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") #returns only the token string

appProps = MyUtils.loadProperties("general")["app"]
logger = logging.getLogger(appProps["logger"])

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
        user_id = data["user_id"]
    to_encode.update({"exp": expire, "user_id":user_id})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str, credentials_exception: Exception) -> TokenData:
    try:
        logger.info(f"verifying access for token {token}")
        payload = jwt.decode(token,SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        logger.info(f"decoded user_id {token}")

        if not user_id:
            raise credentials_exception
        token_data = TokenData(user_id=user_id)
    except JWTError as e:
        logger.info(f"got error: {e}")
        raise credentials_exception
    return token_data

def get_current_user(token: str = Depends(oauth2_scheme) ) -> TokenData:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    logger.info(f"got TokenModel {token}")
    return verify_access_token(token,credentials_exception)