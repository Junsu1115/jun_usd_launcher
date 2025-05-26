from pathlib import Path
import os
from pxr import Usd

class MakeDir:
    @staticmethod
    def make_usd_dir(asset_name: str, dept: str, lod: str, ver: str):
        try:
            root = Path("/Users/junsu/Desktop/jun/usd/KJS/character")
            dir_list = [asset_name, dept, lod, ver]
            target_dir = root.joinpath(*dir_list)
            target_dir.mkdir(parents=True, exist_ok=True)
            return target_dir

        except Exception as e:
            print(e)

class PrepareSetting:
    @staticmethod
    def scan_scene(maya_file_name):
        file_name = os.path.splitext(maya_file_name)[0]
        asset_name= file_name.split('_')[0]
        dept = file_name.split('_')[1]
        lod = file_name.split('_')[2]
        ver = file_name.split('_')[3]
        return asset_name, dept, lod, ver

    @staticmethod
    def make_variant_set(maya_file_path):
        try:
            root = Path("/Users/junsu/Desktop/jun/usd")

            maya_file_path = os.path.basename(maya_file_path)

            file_name = os.path.splitext(maya_file_name)[0]
            split_file_name = file_name.split("_")
            asset_file_name = "_".join(split_file_name[:-3])
            dept_file_name = "_".join(split_file_name[:-2])
            lod_file_name = "_".join(split_file_name[:-1])



        except Exception as e:
            print(e)