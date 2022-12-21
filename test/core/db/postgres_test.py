
from typing import Mapping
import pytest
import os

from core.db.Postgres import PostgresConn

@pytest.fixture
def create_env()-> str:
    os.environ["pguser"]="user"
    os.environ["pgpass"]="pass"
    os.environ["pgdbname"]="dbname"
    os.environ["pghost"]="host"
    conn_str = "postgresql://user:pass@host/dbname"
    return conn_str

@pytest.fixture
def create_dict() -> Mapping[str,str]:
    m = {"user":"user","password":"pass", "dbname":"dbname", "host":"host"}
    return m

class TestPostgres:

    def test_get_uri_conn(self, create_env):
        postgres_conn = PostgresConn()
        assert(create_env == postgres_conn.get_uri_conn())

    def test_get_conn_params(self, create_dict):
        postgres_conn = PostgresConn()
        assert(create_dict == postgres_conn.get_conn_params())
        
        

    