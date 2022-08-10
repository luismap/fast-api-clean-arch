
from typing import List
from features.posts.data.controllers.UserPostController import UserPostController
from features.posts.data.models.PostModel import PostModel
from features.posts.domain.controllers.PostsController import PostController


class GetPosts:
    def __init__(self, postController: PostController) -> None:
        self.postController = postController

    def getPosts(self) -> List[PostModel]:
        return self.postController.getPosts()
