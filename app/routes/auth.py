

import logging
from fastapi import APIRouter, HTTPException, status
from core.db.Postgres import PostgresConn
from core.utils.MyUtils import MyUtils
from features.user.data.controllers.UserHandler import UserHandler
from features.user.data.datasources.UserAlchemyDS import UserAlchemyDS

from features.user.data.models.CredentialsModel import CredentialsModel, CredentialsResponse
from features.user.data.models.UserModel import UserRead
from features.user.domain.usecase.UserCrud import UserCrud

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

@router.post("/login", response_model=CredentialsResponse)
def login(user_credentials: CredentialsModel):
    logger.info(f"retriving user email {user_credentials.email}")
    user = UserCrud(user_handler).get_user_by_email(user_credentials.email)
    logger.info(f"got user {user}")
    if user:
        verification = MyUtils.verify(user_credentials.password, user.password)
        if not verification:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="Invalid Credentials")
    else:
        raise HTTPException(404, detail="Invalid Credentials")
    return user