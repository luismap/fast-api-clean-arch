

import logging
from core.utils.MyUtils import MyUtils
from features.posts.data.datasources.api.DataSource import DataSource
from features.posts.data.models.PostModel import PostModel
from core.db.Postgres import PostgresConn
import psycopg
from psycopg.rows import dict_row
from core.failures.MyExeptions import IdNotFound
import yaml

from features.posts.domain.entities.Post import PostCreate

class PostsPostgresDS(DataSource):

    def __init__(self) -> None:
        self.logger = logging.getLogger("api_dev")
        self.logger.info("postPostgresDS initialized")
        self.postgresConn = PostgresConn()
        properties = MyUtils.loadProperties("postgres")["posts"]
        self.db = properties["db"]
        self.table = properties["table"]
        self.connParams = self.postgresConn.get_conn_params()

    def isAvailable(self) -> bool:
        try:
            with psycopg.connect(**self.connParams) as conn:
                self.logger.info("connection to postgres successful")
            return True
        except:
            self.logger.info("connect postgres unsuccessful")
            return False

    def getPosts(self) -> list[PostModel]:
        with psycopg.connect(**self.connParams, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                cur.execute(f"select * from {self.db}.{self.table}")
                data = cur.fetchall()
                return [PostModel(**e) for e in data]
    
    def dumpPosts(posts: list[PostCreate]):
        pass

    def getPost(self, id: int) -> PostModel:
        with psycopg.connect(**self.connParams, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                cur.execute(f"""
                select
                *
                 from {self.db}.{self.table}
                where id = {id}::bigint
                """)
                row = cur.fetchone()
                if row == None:
                    return None
                self.logger.info(f"returned row{row}")
                return PostModel(**row)

    def createPost(self, post: PostCreate) -> bool:
        #tbe with correct boolean logic
        with psycopg.connect(**self.connParams, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                cur.execute(f"""
                INSERT INTO {self.db}.{self.table} (title, content, published, rating)
                values(%s,%s,%s,%s)
                """,(post.title, post.content, post.published, post.rating))

        return True

        

    def updatePost(self,id: int, post: dict) -> bool:
        lookedPost = self.getPost(id)
        if lookedPost == None:
            return False

        lookedPost.update(post)

        with psycopg.connect(**self.connParams, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                cur.execute(f"""
                UPDATE {self.db}.{self.table}
                SET title= %s, content = %s, published= %s, rating = %s
                WHERE id = {id}
                """,(lookedPost.title, lookedPost.content, lookedPost.published, lookedPost.rating))

        return True

    def deletePost(self, postId: int ) -> bool:
        with psycopg.connect(**self.connParams, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                post = self.getPost(postId) #check post exists
                if post:
                    cur.execute(f"""
                        DELETE FROM {self.db}.{self.table}
                        WHERE id = %s
                        """,(postId,))
                else:
                    return False
                self.logger.info(f"[deleting] post {post}")
        uPost = self.getPost(postId) #check post deleted
        if uPost == None:
            return True
        return False