import json
import pytest

from core.db.AlchemySql import Base, SqlAlchemyAccessLayer
from core.db.models.AlchemyModels import PostsAlmy
from core.utils import MyUtils
from features.posts.data.models.PostCreateModel import PostCreateModel
from features.posts.data.models.PostModel import PostModel

sqlal = SqlAlchemyAccessLayer("sqlite:///")
sqlal.engine.connect()

with open("test/local_db_test_data.json", "r") as f:
    local_data = json.load(f)["data"]


@pytest.fixture
def setup():
    with sqlal.engine.connect() as conn:
        # https://www.sqlite.org/inmemorydb.html
        # by passing empty string, we create ephemeral db
        conn.execute("attach '' as fast_api")

    Base.metadata.create_all(bind=sqlal.engine)
    return sqlal.SessionLocal()


@pytest.fixture
def teardown(setup):
    setup.remove()


def test_model_is_save(setup):
    session = setup
    row = PostsAlmy(**PostCreateModel(**local_data[0]).dict())
    session.add(row)
    session.commit()
    data = session.query(PostsAlmy).first()
    # row.content = "new content"
    content1 = PostModel.from_orm(row)
    content2 = PostModel.from_orm(data)
    assert content1.dict() == content2.dict()
