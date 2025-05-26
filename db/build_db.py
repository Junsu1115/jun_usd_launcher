from dataclasses import dataclass

@dataclass
class AssetViewData:
    type: str
    name: str
    path: str
    dept: str
    lod: str
    work: str
    ver: int

class AssetBuilder:
    def __init__(self, row: dict):
        self.row = row

    def build(self) -> AssetViewData:
        return AssetViewData(
            type=Type(self.row['type_id']).name,
            name=self.row['name'],
            path=self.row['path'],
            dept=Dept(self.row['dept_id']).name,
            lod=Lod(self.row['lod_id']).name,
            work=Work(self.row['work_id']).name,
            ver=self.row['ver']
        )
