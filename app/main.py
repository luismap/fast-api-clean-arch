from fastapi import Body, FastAPI

import logging
import logging.config
from app.routes import auth, post, user, votes
from core.utils.MyUtils import MyUtils
from features.user.data.controllers.UserHandler import UserHandler
    
canlog = True
appProps = MyUtils.loadProperties("general")["app"]
logger = logging.getLogger(appProps["logger"])

app = FastAPI()

@app.get("/")
def read_root():
    if canlog: logger.info("root got call")
    return {"Hello": "World"}

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(votes.router)