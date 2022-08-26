
import imp
from features.posts.data.datasources.PostsLocalDS import PostsLocalDataSource
from features.posts.data.models.PostModel import PostModel
from features.posts.domain.controllers.PostsController import PostController

class GetPostsById:
    def __init__(self, postCtrl: PostController) -> None:
       self.postController = postCtrl
    
    def getPostById(self,id: int) -> PostModel:
        data = self.postController.getPosts()
        post = filter(lambda p: p.id == id, data)
        return post