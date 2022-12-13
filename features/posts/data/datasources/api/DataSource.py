
from abc import ABC, abstractclassmethod
from typing import Optional
from features.posts.data.models.PostModel import PostModel

class DataSource(ABC):

    @abstractclassmethod
    def isAvailable() -> bool:
        pass

    @abstractclassmethod
    def getPosts() -> Optional[list[PostModel]]:
        pass

    @abstractclassmethod
    def dumpPosts(posts: list[PostModel]):
        pass
    
    @abstractclassmethod
    def getPost(id: int) -> Optional[PostModel]:
        pass

    @abstractclassmethod
    def createPost(post: PostModel) -> bool:
        pass

    @abstractclassmethod
    def updatePost(id: int, post: dict) -> bool:
        pass

    @abstractclassmethod
    def deletePost(postId: int ) -> PostModel:
        pass