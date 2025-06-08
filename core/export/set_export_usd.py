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
        usd_root = '/Users/junsu/Desktop/jun/usd'
        try:
            maya_file_name = os.path.basename(maya_file_path)
            file_name = os.path.splitext(maya_file_name)[0]
            file_parts = file_name.split('_')
            if len(file_parts) < 3:
                raise ValueError("파일명을 asset_dept_lod_v000 형식으로 맞춰주세요.")

            project_name = maya_file_path.split("/")[5]
            asset_type =maya_file_path.split("/")[6]

            ver_file_name = file_parts[3]
            lod_file_name = file_parts[2]
            dept_file_name = file_parts[1]
            asset_file_name = file_parts[0]

            asset_usda = f"{asset_file_name}.usda"
            dept_usda = f"{asset_file_name}_{dept_file_name}.usda"
            lod_usda = f"{asset_file_name}_{dept_file_name}_{lod_file_name}.usda"
            ver_usda = f"{asset_file_name}_{ver_file_name}.usda"

            asset_usda_path = os.path.join(usd_root, project_name, asset_type,
                                           asset_file_name, asset_usda)

            dept_usda_path = os.path.join(usd_root, project_name, asset_type,
                                          asset_file_name, dept_file_name, dept_usda)

            lod_usda_path = os.path.join(usd_root, project_name, asset_type,
                                         asset_file_name, dept_file_name, lod_file_name, lod_usda)

            ver_usda_path = os.path.join(usd_root, project_name, asset_type,
                                         asset_file_name, dept_file_name, lod_file_name, ver_file_name, ver_usda)

            Usd.Stage.Open(asset_usda_path)
            if not os.path.exists(asset_usda_path):
                Usd.Stage.CreateNew(asset_usda_path)

            Usd.Stage.Open(dept_usda_path)
            if not os.path.exists(dept_usda_path):
                Usd.Stage.CreateNew(dept_usda_path)

            Usd.Stage.Open(lod_usda_path)
            if not os.path.exists(lod_usda_path):
                Usd.Stage.CreateNew(lod_usda_path)

            Usd.Stage.SaveAs(ver_usda_path)
            if not os.path.exists(ver_usda_path):
                Usd.Stage.CreateNew(ver_usda_path)

        except Exception as e:
            print(e)