
from abc import ABC, abstractmethod
from typing import Optional
from features.posts.data.models.PostModel import PostModel

class DataSource(ABC):

    @abstractmethod
    def isAvailable(self) -> bool:
        pass

    @abstractmethod
    def getPosts(self) -> Optional[list[PostModel]]:
        pass

    @abstractmethod
    def dumpPosts(self,posts: list[PostModel]):
        pass
    
    @abstractmethod
    def getPost(self,id: int) -> Optional[PostModel]:
        pass

    @abstractmethod
    def createPost(self,post: PostModel) -> bool:
        pass

    @abstractmethod
    def updatePost(self,id: int, post: dict) -> bool:
        pass

    @abstractmethod
    def deletePost(self,postId: int ) -> Optional[PostModel]:
        pass