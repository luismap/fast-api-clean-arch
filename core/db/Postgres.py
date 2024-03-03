from typing import Dict
from dotenv import load_dotenv
import os
import psycopg

"""
Get common details for postgres db
"""


class PostgresConn:
    def get_conn_params(self) -> Dict[str, str]:
        pg_uri = self.get_uri_conn()
        return psycopg.conninfo.conninfo_to_dict(pg_uri)

    def get_uri_conn(self) -> str:
        load_dotenv()
        pguser = os.getenv("pguser")
        pgpass = os.getenv("pgpass")
        pgdbname = os.getenv("pgdbname")
        pghost = os.getenv("pghost")
        return f"postgresql://{pguser}:{pgpass}@{pghost}/{pgdbname}"
