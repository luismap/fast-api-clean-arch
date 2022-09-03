import logging
from core.db.LocalStore import LocalStore
from core.failures.MyExeptions import CreatePostError
from core.utils.MyUtils import MyUtils
from features.posts.data.datasources.api.DataSource import DataSource
from features.posts.data.models.PostModel import PostModel

class PostsLocalDataSource(DataSource):
    def __init__(self) -> None:
        self.appProps = MyUtils.loadProperties("general")["app"]
        self.logger = logging.getLogger(self.appProps["logger"])
        self.localDb = MyUtils.loadProperties("localStore")
        self.logger.info("local datasource instanciated")
        self.postFile = self.localDb["dbFileName"]
        self.logger.info(f"{self.postFile}")
        self.localStore = LocalStore()
    
    def isAvailable(self) -> bool:
        isA = self.localStore.isAvailable(self.postFile)
        self.logger.info(f"is local Db available {isA}")
        return isA

    def getPosts(self) -> list[PostModel]:
        postData = self.localStore.getLocalData(self.postFile)
        posts = [PostModel(**e) for e in postData]
        return posts

    def dumpPosts(self,posts: list[PostModel]):
        data = [e.dict() for e in posts]
        self.localStore.dumpLocalData(self.postFile, data)

    def getPost(self,id: int) -> PostModel:
        """given an id, get post from local datasource
        Args:
            id (int): id

        Returns:
            PostModel: a post model
        """
        localPosts = self.getPosts()
        post = list(filter(lambda p: p.id == id, localPosts))
        return post[0] if len(post) > 0 else None

    def createPost(self,payload: PostModel) -> bool:
        try:
            posts = self.getPosts()
            newId = max([e.id for e in posts]) + 1
            payload.id = newId
            posts.append(payload)
            self.dumpPosts(posts)
            return True
        except:
            raise CreatePostError("error creating post")

    def updatePost(self,id: int, post: dict) -> bool:
        posts = self.getPosts()
        toUpdate = [i for i,p in enumerate(posts) if p.id == id]

        for i in toUpdate:
            posts[i].update(post)

        self.dumpPosts(posts)
        return True if len(toUpdate) > 0 else False

    def deletePost(self,postId: int ) -> PostModel:
        posts = self.getPosts()
        postIdx = [i for i,p in enumerate(posts) if p.id == postId]
        if len(postIdx) > 1:
            raise Exception(f"non unique post")
        if len(postIdx) == 1:
            deletedPost = posts.pop(postIdx[0])
            self.dumpPosts(posts)
        else:
            deletedPost = None
 
        return deletedPost