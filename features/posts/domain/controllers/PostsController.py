from abc import ABC, abstractmethod
from typing import List, Optional
from features.posts.data.models.PostCreateModel import PostCreateModel
from features.posts.data.models.PostModel import PostModel
from features.posts.domain.entities.Post import PostCreate, PostRead


class PostController(ABC):
    @abstractmethod
    def getPosts(self,
                limit: int,
                offset: int,
                search_title: Optional[str]) -> Optional[List[PostModel]]:
        pass

    @abstractmethod
    def dumpPosts(self,posts: List[PostCreate]):
        pass

    @abstractmethod
    def getPost(self,id: int) -> PostRead:
        pass

    @abstractmethod
    def createPost(self,post: PostCreateModel) -> bool:
        pass

    @abstractmethod
    def updatePost(self,id: int, post: dict, as_user: int) -> bool:
        pass

    @abstractmethod
    def deletePost(self,postId: int, as_user: int ) -> Optional[PostModel]:
        pass

    @classmethod
    def get_post_by_user(
        as_user: int,
        limit: int,
        offset: int,
        search_title: Optional[str]    ) -> List[PostRead]:
        pass
