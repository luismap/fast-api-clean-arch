
from turtle import pos
from features.posts.data.models.PostModel import PostModel
from features.posts.domain.controllers.PostsController import PostController


class UpdatePosts:
    def __init__(self, postCtrl: PostController) -> None:
        self.postController = postCtrl

    def update(self, id: int, post: dict) -> list[int]:
        ans = self.postController.updatePost(id, post)
        return {"updated": ans }

