import logging
from typing import List, Optional
from features.posts.data.datasources.PostsAlchemyDS import PostsAlchemyDS
from features.posts.data.datasources.PostsLocalDS import PostsLocalDataSource
from features.posts.data.datasources.PostsPostgresDS import PostsPostgresDS
from features.posts.data.models.PostCreateModel import PostCreateModel
from features.posts.data.models.PostModel import PostModel
from features.posts.domain.controllers.PostsController import PostController
from core.utils.MyUtils import MyUtils
from features.posts.domain.entities.Post import PostCreate, PostRead

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
            self.logger.info("using POST alchemy DS")
            self.activeDS = alchemyDS
        elif postgresDS.isAvailable():
            self.logger.info("using POSTGRES DS")
            self.activeDS = postgresDS 
        elif localDS.isAvailable():
            self.logger.info("using LOCALDB")
            self.activeDS = localDS
        self.logger.info("userPostController initialized")

    def getPosts(self) -> Optional[list[PostRead]]:
        posts = self.activeDS.getPosts()
        return posts

    def dumpPosts(self,posts: list[PostCreate]):
        self.activeDS.dumpPosts(posts)

    def getPost(self,id: int) -> PostRead:
        post = self.activeDS.getPost(id)
        return post

    def createPost(self,post: PostCreateModel) -> bool:
        return self.activeDS.createPost(post)
   
    def updatePost(self,id: int, post: dict) -> bool:
        return self.activeDS.updatePost(id, post)

    def deletePost(self,postId: int, as_user: int ) -> Optional[PostModel]:
        return self.activeDS.deletePost(postId, as_user)
    
    def get_post_by_user(self, as_user: int) -> List[PostRead]:
        return self.activeDS.getPostByUser(as_user)

