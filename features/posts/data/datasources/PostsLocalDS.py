import logging
from typing import List, Optional
from core.db.LocalStore import LocalStore
from core.failures.MyExeptions import CreatePostError
from core.utils.MyUtils import MyUtils
from features.posts.data.datasources.api.DataSource import DataSource
from features.posts.data.models.PostCreateModel import PostCreateModel
from features.posts.data.models.PostModel import PostModel, PostReadModel


class PostsLocalDataSource(DataSource):
    def __init__(self) -> None:
        self.appProps = MyUtils.loadProperties("general")["app"]
        self.logger = logging.getLogger(self.appProps["logger"])
        self.localDb = MyUtils.loadProperties("localStore")
        self.logger.info("local datasource instanciated")
        self.postFile = self.localDb["dbFileName"]
        self.logger.info(f"{self.postFile}")
        self.localStore = LocalStore()

    def get_post_votes(post: List[PostReadModel]):
        pass

    def isAvailable(self) -> bool:
        isA = self.localStore.isAvailable(self.postFile)
        self.logger.info(f"is local Db available {isA}")
        return isA

    def getPosts(self) -> Optional[list[PostModel]]:
        postData = self.localStore.getLocalData(self.postFile)
        self.logger.info(f"got data {postData}")
        if postData:
            posts = [PostModel(**e) for e in postData]
            return posts
        else:
            return None

    def dumpPosts(self, posts: list[PostCreateModel]):
        data = [e.dict() for e in posts]
        f = lambda e: e.update({"created_at": str(e["created_at"])})
        list(map((f), data))
        self.logger.info(f"data to dump {data}")
        self.localStore.dumpLocalData(self.postFile, data)

    def getPost(self, id: int) -> Optional[PostModel]:
        """given an id, get post from local datasource
        Args:
            id (int): id

        Returns:
            PostModel: a post model
        """
        localPosts = self.getPosts()
        if localPosts:
            post = list(filter(lambda p: p.id == id, localPosts))
            return post[0] if post else None
        else:
            return None

    def createPost(self, payload: PostCreateModel) -> bool:
        try:
            posts = []
            tmp_posts = self.getPosts()
            if tmp_posts:
                posts = [PostCreateModel(**e.dict()) for e in tmp_posts]
                ids = map(lambda e: e if e else 0, [e.id for e in posts])
                newId = max(ids) + 1
            else:
                newId = 1
                posts = []
            payload.id = newId
            posts.append(payload)
            self.dumpPosts(posts)
            return True
        except:
            raise CreatePostError("error creating post")

    def updatePost(self, id: int, post: dict) -> bool:
        posts = self.getPosts()
        toUpdate = [i for i, p in enumerate(posts) if p.id == id]

        for i in toUpdate:
            posts[i].update(post)

        self.dumpPosts(posts)
        return True if len(toUpdate) > 0 else False

    def deletePost(self, postId: int) -> Optional[PostModel]:
        posts = self.getPosts()
        postIdx = [i for i, p in enumerate(posts) if p.id == postId]
        if len(postIdx) > 1:
            raise Exception(f"non unique post")
        if len(postIdx) == 1:
            deletedPost = posts.pop(postIdx[0])
            self.dumpPosts(posts)
        else:
            deletedPost = None

        return deletedPost

    def getPostByUser(user_id: int, limit: int, offset: int) -> List[PostReadModel]:
        pass
