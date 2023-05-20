
import logging
from typing import List, Optional
from core.utils import MyUtils
from features.posts.data.models.PostCreateModel import PostCreateModel
from features.posts.data.models.PostModel import PostModel
from features.posts.domain.controllers.PostsController import PostController
from features.posts.domain.entities.Post import PostRead


class PostCrud:

    def __init__(self, postCtrl: PostController) -> None:
        self.postController = postCtrl
        appProps = MyUtils.loadProperties(key="general")["app"]
        self.postController = postCtrl
        self.appProps = MyUtils.loadProperties("general")["app"]
        self.logger = logging.getLogger(appProps["logger"])

    def createPosts(self,payload: PostCreateModel) -> bool: 
        return self.postController.createPost(payload)

    def deletePost(self, id: int, as_user: int) -> Optional[PostRead]:
        return self.postController.deletePost(id, as_user)

    def getPosts(self) -> Optional[List[PostModel]]:
        return self.postController.getPosts()
    
    def getPostById(self,id: int) -> PostRead:
        data = self.postController.getPost(id)
        self.logger.info(f"for id {id} got content {data} ")
        return data
    
    def getPostsIds(self) -> Optional[list[int]]:
        data = self.postCtrl.getPosts()
        if data:
            return [e.id for e in data]
        else:
            return None
        
    def update(self, id: int, post: dict) -> bool:
        ans = self.postController.updatePost(id, post)
        return ans