import os
from pathlib import Path
from typing import Union


def merge_files(output_file: Union[str, Path], root_dir: str = ".", target_filename: str = "maven_dependency_file") -> None:
    """Merge all dependency files from the directory tree into a single file."""
    files_found = 0

    try:
        with open(output_file, "w", encoding="utf-8") as outfile:
            for dirpath, _, filenames in os.walk(root_dir):
                for fname in filenames:
                    if fname == target_filename:
                        file_path: str = os.path.join(dirpath, fname)
                        try:
                            with open(file_path, "r", encoding="utf-8") as infile:
                                content = infile.read()
                                if content.strip():  # Only write non-empty content
                                    outfile.write(content)
                                    if not content.endswith("\n"):
                                        outfile.write("\n")
                                    files_found += 1
                        except UnicodeDecodeError as e:
                            raise UnicodeDecodeError(
                                e.encoding,
                                e.object,
                                e.start,
                                e.end,
                                f"Error reading '{file_path}': {e.reason}. Please ensure the file is in UTF-8 format.",
                            )
                        except PermissionError:
                            raise PermissionError(f"Permission denied reading '{file_path}'")
    except PermissionError:
        raise PermissionError(f"Permission denied writing to '{output_file}'")
    except OSError as e:
        raise OSError(f"Error writing to '{output_file}': {e}")

    if files_found == 0:
        raise FileNotFoundError(f"No '{target_filename}' files found in '{root_dir}' or its subdirectories")
