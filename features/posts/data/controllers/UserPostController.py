from asyncio.log import logger
import logging
from features.posts.data.datasources.PostsAlchemyDS import PostsAlchemyDS
from features.posts.data.datasources.PostsLocalDS import PostsLocalDataSource
from features.posts.data.datasources.PostsPostgresDS import PostsPostgresDS
from features.posts.data.models.PostModel import PostModel
from features.posts.domain.controllers.PostsController import PostController
from core.utils.MyUtils import MyUtils

class UserPostController(PostController):

    def __init__(self, 
    localDS: PostsLocalDataSource,
    postgresDS: PostsPostgresDS,
    alchemyDS: PostsAlchemyDS

    ) -> None:
        self.localDS = localDS
        self.postgresDS = postgresDS
        self.alchemyDS = alchemyDS
        self.appProps = MyUtils.loadProperties("general")["app"]
        self.appState = self.appProps["env"]
        self.logger = logging.getLogger(self.appProps["logger"])
        if alchemyDS.isAvailable():
            self.logger.info("using alchemy DS")
            self.activeDS = alchemyDS
        elif postgresDS.isAvailable():
            self.logger.info("using postgres DS")
            self.activeDS = postgresDS 
        elif localDS.isAvailable():
            self.logger.info("using localDb")
            self.activeDS = localDS
        self.logger.info("userPostController initialized")

    def getPosts(self) -> list[PostModel]:
        posts = self.activeDS.getPosts()
        return posts

    def dumpPosts(self,posts: list[PostModel]):
        self.activeDS.dumpPosts(posts)

    def getPost(self,id: int) -> PostModel:
        post = self.activeDS.getPost(id)
        return post

    def createPost(self,post: PostModel) -> bool:
        return self.activeDS.createPost(post)

    def updatePost(self,id: int, post: dict) -> bool:
        return self.activeDS.updatePost(id, post)

    def deletePost(self, postId: int ) -> PostModel:
        return self.activeDS.deletePost(postId)
