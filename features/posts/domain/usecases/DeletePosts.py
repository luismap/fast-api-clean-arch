
from features.posts.data.models.PostModel import PostModel
from features.posts.domain.controllers.PostsController import PostController

class DeletePost:
    def __init__(self, postCtrl: PostController) -> None:
        self.postController = postCtrl

    def deletePost(self, id: int):
        posts = self.postController.getPosts()
        postIdx = [i for i,p in enumerate(posts) if p.id == id]
        deletedPost = [posts.pop(i) for i in postIdx]
        self.postController.dumpPosts(posts)
        return deletedPost
