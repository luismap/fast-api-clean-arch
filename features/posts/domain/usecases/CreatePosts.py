from features.posts.data.models.PostCreateModel import PostCreateModel
from features.posts.data.models.PostModel import PostModel
from features.posts.domain.controllers.PostsController import PostController
from features.posts.domain.entities.Post import PostCreate

class CreatePosts:
    def __init__(self, postCtrl: PostController) -> None:
        self.postController = postCtrl

    def createPosts(self,payload: PostCreateModel) -> bool: 
        return self.postController.createPost(payload)