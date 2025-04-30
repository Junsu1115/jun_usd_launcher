import os

from abc import ABC, abstractmethod

from pxr import Usd

class USDExporter(ABC):
    @abstractmethod
    def export(self):
        pass

    def make_dirs(self):
        root_path = "/Users/junsu/Desktop"
        project_name = "jun"
        entity_type = "asset"
        asset_type = "character"
        asset_name = "hello"
        dept = "model"
        lod = "lo"
        work = "dev"
        ver = "v001"

        path = os.path.join(root_path, project_name, entity_type, asset_type, asset_name, dept, lod, work)
        if not os.path.exists(path):
            os.makedirs(path)

        return path


class ExportMaya(USDExporter):
    def export(self):
        self.make_dirs()
        asset_name = "hello_model_lo_v001.usdc"
        usd_root_path = os.path.join(self.make_dirs(), asset_name)
        Usd.Stage.CreateNew(usd_root_path)
        if os.path.exists(usd_root_path):
            Usd.Stage.Open(usd_root_path)

def create_usd() -> USDExporter:
    try:
        import maya.cmds as cmds
        return ExportMaya()
    except ImportError:
        pass