import os
from abc import ABC, abstractmethod

class ImportInDCC(ABC):
    @abstractmethod
    def import_usd(self, file_path):
        pass

class ImportInMaya(ImportInDCC):
    def import_usd(self, file_path):
        try:
            if not os.path.exists(file_path):
                return None

            import maya.cmds as cmds
            if not cmds.pluginInfo('mayaUsdPlugin', query=True, loaded=True):
                cmds.loadPlugin('mayaUsdPlugin', quiet=True)

            proxy_node = (cmds.createNode('mayaUsdProxyShape', name='UsdProxyNode'))
            cmds.setAttr(f"{proxy_node}.filePath", file_path, type='string')

        except Exception as e:
            print(e)
            return None

class ImportInHoudini(ImportInDCC):
    def import_usd(self, file_path):
        try:
            if not os.path.exists(file_path):
                return None
        except Exception as e:
            print(e)
            return None

def create_importer() -> ImportInDCC:
    try:
        import maya.cmds as cmds
        return ImportInMaya()
    except ImportError:
        pass
    #
    # try:
    #     import hou
    #     return ImportInHoudini()
    # except ImportError:
    #     pass