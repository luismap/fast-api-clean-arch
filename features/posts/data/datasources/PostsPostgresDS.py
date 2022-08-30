

import logging
from core.utils.MyUtils import MyUtils
from features.posts.data.datasources.api.DataSource import DataSource
from features.posts.data.models.PostModel import PostModel
from core.db.Postgres import PostgresConn
import psycopg
from psycopg.rows import dict_row
from core.failures.MyExeptions import IdNotFound
import yaml

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
    
    def dumpPosts(posts: list[PostModel]):
        pass

    def getPost(self, id: int) -> PostModel:
        with psycopg.connect(**self.connParams, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                cur.execute(f"""
                select * from {self.db}.{self.table}
                where id = {id}::bigint
                """)
                row = cur.fetchone()
                if row == None:
                    raise IdNotFound(id)
                return PostModel(**row)

    def createPost(post: PostModel) -> bool:
        pass

    def updatePost(post: PostModel) -> bool:
        pass

    def deletePost(postId: int ) -> bool:
        pass