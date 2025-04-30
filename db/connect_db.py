import pymysql

class ConnectDB:
    _instance = None
    _conn = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def conn_db(self):
        if self._conn is None or not self._conn.open:
            self._conn = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="jun_usd",
                charset="utf8",
                cursorclass = pymysql.cursors.DictCursor
            )
        return self._conn