from abc import ABC, abstractmethod
from typing import List, Optional
from features.posts.data.models.PostCreateModel import PostCreateModel
from features.posts.data.models.PostModel import PostModel, PostReadModel


class DataSource(ABC):
    @abstractmethod
    def isAvailable() -> bool:
        pass

    @abstractmethod
    def get_post_votes(post: List[PostReadModel]) -> List[PostReadModel]:
        pass

    @abstractmethod
    def getPosts(
        limit: int, offset: int, search_title: Optional[str]
    ) -> Optional[list[PostReadModel]]:
        pass

    @abstractmethod
    def dumpPosts(posts: list[PostCreateModel]):
        pass

    @abstractmethod
    def getPost(id: int) -> Optional[PostReadModel]:
        pass

    @abstractmethod
    def createPost(post: PostCreateModel) -> bool:
        pass

    @abstractmethod
    def updatePost(id: int, post: dict, as_user: int) -> bool:
        pass

    @abstractmethod
    def deletePost(postId: int, as_user: int) -> Optional[PostModel]:
        pass

    @abstractmethod
    def getPostByUser(user_id: int, limit: int, offset: int) -> list[PostReadModel]:
        pass
