import imp
from typing import List
from fastapi import Body, FastAPI, HTTPException, status

import logging
import logging.config
import yaml
from core.db.Postgres import PostgresConn
from core.utils.MyUtils import MyUtils
from features.posts.data.controllers.UserHandler import UserHandler
from features.posts.data.controllers.UserPostController import UserPostController
from features.posts.data.datasources.PostsAlchemyDS import PostsAlchemyDS
from features.posts.data.datasources.PostsLocalDS import PostsLocalDataSource
from features.posts.data.datasources.PostsPostgresDS import PostsPostgresDS
from features.posts.data.datasources.UserAlchemyDS import UserAlchemyDS
from features.posts.data.models.PostCreateModel import PostCreateModel
from features.posts.data.models.PostResponseModel import PostResponseModel
import features.posts.data.models.UserModel as um
from features.posts.domain.usecases.CreatePosts import CreatePosts
from features.posts.domain.usecases.DeletePosts import DeletePost
from features.posts.domain.usecases.GetPosts import GetPosts
from features.posts.domain.usecases.GetPostsById import GetPostsById
from features.posts.domain.usecases.GetPostsIds import GetPostsIds
from features.posts.domain.usecases.UserCrud import UserCrud
from features.posts.domain.usecases.UpdatePosts import UpdatePosts
from fastapi import Depends
from sqlalchemy.orm import Session
 

canlog = True
appProps = MyUtils.loadProperties("general")["app"]

# Initialize the logger once as the application starts up.
with open("logging.yaml", 'rt') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
 
# Get an instance of the logger and use it to write a log!
# Note: Do this AFTER the config is loaded above or it won't use the config.
logger = logging.getLogger(appProps["logger"])
logger.info("Configured the logger!")

app = FastAPI()

postgreConn = PostgresConn()
# user postController

alchemyDS = PostsAlchemyDS(postgreConn)
localDS = PostsLocalDataSource()
postgresDS = PostsPostgresDS()
userPostController = UserPostController(localDS, postgresDS, alchemyDS)

#user handler
user_alchemy_ds = UserAlchemyDS(postgreConn)
user_handler = UserHandler(user_alchemy_ds)

@app.get("/")
def read_root():
    if canlog: logger.info("root got call")
    return {"Hello": "World"}

@app.get("/posts", response_model=List[PostResponseModel])
def get_posts():
    parsedData = GetPosts(userPostController).getPosts()
    logger.info(parsedData)
    return parsedData

@app.post("/createpost",status_code=201)
def create_post(payload: PostCreateModel):
    logger.info(payload)
    parsedData = CreatePosts(userPostController).createPosts(payload)
    if not parsedData:
        raise HTTPException(404, "not able to create post")
    return {"added": parsedData}

@app.get("/posts/ids")
def get_post():
    ids = GetPostsIds(userPostController).getPostsIds()
    logger.info(ids)
    return {"postsIds": ids}

@app.get("/posts/{id}", response_model=PostResponseModel)
def get_post_id(id: int):
    logger.info(f"retriving id {id}")
    post = GetPostsById(userPostController).getPostById(id)
    if not post: 
        raise HTTPException(404, detail=f"post id: {id} not found")
    return post

@app.delete("/posts/{id}")
def delete_post(id: int):
    logger.info(f"deleting post with id: {id}")
    deleted = DeletePost(userPostController).deletePost(id)
    if not deleted:
        raise HTTPException(404, detail=f"fail to delete id {id}")
    return {"deleted": deleted}

@app.put("/post/{id}")
def update_post(id: int, post: dict):
    logger.info(f"updating for id {id} with data {post} type {type(post)}")
    if not id: 
        raise HTTPException(404, detail=f"post id: {id} not passed")
    updated = UpdatePosts(userPostController).update(id, post)
    if not updated:
         raise HTTPException(404, detail=f"post id: {id} not found")
    return {"updated": updated}

#user section
@app.get("/user/{id}",response_model=um.UserResponse, status_code=status.HTTP_202_ACCEPTED)
def get_user(id: int):
    logger.info(f"retriving user id {id}")
    user = UserCrud(user_handler).get_user(id)
    if not user:
        raise HTTPException(404, detail=f"user id: {id} not found")
    return user


@app.post("/createuser",status_code=status.HTTP_201_CREATED, response_model=um.UserResponse)
def create_post(payload: um.UserCreate):
    logger.info(payload)
    parsedData = UserCrud(user_handler).create_user(payload)
    if not parsedData:
        raise HTTPException(404, "not able to create user")
    return parsedData