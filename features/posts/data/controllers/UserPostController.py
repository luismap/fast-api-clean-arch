import logging
from typing_extensions import Self
from features.posts.data.datasources.PostsLocalDS import PostsLocalDataSource
from features.posts.data.datasources.api.LocalDataSource import LocalDataSource
from features.posts.data.models.PostModel import PostModel

from features.posts.domain.controllers.PostsController import PostController

class UserPostController(PostController):
    def __init__(self) -> None:
        self.localDatasource = PostsLocalDataSource()
        self.logger = logging.getLogger("api_dev")
        self.logger.info("userPostControllerInitialized")

    def getPosts(self) -> list[PostModel]:
       return self.localDatasource.getLocalPosts()

    def dumpPosts(self,posts: list[PostModel]):
        self.localDatasource.dumpLocalPosts(posts)

    def getPost() -> PostModel:
        pass

    def createPost(post: PostModel) -> bool:
        pass

    def updatePost(post: PostModel) -> bool:
        pass

    def deletePost(postId: int ) -> bool:
        pass
