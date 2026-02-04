import tempfile
from pathlib import Path

import pytest

from mvn_tree_visualizer.get_dependencies_in_one_file import merge_files


def test_merge_files_collects_content():
    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        (root / "a").mkdir()
        (root / "b").mkdir()
        (root / "a" / "maven_dependency_file").write_text("a1")
        (root / "b" / "maven_dependency_file").write_text("b1\n")
        output_file = root / "dependency_tree.txt"

        merge_files(output_file=output_file, root_dir=temp_dir, target_filename="maven_dependency_file")

        content = output_file.read_text()
        assert "a1" in content
        assert "b1" in content


def test_merge_files_no_files_found():
    with tempfile.TemporaryDirectory() as temp_dir:
        output_file = Path(temp_dir) / "dependency_tree.txt"

        with pytest.raises(FileNotFoundError):
            merge_files(output_file=output_file, root_dir=temp_dir, target_filename="maven_dependency_file")


def test_merge_files_unicode_decode_error(monkeypatch):
    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        file_path = root / "maven_dependency_file"
        file_path.write_bytes(b"\xff")
        output_file = root / "dependency_tree.txt"
        with pytest.raises(UnicodeDecodeError):
            merge_files(output_file=output_file, root_dir=temp_dir, target_filename="maven_dependency_file")


def test_merge_files_permission_error_on_output(monkeypatch):
    with tempfile.TemporaryDirectory() as temp_dir:
        output_file = Path(temp_dir) / "dependency_tree.txt"
        original_open = open

        def open_with_permission_error(path, *args, **kwargs):
            if str(path).endswith("dependency_tree.txt"):
                raise PermissionError("no write")
            return original_open(path, *args, **kwargs)

        monkeypatch.setattr("builtins.open", open_with_permission_error)

        with pytest.raises(PermissionError):
            merge_files(output_file=output_file, root_dir=temp_dir, target_filename="maven_dependency_file")


def test_merge_files_permission_error_on_input(monkeypatch):
    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        file_path = root / "maven_dependency_file"
        file_path.write_text("x")
        output_file = root / "dependency_tree.txt"
        original_open = open

        def open_with_permission_error(path, *args, **kwargs):
            if str(path).endswith("maven_dependency_file"):
                raise PermissionError("no read")
            return original_open(path, *args, **kwargs)

        monkeypatch.setattr("builtins.open", open_with_permission_error)

        with pytest.raises(PermissionError):
            merge_files(output_file=output_file, root_dir=temp_dir, target_filename="maven_dependency_file")


def test_merge_files_os_error_on_output(monkeypatch):
    with tempfile.TemporaryDirectory() as temp_dir:
        output_file = Path(temp_dir) / "dependency_tree.txt"
        original_open = open

        def open_with_os_error(path, *args, **kwargs):
            if str(path).endswith("dependency_tree.txt"):
                raise OSError("disk full")
            return original_open(path, *args, **kwargs)

        monkeypatch.setattr("builtins.open", open_with_os_error)

        with pytest.raises(OSError):
            merge_files(output_file=output_file, root_dir=temp_dir, target_filename="maven_dependency_file")
