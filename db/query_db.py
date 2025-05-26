from connect_db import ConnectDB
from column_db import *
from dataclasses import dataclass

import pymysql

@dataclass
class AssetViewData:
    type: str
    name: str
    path: str
    dept: str
    lod: str
    work: str
    ver: int

class QueryDB:
    @staticmethod
    def query_db():
        db = ConnectDB()
        conn = db.conn_db()
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute("SELECT * FROM assets")
            rows = cursor.fetchall()
        return rows

    @staticmethod
    def db():
        rows = QueryDB.query_db()
        return [
            AssetViewData(
                type=Type(row['type_id']).name,
                name=row['name'],
                path=row['path'],
                dept=Dept(row['dept_id']).name,
                lod=Lod(row['lod_id']).name,
                work=Work(row['work_id']).name,
                ver=row['ver']
            )
            for row in rows
        ]
