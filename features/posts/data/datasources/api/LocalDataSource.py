
from abc import ABC, abstractclassmethod
from features.posts.data.models.PostModel import PostModel

class LocalDataSource(ABC):
    @abstractclassmethod
    def getLocalPosts() -> list[PostModel]:
        pass

    @abstractclassmethod
    def dumpLocalPosts(posts: list[PostModel]):
        pass