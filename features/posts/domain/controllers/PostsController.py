from abc import ABC, abstractmethod
from typing import Optional
from features.posts.data.models.PostCreateModel import PostCreateModel
from features.posts.data.models.PostModel import PostModel
from features.posts.domain.entities.Post import PostCreate, PostRead


class PostController(ABC):
    @abstractmethod
    def getPosts(self) -> Optional[list[PostModel]]:
        pass

    @abstractmethod
    def dumpPosts(self,posts: list[PostCreate]):
        pass

    @abstractmethod
    def getPost(self,id: int) -> PostRead:
        pass

    @abstractmethod
    def createPost(self,post: PostCreateModel) -> bool:
        pass

    @abstractmethod
    def updatePost(self,id: int, post: dict) -> bool:
        pass

    @abstractmethod
    def deletePost(self,postId: int, as_user: int ) -> Optional[PostModel]:
        pass
