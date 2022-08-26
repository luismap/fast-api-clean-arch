from abc import ABC, abstractclassmethod
from features.posts.data.models.PostModel import PostModel


class PostController(ABC):
    @abstractclassmethod
    def getPosts() -> list[PostModel]:
        pass

    @abstractclassmethod
    def dumpPosts(posts: list[PostModel]):
        pass

    @abstractclassmethod
    def getPost() -> PostModel:
        pass

    @abstractclassmethod
    def createPost(post: PostModel) -> bool:
        pass

    @abstractclassmethod
    def updatePost(post: PostModel) -> bool:
        pass

    @abstractclassmethod
    def deletePost(postId: int ) -> bool:
        pass
