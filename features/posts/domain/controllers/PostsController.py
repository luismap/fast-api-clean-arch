from abc import ABC, abstractclassmethod

from features.posts.data.models.PostModel import PostModel


class PostController(ABC):
    @abstractclassmethod
    def getPosts() -> list[PostModel]:
        pass

    @abstractclassmethod
    def dumpPosts(posts: list[PostModel]):
        pass