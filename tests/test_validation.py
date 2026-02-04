import os
import tempfile
from pathlib import Path

import pytest

from mvn_tree_visualizer.exceptions import DependencyFileNotFoundError, OutputGenerationError
from mvn_tree_visualizer.validation import find_dependency_files, validate_dependency_files, validate_directory, validate_output_directory


def test_find_dependency_files_recurses():
    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        (root / "a" / "b").mkdir(parents=True)
        (root / "a" / "b" / "maven_dependency_file").write_text("x")

        found = find_dependency_files(temp_dir, "maven_dependency_file")

        assert len(found) == 1
        assert found[0].endswith("maven_dependency_file")


def test_validate_directory_missing():
    with pytest.raises(DependencyFileNotFoundError):
        validate_directory("not-a-real-dir")


def test_validate_directory_not_a_dir():
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / "file.txt"
        file_path.write_text("x")

        with pytest.raises(DependencyFileNotFoundError):
            validate_directory(str(file_path))


def test_validate_directory_not_readable(monkeypatch):
    with tempfile.TemporaryDirectory() as temp_dir:
        monkeypatch.setattr(os, "access", lambda *_args, **_kwargs: False)

        with pytest.raises(DependencyFileNotFoundError):
            validate_directory(temp_dir)


def test_validate_dependency_files_none_found():
    with tempfile.TemporaryDirectory() as temp_dir:
        with pytest.raises(DependencyFileNotFoundError):
            validate_dependency_files(temp_dir, "maven_dependency_file")


def test_validate_dependency_files_unreadable(monkeypatch):
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = Path(temp_dir) / "maven_dependency_file"
        file_path.write_text("x")

        def access_side_effect(path, *_args, **_kwargs):
            return not str(path).endswith("maven_dependency_file")

        monkeypatch.setattr(os, "access", access_side_effect)

        with pytest.raises(DependencyFileNotFoundError):
            validate_dependency_files(temp_dir, "maven_dependency_file")


def test_validate_output_directory_creates():
    with tempfile.TemporaryDirectory() as temp_dir:
        out_dir = Path(temp_dir) / "nested" / "out"
        output_file = out_dir / "diagram.html"

        validate_output_directory(str(output_file))

        assert out_dir.exists()


def test_validate_output_directory_permission_error(monkeypatch):
    with tempfile.TemporaryDirectory() as temp_dir:
        output_file = Path(temp_dir) / "out" / "diagram.html"

        def raise_permission_error(*_args, **_kwargs):
            raise PermissionError("nope")

        monkeypatch.setattr(Path, "mkdir", raise_permission_error, raising=False)

        with pytest.raises(OutputGenerationError):
            validate_output_directory(str(output_file))


def test_validate_output_directory_generic_error(monkeypatch):
    with tempfile.TemporaryDirectory() as temp_dir:
        output_file = Path(temp_dir) / "out" / "diagram.html"

        def raise_runtime_error(*_args, **_kwargs):
            raise RuntimeError("boom")

        monkeypatch.setattr(Path, "mkdir", raise_runtime_error, raising=False)

        with pytest.raises(OutputGenerationError):
            validate_output_directory(str(output_file))


def test_validate_output_directory_not_writable(monkeypatch):
    with tempfile.TemporaryDirectory() as temp_dir:
        output_file = Path(temp_dir) / "diagram.html"
        monkeypatch.setattr(os, "access", lambda *_args, **_kwargs: False)

        with pytest.raises(OutputGenerationError):
            validate_output_directory(str(output_file))
