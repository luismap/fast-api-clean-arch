from features.posts.data.datasources.api.LocalDataSource import LocalDataSource
from features.posts.data.models.PostModel import PostModel
import json

class PostsLocalDataSource(LocalDataSource):
    def getLocalPosts() -> list[PostModel]:
        with open("test/post_fixtures.txt", "r") as f:
            jsonData = json.load(f)
            posts = [PostModel(**e) for e in jsonData["data"]]
        return posts

    def dumpLocalPosts(posts: list[PostModel]):
        with open("test/post_fixtures.txt", "w") as f:
            json.dump({"data": [e.dict() for e in posts]},f)