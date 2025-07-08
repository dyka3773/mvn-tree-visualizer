import os
from pathlib import Path
from typing import Union


def merge_files(output_file: Union[str, Path], root_dir: str = ".", target_filename: str = "maven_dependency_file") -> None:
    with open(output_file, "w", encoding="utf-8") as outfile:
        for dirpath, _, filenames in os.walk(root_dir):
            for fname in filenames:
                if fname == target_filename:
                    file_path: str = os.path.join(dirpath, fname)
                    with open(file_path, "r", encoding="utf-8") as infile:
                        outfile.write(infile.read())
