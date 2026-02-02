import os
import tempfile
from pathlib import Path

import pytest

from mvn_tree_visualizer.cli import cli, generate_diagram, get_version
from mvn_tree_visualizer.exceptions import DependencyFileNotFoundError, DependencyParsingError, OutputGenerationError


# Test: get_version returns a string
def test_get_version_returns_string():
    assert isinstance(get_version(), str)


# Test: generate_diagram raises error for invalid directory
def test_generate_diagram_invalid_directory():
    with pytest.raises(DependencyFileNotFoundError):
        generate_diagram(
            directory="nonexistent_dir",
            output_file="output.html",
            filename="maven_dependency_file",
            keep_tree=False,
            output_format="html",
            show_versions=False,
        )


# Test: generate_diagram raises error for empty dependency file
def test_generate_diagram_empty_dependency_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        dep_file = Path(temp_dir) / "maven_dependency_file"
        dep_file.write_text("")
        output_file = Path(temp_dir) / "output.html"
        with pytest.raises(DependencyParsingError):
            generate_diagram(
                directory=temp_dir,
                output_file=str(output_file),
                filename="maven_dependency_file",
                keep_tree=False,
                output_format="html",
                show_versions=False,
            )


# Test: generate_diagram raises error for permission denied
@pytest.mark.skipif(os.name != "nt", reason="Permission test is Windows-specific")
def test_generate_diagram_permission_denied(monkeypatch):
    with tempfile.TemporaryDirectory() as temp_dir:
        dep_file = Path(temp_dir) / "maven_dependency_file"
        dep_file.write_text("some content")
        output_file = Path(temp_dir) / "output.html"

        def raise_permission_error(*_args, **_kwargs):
            raise PermissionError("no read")

        monkeypatch.setattr("mvn_tree_visualizer.cli.merge_files", raise_permission_error)

        with pytest.raises(DependencyParsingError):
            generate_diagram(
                directory=temp_dir,
                output_file=str(output_file),
                filename="maven_dependency_file",
                keep_tree=False,
                output_format="html",
                show_versions=False,
                quiet=True,
            )


# Test: generate_diagram with quiet mode (should not print extra info)
def test_generate_diagram_quiet_mode(monkeypatch):
    with tempfile.TemporaryDirectory() as temp_dir:
        dep_file = Path(temp_dir) / "maven_dependency_file"
        dep_file.write_text("some content")
        output_file = Path(temp_dir) / "output.html"
        monkeypatch.setattr("mvn_tree_visualizer.cli.create_diagram", lambda **kwargs: "digraph G {}")
        monkeypatch.setattr("mvn_tree_visualizer.cli.create_html_diagram", lambda *args, **kwargs: None)
        monkeypatch.setattr("mvn_tree_visualizer.cli.create_json_output", lambda *args, **kwargs: None)
        generate_diagram(
            directory=temp_dir,
            output_file=str(output_file),
            filename="maven_dependency_file",
            keep_tree=False,
            output_format="html",
            show_versions=False,
            quiet=True,
        )


def test_generate_diagram_unsupported_format():
    with tempfile.TemporaryDirectory() as temp_dir:
        dep_file = Path(temp_dir) / "maven_dependency_file"
        dep_file.write_text("group:artifact:1.0")
        output_file = Path(temp_dir) / "output.txt"
        with pytest.raises(OutputGenerationError):
            generate_diagram(
                directory=temp_dir,
                output_file=str(output_file),
                filename="maven_dependency_file",
                keep_tree=False,
                output_format="txt",
                show_versions=False,
            )


def test_generate_diagram_open_browser_quiet_does_not_open(monkeypatch):
    with tempfile.TemporaryDirectory() as temp_dir:
        dep_file = Path(temp_dir) / "maven_dependency_file"
        dep_file.write_text("group:artifact:1.0")
        output_file = Path(temp_dir) / "output.html"
        opened = []

        def fake_open(_):
            opened.append(True)

        monkeypatch.setattr("mvn_tree_visualizer.cli.webbrowser.open", fake_open)
        monkeypatch.setattr("mvn_tree_visualizer.cli.create_html_diagram", lambda *_args, **_kwargs: None)

        generate_diagram(
            directory=temp_dir,
            output_file=str(output_file),
            filename="maven_dependency_file",
            keep_tree=False,
            output_format="html",
            show_versions=False,
            quiet=True,
            open_browser=True,
        )

        assert not opened


def test_generate_diagram_output_permission_error(monkeypatch):
    with tempfile.TemporaryDirectory() as temp_dir:
        dep_file = Path(temp_dir) / "maven_dependency_file"
        dep_file.write_text("group:artifact:1.0")
        output_file = Path(temp_dir) / "output.html"

        def raise_permission_error(*_args, **_kwargs):
            raise PermissionError("no write")

        monkeypatch.setattr("mvn_tree_visualizer.cli.create_html_diagram", raise_permission_error)

        with pytest.raises(OutputGenerationError):
            generate_diagram(
                directory=temp_dir,
                output_file=str(output_file),
                filename="maven_dependency_file",
                keep_tree=False,
                output_format="html",
                show_versions=False,
                quiet=True,
            )


def test_cli_timestamp_output_applies_timestamp(monkeypatch):
    called = {}

    def fake_generate_diagram(*args, **kwargs):
        called["args"] = args
        called["kwargs"] = kwargs

    monkeypatch.setattr("mvn_tree_visualizer.cli.generate_diagram", fake_generate_diagram)
    monkeypatch.setattr("mvn_tree_visualizer.cli.add_timestamp_to_filename", lambda _f: "diagram-TEST.html")
    monkeypatch.setattr("sys.argv", ["mvn-tree-visualizer", "--timestamp-output", "--output", "diagram.html"])

    cli()

    assert called["args"][1] == "diagram-TEST.html"


def test_cli_watch_mode_starts_watcher(monkeypatch):
    events = {"started": False, "waited": False}

    class DummyWatcher:
        def __init__(self, *_args, **_kwargs):
            pass

        def start(self):
            events["started"] = True

        def wait(self):
            events["waited"] = True

    monkeypatch.setattr("mvn_tree_visualizer.cli.FileWatcher", DummyWatcher)
    monkeypatch.setattr("mvn_tree_visualizer.cli.generate_diagram", lambda *_args, **_kwargs: None)
    monkeypatch.setattr("sys.argv", ["mvn-tree-visualizer", "--watch"])

    cli()

    assert events["started"] is True
    assert events["waited"] is True


def test_cli_exits_with_error_on_dependency_error(monkeypatch):
    def raise_error(*_args, **_kwargs):
        raise DependencyParsingError("boom")

    monkeypatch.setattr("mvn_tree_visualizer.cli.generate_diagram", raise_error)
    monkeypatch.setattr("sys.argv", ["mvn-tree-visualizer"])

    with pytest.raises(SystemExit) as exc:
        cli()

    assert exc.value.code == 1
