from abc import ABC, abstractmethod
from typing import List, Optional
from features.posts.data.models.PostCreateModel import PostCreateModel
from features.posts.data.models.PostModel import PostModel
from features.posts.domain.entities.Post import PostCreate, PostRead


class PostController(ABC):
    @abstractmethod
    def getPosts(
        limit: int, offset: int, search_title: Optional[str]
    ) -> Optional[List[PostModel]]:
        pass

    @abstractmethod
    def dumpPosts(posts: List[PostCreate]):
        pass

    @abstractmethod
    def getPost(id: int) -> PostRead:
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

    @classmethod
    def get_post_by_user(
        as_user: int, limit: int, offset: int, search_title: Optional[str]
    ) -> List[PostRead]:
        pass
