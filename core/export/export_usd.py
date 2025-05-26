import os
import json
from abc import ABC, abstractmethod

from core.export.setting_dir import maya_file_name
from setting_dir import MakeDir, PrepareSetting

class USDExporter(ABC):
    def __init__(self):
        super().__init__()
        with open("/Users/junsu/Desktop/jun_usd_helper/core/export/export_option.json", "r") as f:
            self.export_option = json.load(f)

    @abstractmethod
    def export(self):
        pass

class ExportMaya(USDExporter):
    def export(self):
        try:
            import maya.cmds as cmds
            if not cmds.pluginInfo("mayaUsdPlugin", query=True, loaded=True):
                cmds.loadPlugin("mayaUsdPlugin")
            cmds.select(clear=True)

        except ImportError as e:
            print(e)
            return

        maya_file_path = cmds.file(q=True, sn=True)
        if maya_file_path == "":
            print("maya_file_path is empty")
            return

        maya_file_name = os.path.basename(maya_file_path)
        asset_name, dept, lod, ver = PrepareSetting.scan_scene(maya_file_name)
        matches = cmds.ls(asset_name, long=True)
        target_dir = MakeDir.make_usd_dir(asset_name, dept, lod, ver)
        usd_ver_name = os.path.splitext(maya_file_name)[0] + ".usdc"

        if dept == "model":
            options = self.export_option['maya']['model']
            if matches:
                usdc_file_path = os.path.join(target_dir, usd_ver_name)
                root_node = matches[0]
                export_list = [root_node] + cmds.listRelatives(root_node, allDescendents=True, fullPath=True) or []
                cmds.select(export_list, replace=True)
                cmds.mayaUSDExport(file = usdc_file_path, selection=True, **options)


def create_usd() -> USDExporter:
    try:
        import maya.cmds  # noqa: F401
        return ExportMaya()

    except ImportError as e:
        print(e)