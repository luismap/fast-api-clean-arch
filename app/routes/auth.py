

import logging
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from app.auth.oauth2 import create_access_token
from core.db.Postgres import PostgresConn
from core.utils.MyUtils import MyUtils
from features.user.data.controllers.UserHandler import UserHandler
from features.user.data.datasources.UserAlchemyDS import UserAlchemyDS

from features.user.data.models.CredentialsModel import CredentialsModel, CredentialsResponse
from features.user.data.models.TokenModel import TokenModel
from features.user.data.models.UserModel import UserRead
from features.user.domain.usecase.UserCrud import UserCrud
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

canlog = True
appProps = MyUtils.loadProperties("general")["app"]
logger = logging.getLogger(appProps["logger"])

#db conn
postgreConn = PostgresConn()

#user handler
user_alchemy_ds = UserAlchemyDS(postgreConn)
user_handler = UserHandler(user_alchemy_ds)

router = APIRouter(
    tags=["Authentication"]
)

@router.post("/login", response_model=TokenModel)
def login(user_cred: OAuth2PasswordRequestForm = Depends()):
    logger.info(f"retriving user email {user_cred.username}")
    user = UserCrud(user_handler).get_user_by_email(user_cred.username)
    logger.info(f"got user {user}")
    if user:
        verification = MyUtils.verify(user_cred.password, user.password)
        if not verification:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                             detail="Invalid Credentials")
        else:
            access_token = create_access_token(
                {"user_id": user.user_id}
                )
    else:
        raise HTTPException(403, detail="Invalid Credentials")

    return {"access_token": access_token, "token_type": "bearer"}