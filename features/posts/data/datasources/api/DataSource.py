
from abc import ABC, abstractmethod
from typing import Optional
from features.posts.data.models.PostCreateModel import PostCreateModel
from features.posts.data.models.PostModel import PostModel
from features.posts.domain.entities.Post import PostCreate, PostRead

class DataSource(ABC):

    @classmethod
    def isAvailable(self) -> bool:
        pass

    @classmethod
    def getPosts(self) -> Optional[list[PostRead]]:
        pass

    @classmethod
    def dumpPosts(self,posts: list[PostCreateModel]):
        pass
    
    @classmethod
    def getPost(self,id: int) -> Optional[PostRead]:
        pass

    @classmethod
    def createPost(self,post: PostCreateModel) -> bool:
        pass

    @classmethod
    def updatePost(self,id: int, post: dict) -> bool:
        pass

    @classmethod
    def deletePost(self,postId: int, as_user: int ) -> Optional[PostModel]:
        pass

    @classmethod
    def getPostByUser(user_id: int) -> list[PostRead]:
        pass