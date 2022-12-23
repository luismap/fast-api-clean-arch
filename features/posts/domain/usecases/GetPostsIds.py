
from typing import Optional
from features.posts.data.models.PostModel import PostModel
from features.posts.domain.controllers.PostsController import PostController


class GetPostsIds:
    def __init__(self, postCtrl: PostController) -> None:
        self.postCtrl = postCtrl

    def getPostsIds(self) -> Optional[list[int]]:
        data = self.postCtrl.getPosts()
        if data:
            return [e.id for e in data]
        else:
            return None