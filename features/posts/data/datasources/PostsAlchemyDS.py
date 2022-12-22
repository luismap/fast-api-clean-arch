
from tkinter import SE
from typing import Optional
from sqlalchemy.orm import Session
from core.db.Postgres import PostgresConn
from core.db.models.AlchemyModels import PostsAlmy
from core.utils import MyUtils
from features.posts.data.datasources.api.DataSource import DataSource
from features.posts.data.models.PostCreateModel import PostCreateModel
from features.posts.data.models.PostModel import PostModel
from fastapi import Depends
from features.posts.domain.entities.Post import PostCreate
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

    def getPosts(self) -> list[PostModel]:
        with self.SessionLocal() as session:
            posts = session.query(PostsAlmy).all()
        return posts

    def getPost(self,userId: int) -> Optional[PostModel]:
        with self.SessionLocal() as session:
            post = session.query(PostsAlmy).filter(PostsAlmy.id == userId).first()
        return post

    def dumpPosts(posts: list[PostCreate]):
        pass

    def createPost(self,post: PostCreateModel) -> bool:
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

    def updatePost(self, id: int, post: dict) -> bool:
        ans = False
        with self.SessionLocal() as session:
            try:
                update = session\
                    .query(PostsAlmy)\
                    .filter(PostsAlmy.id == id)\
                    .update(post,synchronize_session="fetch") 
                self.logger.info(f"updating for {update}")
                session.commit()
                if update:
                    ans = True
            except Exception as e:
                self.logger.info(e)
        return ans

    def deletePost(self, postId: int ) -> Optional[PostModel]:
        with self.SessionLocal() as session:
            postDel = self.getPost(postId)
            self.logger.info(f"deleting {postDel}")
            if postDel:#if not None
                session.delete(postDel)
                session.commit()
        return postDel
            

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