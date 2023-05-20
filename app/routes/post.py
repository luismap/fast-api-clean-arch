from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException
import yaml
from app.auth.oauth2 import get_current_user
from core.db.Postgres import PostgresConn
from core.utils.MyUtils import MyUtils
from features.posts.data.controllers.UserPostController import UserPostController
import logging
from features.posts.data.datasources.PostsAlchemyDS import PostsAlchemyDS
from features.posts.data.datasources.PostsLocalDS import PostsLocalDataSource
from features.posts.data.datasources.PostsPostgresDS import PostsPostgresDS
from features.posts.data.models.PostCreateModel import PostCreateModel
from features.posts.data.models.PostResponseModel import PostResponseModel
from features.posts.domain.entities.Post import PostRead
from features.posts.domain.usecases.PostCrud import PostCrud
from features.user.data.models.TokenModel import TokenData

canlog = True
appProps = MyUtils.loadProperties("general")["app"]
logger = logging.getLogger(appProps["logger"])

# Initialize the logger once as the application starts up
# because dependencies, configure logger in first route called in app.main
with open("logging.yaml", 'rt') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

# Get an instance of the logger and use it to write a log!
# Note: Do this AFTER the config is loaded above or it won't use the config.
logger = logging.getLogger(appProps["logger"])
logger.info("Initial log config in route post!")



#db conn
postgreConn = PostgresConn()

# user postController
alchemyDS = PostsAlchemyDS(postgreConn)
localDS = PostsLocalDataSource()
postgresDS = PostsPostgresDS()
userPostController = UserPostController(localDS, postgresDS, alchemyDS)
router = APIRouter(
    prefix="/posts",
    tags=['posts']
)

@router.get("/", response_model=List[PostResponseModel])
def get_posts():
    parsedData = PostCrud(userPostController).getPosts()
    logger.info(parsedData)
    return parsedData

@router.post("/create",status_code=201)
def create_post(payload: PostCreateModel, token_data : Annotated[TokenData, Depends(get_current_user)]):
    logger.info(f"creating post as user {token_data}")
    payload.user_id = token_data.user_id
    logger.info(f"creating following payload {payload}")


    parsedData = PostCrud(userPostController).createPosts(payload)
    if not parsedData:
        raise HTTPException(404, "not able to create post")
    return {"added": parsedData}

@router.get("/ids")
def get_post():
    ids = PostCrud(userPostController).getPostsIds()
    logger.info(ids)
    return {"postsIds": ids}

@router.get("/{id}", response_model=PostResponseModel)
def get_post_id(id: int):
    logger.info(f"retriving id {id}")
    post = PostCrud(userPostController).getPostById(id)
    if not post: 
        raise HTTPException(404, detail=f"post id: {id} not found")
    return post

@router.delete("/{id}")
def delete_post(id: int, token_data: Annotated[TokenData, Depends(get_current_user)]):
    logger.info(f"deleting post with id: {id} by user: {token_data.user_id}")
    deleted = PostCrud(userPostController).deletePost(id, token_data.user_id)
    if not deleted:
        raise HTTPException(404, detail=f"fail to delete id {id}")
    return {"deleted": deleted}

@router.put("/{id}")
def update_post(id: int, post: dict):
    logger.info(f"updating for id {id} with data {post} type {type(post)}")
    if not id: 
        raise HTTPException(404, detail=f"post id: {id} not passed")
    updated = PostCrud(userPostController).update(id, post)
    if not updated:
         raise HTTPException(404, detail=f"post id: {id} not found")
    return {"updated": updated}

@router.get("/my")
def get_my_posts(token_data: Annotated[TokenData, Depends(get_current_user)]) -> List[PostRead]:
    pass
