
import pytest
from core.utils.MyUtils import MyUtils


def test_load_properties():
    key = "localStore"
    value = MyUtils().loadProperties(key)["dbFileName"]
    assert(value == "test/post_fixtures.txt")