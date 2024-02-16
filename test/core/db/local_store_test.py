import json
from pytest import mark
import pytest

from core.db.LocalStore import LocalStore
from core.utils.MyUtils import MyUtils
from features.posts.data.models.PostModel import PostModel


@pytest.fixture
def local_store():
    return LocalStore()


@pytest.fixture
def local_data():
    with open("test/local_db_test_data.json", "r") as ldb:
        data = json.load(ldb)["data"]
    return data


class TestLocalStore:
    def test_is_available_return_true(self, local_store):
        fileName = MyUtils.loadProperties("localStore")["dbFileName"]
        assert True == local_store.isAvailable(fileName)

    def test_is_available_return_false(self, local_store):
        fileName = "not_existing_file"
        assert False == local_store.isAvailable(fileName)

    def test_get_local_data_returns_data(self, local_store, local_data):
        load_data = local_store.getLocalData("test/local_db_test_data.json")
        assert local_data == load_data

    def test_get_local_data_returns_none(self, local_store, local_data):
        load_data = local_store.getLocalData("test/non_existing_data.json")
        assert None == load_data

    def test_dump_local_data(self, local_store, local_data):
        ans = local_store.dumpLocalData("test/dump_local.json", local_data)
        assert True == ans
