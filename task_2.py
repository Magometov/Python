import os
from pathlib import Path
from typing import Union

import yaml


def create_project(structure: Union[dict, str, list], path: list = ["."]) -> None:
    if isinstance(structure, dict):
        for folder, files in structure.items():
            curdir = path[:] + [folder]
            os.mkdir(os.path.join(*curdir))

            if isinstance(files, list):
                for file in files:
                    create_project(file, curdir)
            elif isinstance(files, str):
                Path(os.path.join(*(curdir[:]+[files]))).touch()
            else:
                print("error", curdir, files)
    elif isinstance(structure, str):
        Path(os.path.join(*(path[:]+[structure]))).touch()
    elif isinstance(structure, list):
        for file in structure:
            create_project(file, path)
    else:
        print("error", path, structure)
    return


if __name__ == '__main__':
    with open('config.yaml', 'r') as file:
        data = yaml.safe_load(file)

    create_project(data)