
from features.posts.data.models.PostModel import PostModel
from features.posts.domain.controllers.PostsController import PostController


class GetPostsIds:
    def __init__(self, postCtrl: PostController) -> None:
        self.postCtrl = postCtrl

    def getPostsIds(self) -> list[int]:
        data: list[PostModel] = self.postCtrl.getPosts()
        return [e.id for e in data]