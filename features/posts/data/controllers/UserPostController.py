from typing_extensions import Self
from features.posts.data.datasources.PostsLocalDataSource import PostsLocalDataSource
from features.posts.data.datasources.api.LocalDataSource import LocalDataSource
from features.posts.data.models.PostModel import PostModel

from features.posts.domain.controllers.PostsController import PostController

class UserPostController(PostController):
    def __init__(self) -> None:
        self.localDatasource = PostsLocalDataSource
    def getPosts(self) -> list[PostModel]:
       return self.localDatasource.getLocalPosts()

    def dumpPosts(self,posts: list[PostModel]):
        self.localDatasource.dumpLocalPosts(posts)