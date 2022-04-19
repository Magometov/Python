import os
import shutil
import pathlib


def find_html_file(structure: str, new_file: str) -> None:
    os.makedirs(f"{structure}/{new_file}", exist_ok=True)
    destination_path = os.path.join(pathlib.Path.cwd(), structure, new_file)
    try:
        for root, dirs, files in os.walk(structure):
            el = root.split('\\')
            if el[-1] == 'templates':
                source_path = os.path.join(pathlib.Path.cwd(), '\\'.join(el), el[-2])
                new_location = shutil.move(source_path, destination_path)

    except:
        pass


find_html_file('my_project_2', 'templates')
