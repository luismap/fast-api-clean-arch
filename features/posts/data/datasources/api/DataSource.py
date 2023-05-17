
from abc import ABC, abstractmethod
from typing import Optional
from features.posts.data.models.PostCreateModel import PostCreateModel
from features.posts.data.models.PostModel import PostModel
from features.posts.domain.entities.Post import PostCreate, PostRead

class DataSource(ABC):

    @abstractmethod
    def isAvailable(self) -> bool:
        pass

    @abstractmethod
    def getPosts(self) -> Optional[list[PostRead]]:
        pass

    @abstractmethod
    def dumpPosts(self,posts: list[PostCreateModel]):
        pass
    
    @abstractmethod
    def getPost(self,id: int) -> Optional[PostRead]:
        pass

    @abstractmethod
    def createPost(self,post: PostCreateModel) -> bool:
        pass

    @abstractmethod
    def updatePost(self,id: int, post: dict) -> bool:
        pass

    @abstractmethod
    def deletePost(self,postId: int ) -> Optional[PostModel]:
        pass