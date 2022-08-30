
from features.posts.data.models.PostModel import PostModel
from features.posts.domain.controllers.PostsController import PostController

class DeletePost:
    def __init__(self, postCtrl: PostController) -> None:
        self.postController = postCtrl

    def deletePost(self, id: int) -> PostModel:
        return self.postController.deletePost(id)