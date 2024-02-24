import logging
from typing import List, Optional
from core.utils.MyUtils import MyUtils
from features.posts.data.models.PostCreateModel import PostCreateModel
from features.posts.data.models.PostModel import PostModel
from features.posts.domain.controllers.PostsController import PostController
from features.posts.domain.entities.Post import PostRead


class PostCrud:
    def __init__(self, postCtrl: PostController) -> None:
        self.postController = postCtrl
        appProps = MyUtils.loadProperties(key="general")["app"]
        self.appProps = MyUtils.loadProperties("general")["app"]
        self.logger = logging.getLogger(appProps["logger"])

    def createPosts(self, payload: PostCreateModel) -> bool:
        return self.postController.createPost(payload)

    def deletePost(self, id: int, as_user: int) -> Optional[PostRead]:
        return self.postController.deletePost(id, as_user)

    def getPosts(
        self, limit: int, offset: int, search_title: Optional[str]
    ) -> Optional[List[PostModel]]:
        return self.postController.getPosts(limit, offset, search_title)

    def getPostById(self, id: int) -> PostRead:
        data = self.postController.getPost(id)
        self.logger.info(f"for id {id} got content {data} ")
        return data

    def getPostsIds(self) -> Optional[list[int]]:
        data = self.postController.getPosts(limit=10, offset=0, search_title="")
        if data:
            return [e.id for e in data]
        else:
            return None

    def update(self, id: int, post: dict, as_user: int) -> bool:
        ans = self.postController.updatePost(id, post, as_user)
        return ans

    def get_post_by_user(
        self, as_user: int, limit: int, offset: int, search_titel: Optional[str]
    ) -> List[PostRead]:
        return self.postController.get_post_by_user(
            as_user, limit, offset, search_titel
        )
