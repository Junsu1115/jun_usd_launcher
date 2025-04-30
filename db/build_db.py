from column_db import *
class AssetBuilder:
    def __init__(self, row: dict):
        self.row = row
        self.result = []

    def type(self):
        self.result.append(Type(self.row['type_id']).name)
        return self

    def name(self):
        self.result.append(self.row['name'])
        return self

    def path(self):
        self.result.append(self.row['path'])
        return self

    def dept(self):
        self.result.append(Dept(self.row['dept_id']).name)
        return self

    def lod(self):
        self.result.append(Lod(self.row['lod_id']).name)
        return self

    def work(self):
        self.result.append(Work(self.row['work_id']).name)
        return self

    def ver(self):
        self.result.append(self.row['ver'])
        return self

    def get_result(self):
        return tuple(self.result)