import tempfile
from pathlib import Path

from mvn_tree_visualizer.cli import generate_diagram
from mvn_tree_visualizer.file_watcher import DependencyFileHandler


def test_generate_diagram():
    """Test the generate_diagram function works correctly."""
    dependency_tree = """[INFO] com.example:test:jar:1.0.0
[INFO] \\- org.apache.commons:commons-lang3:jar:3.12.0:compile
"""

    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test dependency file
        dep_file = Path(temp_dir) / "maven_dependency_file"
        dep_file.write_text(dependency_tree)

        output_file = Path(temp_dir) / "test.html"

        # Test HTML generation
        generate_diagram(
            directory=temp_dir,
            output_file=str(output_file),
            filename="maven_dependency_file",
            keep_tree=False,
            output_format="html",
            show_versions=False,
        )

        assert output_file.exists()
        content = output_file.read_text()
        assert "test" in content  # The package name without groupId in the diagram
        assert "commons-lang3" in content


def test_generate_diagram_json():
    """Test the generate_diagram function works with JSON output."""
    dependency_tree = """[INFO] com.example:test:jar:1.0.0
[INFO] \\- org.apache.commons:commons-lang3:jar:3.12.0:compile
"""

    with tempfile.TemporaryDirectory() as temp_dir:
        # Create test dependency file
        dep_file = Path(temp_dir) / "maven_dependency_file"
        dep_file.write_text(dependency_tree)

        output_file = Path(temp_dir) / "test.json"

        # Test JSON generation
        generate_diagram(
            directory=temp_dir,
            output_file=str(output_file),
            filename="maven_dependency_file",
            keep_tree=False,
            output_format="json",
            show_versions=False,
        )

        assert output_file.exists()
        content = output_file.read_text()
        assert '"id": "test"' in content  # JSON now uses simplified package names like HTML
        assert '"id": "commons-lang3"' in content


def test_dependency_file_handler():
    """Test the DependencyFileHandler class."""
    callback_called = False

    def test_callback():
        nonlocal callback_called
        callback_called = True

    # Create handler
    handler = DependencyFileHandler("maven_dependency_file", test_callback)

    # Verify handler attributes are set correctly
    assert handler.filename == "maven_dependency_file"
    assert handler.callback == test_callback

    # Verify callback can be called
    handler.callback()
    assert callback_called


def test_generate_diagram_error_handling():
    """Test that generate_diagram handles errors gracefully."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Try to generate diagram with non-existent file
        output_file = Path(temp_dir) / "test.html"

        # This should not raise an exception, but should print an error
        # and NOT create an output file (improved error handling)
        generate_diagram(
            directory=temp_dir,
            output_file=str(output_file),
            filename="non_existent_file",
            keep_tree=False,
            output_format="html",
            show_versions=False,
        )

        # With improved error handling, no output file should be created
        # when there are no dependency files to process
        assert not output_file.exists()


def test_generate_diagram_invalid_directory():
    """Test error handling for invalid directory."""
    with tempfile.TemporaryDirectory() as temp_dir:
        output_file = Path(temp_dir) / "test.html"

        # Test with non-existent directory
        generate_diagram(
            directory="non_existent_directory",
            output_file=str(output_file),
            filename="maven_dependency_file",
            keep_tree=False,
            output_format="html",
            show_versions=False,
        )

        # Should not create output file when directory doesn't exist
        assert not output_file.exists()


def test_generate_diagram_empty_dependency_file():
    """Test error handling for empty dependency files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create an empty dependency file
        empty_file = Path(temp_dir) / "maven_dependency_file"
        empty_file.write_text("")

        output_file = Path(temp_dir) / "test.html"

        generate_diagram(
            directory=temp_dir,
            output_file=str(output_file),
            filename="maven_dependency_file",
            keep_tree=False,
            output_format="html",
            show_versions=False,
        )

        # Should not create output file when dependency file is empty
        assert not output_file.exists()


def test_generate_diagram_whitespace_only_dependency_file():
    """Test error handling for dependency files with only whitespace."""
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a dependency file with only whitespace
        whitespace_file = Path(temp_dir) / "maven_dependency_file"
        whitespace_file.write_text("   \n\t\n   ")

        output_file = Path(temp_dir) / "test.html"

        generate_diagram(
            directory=temp_dir,
            output_file=str(output_file),
            filename="maven_dependency_file",
            keep_tree=False,
            output_format="html",
            show_versions=False,
        )

        # Should not create output file when dependency file contains only whitespace
        assert not output_file.exists()
