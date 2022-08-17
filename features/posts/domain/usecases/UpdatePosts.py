
from turtle import pos
from features.posts.data.models.PostModel import PostModel
from features.posts.domain.controllers.PostsController import PostController


class UpdatePosts:
    def __init__(self, postCtrl: PostController) -> None:
        self.postController = postCtrl

    def update(self, id: int, postModel: PostModel) -> list[int]:
        posts = self.postController.getPosts()
        toUpdate = [i for i,p in enumerate(posts) if p.id == id]
        postModel.id = id
        for i in toUpdate:
            posts[i] = postModel

        self.postController.dumpPosts(posts)
        return toUpdate

