import sqlite3
from typing import Iterable, Any


class DatabaseManager:
    """Handles SQLite database connections and queries."""

    def __init__(self, db_path: str):
        self._db_path = db_path
        self._connection = None

    def connect(self):
        if self._connection is None:
            self._connection = sqlite3.connect(self._db_path)

    def close(self):
        if self._connection:
            self._connection.close()
            self._connection = None

    def fetch_all(self, sql: str, params: Iterable[Any] = ()):
        if self._connection is None:
            self.connect()
        cur = self._connection.cursor()
        cur.execute(sql, params)
        return cur.fetchall()