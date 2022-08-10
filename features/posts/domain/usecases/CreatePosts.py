
import py_compile
from features.posts.data.models.PostModel import PostModel

from features.posts.domain.controllers.PostsController import PostController
import json

class CreatePosts:
    def __init__(self, postCtrl: PostController) -> None:
        self.postController = postCtrl

    def createPosts(self,payload: PostModel) -> PostModel:
        parsedData = self.postController.getPosts()
        newId = max([e.id for e in parsedData]) + 1
        payload.id = newId
        parsedData.append(payload)
        self.postController.dumpPosts(parsedData)
        return self.postController.getPosts()[-1]