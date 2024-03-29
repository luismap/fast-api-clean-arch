from tkinter import SE
from typing import List, Optional
import sqlalchemy.sql.functions as func
from core.db.Postgres import PostgresConn
from core.db.models.AlchemyModels import PostsAlmy, Votes
from core.failures.MyExeptions import DeletePostException, UpdatePostException
from core.utils import MyUtils
from features.posts.data.datasources.api.DataSource import DataSource
from features.posts.data.models.PostCreateModel import PostCreateModel
from features.posts.data.models.PostModel import PostModel, PostReadModel
from fastapi import Depends
from features.posts.domain.entities.Post import PostCreate, PostRead
import logging
from core.db.AlchemySql import Base, SqlAlchemyAccessLayer


# Dependency


class PostsAlchemyDS(DataSource):
    def __init__(self, postgres_conn: PostgresConn) -> None:
        self.sqlal = SqlAlchemyAccessLayer(postgres_conn.get_uri_conn())
        Base.metadata.create_all(bind=self.sqlal.engine)
        self.SessionLocal = self.sqlal.SessionLocal
        self.logger = logging.getLogger("api_dev")
        self.logger.info("Alchemy Datasource initialized")

    def isAvailable(self) -> bool:
        return True

    def get_post_votes(self, post: List[PostReadModel]) -> List[PostReadModel]:
        posts = []
        with self.SessionLocal() as session:
            for p in post:
                row = (
                    session.query(func.count(Votes.post_id))
                    .filter(Votes.post_id == p.id)
                    .scalar()
                )
                print(row)
                p.votes = row
                posts.append(p)

        return posts

    def getPosts(
        self, limit: int, offset: int, search_title: Optional[str]
    ) -> List[PostReadModel]:
        with self.SessionLocal() as session:
            posts = (
                session.query(PostsAlmy)
                .filter(PostsAlmy.title.contains(search_title))
                .limit(limit)
                .offset(offset)
                .all()
            )

        posts = self.get_post_votes(posts)
        return posts

    def getPost(self, userId: int) -> Optional[PostReadModel]:
        with self.SessionLocal() as session:
            post = session.query(PostsAlmy).filter(PostsAlmy.id == userId).first()
        return post

    def dumpPosts(posts: list[PostCreate]):
        pass

    def createPost(self, post: PostCreateModel) -> bool:
        ans = True
        with self.SessionLocal() as session:
            try:
                session.add(PostsAlmy(**post.dict()))
                session.commit()
            except Exception as e:
                self.logger.info(f"exception: {e}")
                session.rollback()
                session.flush()
                ans = False
        return ans

    def updatePost(self, id: int, post: dict, as_user: int) -> bool:
        ans = False
        post_check = lambda p: p.id == id
        user_posts = [e for e in filter(post_check, self.getPostByUser(as_user))]
        logging.info(f"user post are {user_posts}")

        if not user_posts:
            raise UpdatePostException(id)

        with self.SessionLocal() as session:
            try:
                update = (
                    session.query(PostsAlmy)
                    .filter(PostsAlmy.id == id, PostsAlmy.user_id == as_user)
                    .update(post, synchronize_session="fetch")
                )
                self.logger.info(f"updating for {update}")
                session.commit()
                if update:
                    ans = True
            except Exception as e:
                self.logger.info(e)
        return ans

    def deletePost(self, postId: int, as_user: int) -> Optional[PostModel]:
        with self.SessionLocal() as session:
            postDel = self.getPost(postId)
            if postDel:  # if not None
                if postDel.user_id == as_user:
                    self.logger.info(f"deleting {postDel}")
                    session.delete(postDel)
                    session.commit()
                else:
                    raise DeletePostException(postId)
        return postDel

    def getPostByUser(
        self, user_id: int, limit: int, offset: int, search_titel: Optional[str]
    ) -> List[PostReadModel]:
        with self.SessionLocal() as session:
            posts = (
                session.query(PostsAlmy)
                .filter(
                    PostsAlmy.user_id == user_id, PostsAlmy.title.contains(search_titel)
                )
                .limit(limit)
                .offset(offset)
                .all()
            )
        return posts


"""



    def get_users(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.User).offset(skip).limit(limit).all()


    def create_user(db: Session, user: schemas.UserCreate):
        fake_hashed_password = user.password + "notreallyhashed"
        db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


    def get_items(db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Item).offset(skip).limit(limit).all()


    def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
        db_item = models.Item(**item.dict(), owner_id=user_id)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
"""
