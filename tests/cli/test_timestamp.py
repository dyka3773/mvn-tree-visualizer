"""Tests for CLI --timestamp-output flag functionality."""

import subprocess
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest


class TestTimestampOutputFlag:
    """Test the --timestamp-output flag functionality."""

    def test_add_timestamp_to_filename_helper_function(self):
        """Test the add_timestamp_to_filename helper function."""
        from mvn_tree_visualizer.cli import add_timestamp_to_filename

        # Test with HTML file
        result = add_timestamp_to_filename("diagram.html")
        assert result.startswith("diagram-")
        assert result.endswith(".html")
        assert len(result) == len("diagram-2025-08-13-203045.html")

        # Test with JSON file
        result = add_timestamp_to_filename("output.json")
        assert result.startswith("output-")
        assert result.endswith(".json")

        # Test with custom name
        result = add_timestamp_to_filename("my-project.html")
        assert result.startswith("my-project-")
        assert result.endswith(".html")

        # Test with path
        result = add_timestamp_to_filename("folder/diagram.html")
        assert ("/" in result) or ("\\" in result)  # Should preserve path (handle both Unix and Windows separators)
        assert result.endswith(".html")

    def test_timestamp_format_consistency(self):
        """Test that timestamp format is consistent and valid."""
        import re

        from mvn_tree_visualizer.cli import add_timestamp_to_filename

        result = add_timestamp_to_filename("test.html")
        # Extract timestamp part (between last dash and .html)
        timestamp_pattern = r"test-(\d{4}-\d{2}-\d{2}-\d{6})\.html"
        match = re.search(timestamp_pattern, result)

        assert match is not None, f"Timestamp format invalid in: {result}"
        timestamp = match.group(1)

        # Verify format YYYY-MM-DD-HHMMSS
        assert len(timestamp) == 17  # 2025-08-13-203045
        assert timestamp[4] == "-"
        assert timestamp[7] == "-"
        assert timestamp[10] == "-"

    def test_timestamp_output_flag_with_html(self):
        """Test --timestamp-output with HTML output."""
        with tempfile.TemporaryDirectory() as temp_dir:
            try:
                result = subprocess.run(
                    [
                        sys.executable,
                        "-m",
                        "mvn_tree_visualizer",
                        "examples/simple-project",
                        "--timestamp-output",
                        "--output",
                        str(Path(temp_dir) / "test.html"),
                    ],
                    capture_output=True,
                    text=True,
                    timeout=8,
                    cwd=".",
                )

                # Should exit with code 0 (success)
                assert result.returncode == 0

                # Should have created a timestamped file
                html_files = list(Path(temp_dir).glob("test-*.html"))
                assert len(html_files) == 1

                created_file = html_files[0]
                assert created_file.name.startswith("test-")
                assert created_file.name.endswith(".html")
                assert created_file.exists()

                # Output should mention the timestamped filename
                assert created_file.name in result.stdout

            except subprocess.TimeoutExpired:
                pytest.fail("--timestamp-output HTML test timed out")
            except FileNotFoundError:
                pytest.skip("mvn_tree_visualizer module not available for subprocess testing")

    def test_timestamp_output_flag_with_json(self):
        """Test --timestamp-output with JSON output."""
        with tempfile.TemporaryDirectory() as temp_dir:
            try:
                result = subprocess.run(
                    [
                        sys.executable,
                        "-m",
                        "mvn_tree_visualizer",
                        "examples/simple-project",
                        "--timestamp-output",
                        "--output",
                        str(Path(temp_dir) / "test.json"),
                        "--format",
                        "json",
                    ],
                    capture_output=True,
                    text=True,
                    timeout=8,
                    cwd=".",
                )

                # Should exit with code 0 (success)
                assert result.returncode == 0

                # Should have created a timestamped file
                json_files = list(Path(temp_dir).glob("test-*.json"))
                assert len(json_files) == 1

                created_file = json_files[0]
                assert created_file.name.startswith("test-")
                assert created_file.name.endswith(".json")
                assert created_file.exists()

            except subprocess.TimeoutExpired:
                pytest.fail("--timestamp-output JSON test timed out")
            except FileNotFoundError:
                pytest.skip("mvn_tree_visualizer module not available for subprocess testing")

    def test_timestamp_output_flag_with_default_filename(self):
        """Test --timestamp-output with default diagram.html filename."""
        with tempfile.TemporaryDirectory() as temp_dir:
            original_cwd = Path.cwd()
            try:
                # Change to temp directory so default output goes there
                import os

                os.chdir(temp_dir)

                result = subprocess.run(
                    [
                        sys.executable,
                        "-m",
                        "mvn_tree_visualizer",
                        str(original_cwd / "examples/simple-project"),
                        "--timestamp-output",
                    ],
                    capture_output=True,
                    text=True,
                    timeout=8,
                    cwd=".",
                )

                # Should exit with code 0 (success)
                assert result.returncode == 0

                # Should have created a timestamped file with default name
                html_files = list(Path(".").glob("diagram-*.html"))
                assert len(html_files) == 1

                created_file = html_files[0]
                assert created_file.name.startswith("diagram-")
                assert created_file.name.endswith(".html")
                assert created_file.exists()

            except subprocess.TimeoutExpired:
                pytest.fail("--timestamp-output default filename test timed out")
            except FileNotFoundError:
                pytest.skip("mvn_tree_visualizer module not available for subprocess testing")
            finally:
                os.chdir(original_cwd)

    def test_timestamp_output_with_quiet_mode(self):
        """Test --timestamp-output works with --quiet mode."""
        with tempfile.TemporaryDirectory() as temp_dir:
            try:
                result = subprocess.run(
                    [
                        sys.executable,
                        "-m",
                        "mvn_tree_visualizer",
                        "examples/simple-project",
                        "--timestamp-output",
                        "--quiet",
                        "--output",
                        str(Path(temp_dir) / "test.html"),
                    ],
                    capture_output=True,
                    text=True,
                    timeout=8,
                    cwd=".",
                )

                # Should exit with code 0 (success)
                assert result.returncode == 0

                # Should have no output in quiet mode
                assert result.stdout.strip() == ""

                # Should have created a timestamped file
                html_files = list(Path(temp_dir).glob("test-*.html"))
                assert len(html_files) == 1

            except subprocess.TimeoutExpired:
                pytest.fail("--timestamp-output quiet mode test timed out")
            except FileNotFoundError:
                pytest.skip("mvn_tree_visualizer module not available for subprocess testing")

    def test_timestamp_output_combined_with_open_flag(self):
        """Test --timestamp-output combined with --open flag."""
        with tempfile.TemporaryDirectory() as temp_dir:
            try:
                with patch("mvn_tree_visualizer.cli.webbrowser.open"):
                    result = subprocess.run(
                        [
                            sys.executable,
                            "-m",
                            "mvn_tree_visualizer",
                            "examples/simple-project",
                            "--timestamp-output",
                            "--open",
                            "--output",
                            str(Path(temp_dir) / "test.html"),
                        ],
                        capture_output=True,
                        text=True,
                        timeout=8,
                        cwd=".",
                    )

                    # Should exit with code 0 (success)
                    assert result.returncode == 0

                    # Should have created a timestamped file
                    html_files = list(Path(temp_dir).glob("test-*.html"))
                    assert len(html_files) == 1

                    # Should mention opening browser with timestamped filename
                    assert "Opening diagram in your default browser" in result.stdout

            except subprocess.TimeoutExpired:
                pytest.fail("--timestamp-output with --open test timed out")
            except FileNotFoundError:
                pytest.skip("mvn_tree_visualizer module not available for subprocess testing")
