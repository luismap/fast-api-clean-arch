from asyncio.log import logger
import logging
from features.posts.data.datasources.PostsLocalDS import PostsLocalDataSource
from features.posts.data.datasources.PostsPostgresDS import PostsPostgresDS
from features.posts.data.models.PostModel import PostModel
from features.posts.domain.controllers.PostsController import PostController
from core.utils.MyUtils import MyUtils

class UserPostController(PostController):

    def __init__(self) -> None:
        self.localDS = PostsLocalDataSource()
        self.postgresDS = PostsPostgresDS()
        self.appProps = MyUtils.loadProperties("general")["app"]
        self.appState = self.appProps["env"]
        self.logger = logging.getLogger(self.appProps["logger"])
        if self.postgresDS.isAvailable():
            self.logger.info("using postgres DS")
            self.activeDS = self.postgresDS 
        elif self.localDS.isAvailable():
            self.logger.info("using localDb")
            self.activeDS = self.localDS
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

    def updatePost(self,id: int, post: PostModel) -> bool:
        try:
            return self.activeDS.updatePost(id, post)
        except Exception as ex:
            self.logger.info(f"error updating post {id}: {ex}")

         

    def deletePost(self, postId: int ) -> PostModel:
        return self.activeDS.deletePost(postId)
