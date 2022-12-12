from abc import ABC, abstractclassmethod
from features.posts.data.models.PostModel import PostModel
from features.posts.domain.entities.Post import Post, PostCreate


class PostController(ABC):
    @abstractclassmethod
    def getPosts() -> list[PostModel]:
        pass

    @abstractclassmethod
    def dumpPosts(posts: list[PostModel]):
        pass

    @abstractclassmethod
    def getPost(id: int) -> PostModel:
        pass

    @abstractclassmethod
    def createPost(post: PostCreate) -> bool:
        pass

    @abstractclassmethod
    def updatePost(id: int, post: dict) -> bool:
        pass

    @abstractclassmethod
    def deletePost(postId: int ) -> PostModel:
        pass
