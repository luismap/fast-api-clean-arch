
import logging
from fastapi import APIRouter, HTTPException,status
from core.db.Postgres import PostgresConn
from core.utils.MyUtils import MyUtils
from features.user.data.controllers.UserHandler import UserHandler
from features.user.data.datasources.UserAlchemyDS import UserAlchemyDS
import features.user.data.models.UserModel as um
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
    prefix="/user"
)

#user section
@router.get("/{id}",response_model=um.UserResponse, status_code=status.HTTP_202_ACCEPTED)
def get_user(id: int):
    logger.info(f"retriving user id {id}")
    user = UserCrud(user_handler).get_user(id)
    if not user:
        raise HTTPException(404, detail=f"user id: {id} not found")
    return user


@router.post("/create",status_code=status.HTTP_201_CREATED, response_model=um.UserResponse)
def create_post(payload: um.UserCreate):
    payload.password = MyUtils.hash(payload.password)
    logger.info(payload)
    parsedData = UserCrud(user_handler).create_user(payload)
    if not parsedData:
        raise HTTPException(404, "not able to create user")
    return parsedData