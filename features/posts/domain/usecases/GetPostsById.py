
import imp
import logging
from core.utils.MyUtils import MyUtils
from features.posts.data.models.PostModel import PostModel
from features.posts.domain.controllers.PostsController import PostController

class GetPostsById:
    def __init__(self, postCtrl: PostController) -> None:
        appProps = MyUtils().loadProperties(key="general")["app"]
        self.postController = postCtrl
        self.appProps = MyUtils().loadProperties("general")["app"]
        self.logger = logging.getLogger(appProps["logger"])
    
    def getPostById(self,id: int) -> PostModel:
        data = self.postController.getPost(id)
        self.logger.info(f"for id {id} got content {data} ")
        return data