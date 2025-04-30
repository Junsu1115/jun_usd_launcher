from connect_db import ConnectDB
from build_db import *

class QueryDB:
    @staticmethod
    def query_db():
        db = ConnectDB()
        conn = db.conn_db()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM assets")
            rows = cursor.fetchall()
        return rows

    @staticmethod
    def change_db_column():
        db_data = QueryDB.query_db()
        result = []

        for row in db_data:
            asset = (
                AssetBuilder(row)
                .type()
                .name()
                .path()
                .dept()
                .lod()
                .work()
                .ver()
                .get_result()
            )
            result.append(asset)

        return result

print(QueryDB.change_db_column())