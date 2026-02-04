import builtins
import tempfile
from pathlib import Path

import pytest

from mvn_tree_visualizer.diagram import create_diagram


def test_create_diagram_reads_and_removes_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / "dependency_tree.txt"
        file_path.write_text("root -> child")

        result = create_diagram(keep_tree=False, intermediate_filename=str(file_path))

        assert result == "root -> child"
        assert not file_path.exists()


def test_create_diagram_keeps_file_when_requested():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / "dependency_tree.txt"
        file_path.write_text("root -> child")

        result = create_diagram(keep_tree=True, intermediate_filename=str(file_path))

        assert result == "root -> child"
        assert file_path.exists()


def test_create_diagram_missing_file_raises():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / "missing.txt"
        with pytest.raises(FileNotFoundError):
            create_diagram(keep_tree=False, intermediate_filename=str(file_path))


def test_create_diagram_permission_error(monkeypatch):
    def raise_permission_error(*args, **kwargs):
        if args and args[0].endswith("dependency_tree.txt"):
            raise PermissionError("no read")
        return original_open(*args, **kwargs)

    original_open = builtins.open

    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / "dependency_tree.txt"
        file_path.write_text("root -> child")

        monkeypatch.setattr(builtins, "open", raise_permission_error)

        with pytest.raises(PermissionError):
            create_diagram(keep_tree=False, intermediate_filename=str(file_path))


def test_create_diagram_unicode_decode_error(monkeypatch):
    def raise_unicode_error(*args, **kwargs):
        if args and args[0].endswith("dependency_tree.txt"):
            raise UnicodeDecodeError("utf-8", b"\xff", 0, 1, "invalid")
        return original_open(*args, **kwargs)

    original_open = builtins.open

    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / "dependency_tree.txt"
        file_path.write_text("root -> child")

        monkeypatch.setattr(builtins, "open", raise_unicode_error)

        with pytest.raises(UnicodeDecodeError):
            create_diagram(keep_tree=False, intermediate_filename=str(file_path))


def test_create_diagram_remove_os_error(monkeypatch):
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / "dependency_tree.txt"
        file_path.write_text("root -> child")

        def raise_os_error(_path):
            raise OSError("no remove")

        monkeypatch.setattr("mvn_tree_visualizer.diagram.os.remove", raise_os_error)

        result = create_diagram(keep_tree=False, intermediate_filename=str(file_path))

        assert result == "root -> child"
