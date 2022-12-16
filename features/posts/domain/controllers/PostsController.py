from abc import ABC, abstractclassmethod
from typing import Optional
from features.posts.data.models.PostCreateModel import PostCreateModel
from features.posts.data.models.PostModel import PostModel
from features.posts.domain.entities.Post import Post, PostCreate


class PostController(ABC):
    @abstractclassmethod
    def getPosts() -> Optional[list[PostModel]]:
        pass

    @abstractclassmethod
    def dumpPosts(posts: list[PostCreate]):
        pass

    @abstractclassmethod
    def getPost(id: int) -> PostModel:
        pass

    @abstractclassmethod
    def createPost(post: PostCreateModel) -> bool:
        pass

    @abstractclassmethod
    def updatePost(id: int, post: dict) -> bool:
        pass

    @abstractclassmethod
    def deletePost(postId: int ) -> PostModel:
        pass
