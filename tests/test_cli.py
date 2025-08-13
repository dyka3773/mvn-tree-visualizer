"""Tests for CLI functionality."""

import subprocess
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest

from mvn_tree_visualizer.cli import get_version


def is_valid_version_string(version: str) -> bool:
    """Check if the version string is valid."""
    return (
        version == "unknown"
        or version.replace(".", "").replace("-", "").replace("+", "").replace("dev", "").replace("rc", "").replace("a", "").replace("b", "").isalnum()
    )


class TestVersionFlag:
    """Test the --version/-v flag functionality."""

    def test_get_version_function_returns_string(self):
        """Test that get_version() returns a valid version string."""
        version = get_version()
        assert isinstance(version, str)
        assert len(version) > 0
        # Should either be a proper version (like "1.6.0") or "unknown"

        assert is_valid_version_string(version)

    @patch("mvn_tree_visualizer.cli.metadata.version")
    def test_get_version_handles_package_not_found(self, mock_version):
        """Test that get_version() handles PackageNotFoundError gracefully."""
        from importlib.metadata import PackageNotFoundError

        mock_version.side_effect = PackageNotFoundError("Package not found")

        version = get_version()
        assert version == "unknown"

    @patch("mvn_tree_visualizer.cli.metadata.version")
    def test_get_version_returns_correct_version(self, mock_version):
        """Test that get_version() returns the mocked version."""
        mock_version.return_value = "1.6.0"

        version = get_version()
        assert version == "1.6.0"
        mock_version.assert_called_once_with("mvn-tree-visualizer")

    def test_version_flag_long_form(self):
        """Test --version flag via subprocess."""
        try:
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "mvn_tree_visualizer",
                    "--version",
                ],
                capture_output=True,
                text=True,
                timeout=8,
                cwd=".",
            )

            # Should exit with code 0 (success)
            assert result.returncode == 0

            # Should output version information
            assert "mvn-tree-visualizer" in result.stdout

            # Should not have stderr output for normal version display
            assert result.stderr == ""

        except subprocess.TimeoutExpired:
            pytest.fail("--version command timed out")
        except FileNotFoundError:
            pytest.skip("mvn_tree_visualizer module not available for subprocess testing")

    def test_version_flag_short_form(self):
        """Test -v flag via subprocess."""
        try:
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "mvn_tree_visualizer",
                    "-v",
                ],
                capture_output=True,
                text=True,
                timeout=8,
                cwd=".",
            )

            # Should exit with code 0 (success)
            assert result.returncode == 0

            # Should output version information
            assert "mvn-tree-visualizer" in result.stdout

            # Should not have stderr output for normal version display
            assert result.stderr == ""

        except subprocess.TimeoutExpired:
            pytest.fail("-v command timed out")
        except FileNotFoundError:
            pytest.skip("mvn_tree_visualizer module not available for subprocess testing")

    def test_version_flag_takes_precedence(self):
        """Test that --version flag takes precedence over other arguments."""
        try:
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "mvn_tree_visualizer",
                    "--version",
                    "some_directory",
                ],
                capture_output=True,
                text=True,
                timeout=8,
                cwd=".",
            )

            # Should still exit with code 0 and show version
            assert result.returncode == 0
            assert "mvn-tree-visualizer" in result.stdout

        except subprocess.TimeoutExpired:
            pytest.fail("--version with extra args command timed out")
        except FileNotFoundError:
            pytest.skip("mvn_tree_visualizer module not available for subprocess testing")

    def test_version_output_format(self):
        """Test that version output follows expected format."""
        try:
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "mvn_tree_visualizer",
                    "--version",
                ],
                capture_output=True,
                text=True,
                timeout=8,
                cwd=".",
            )

            if result.returncode == 0:
                # Should be in format "mvn-tree-visualizer X.Y.Z"
                output = result.stdout.strip()
                parts = output.split()
                assert len(parts) == 2
                assert parts[0] == "mvn-tree-visualizer"
                # Second part should be version number
                version_part = parts[1]
                assert len(version_part) > 0

        except subprocess.TimeoutExpired:
            pytest.fail("--version format test command timed out")
        except FileNotFoundError:
            pytest.skip("mvn_tree_visualizer module not available for subprocess testing")


class TestQuietFlag:
    """Test the --quiet/-q flag functionality."""

    def test_quiet_flag_long_form(self):
        """Test --quiet flag suppresses output."""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_output = Path(temp_dir) / "test_diagram.html"

            try:
                result = subprocess.run(
                    [
                        sys.executable,
                        "-m",
                        "mvn_tree_visualizer",
                        "examples/simple-project",
                        "--quiet",
                        "--output",
                        str(temp_output),
                    ],
                    capture_output=True,
                    text=True,
                    timeout=8,
                    cwd=".",
                )

                # Should exit with code 0 (success)
                assert result.returncode == 0

                # Should have no stdout output when quiet
                assert result.stdout.strip() == ""

                # Should not have stderr output for normal operation
                assert result.stderr == ""

                # Should have created the output file
                assert temp_output.exists()

            except subprocess.TimeoutExpired:
                pytest.fail("--quiet command timed out")
            except FileNotFoundError:
                pytest.skip("mvn_tree_visualizer module not available for subprocess testing")

    def test_quiet_flag_short_form(self):
        """Test -q flag suppresses output."""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_output = Path(temp_dir) / "test_diagram.html"

            try:
                result = subprocess.run(
                    [
                        sys.executable,
                        "-m",
                        "mvn_tree_visualizer",
                        "examples/simple-project",
                        "-q",
                        "--output",
                        str(temp_output),
                    ],
                    capture_output=True,
                    text=True,
                    timeout=8,
                    cwd=".",
                )

                # Should exit with code 0 (success)
                assert result.returncode == 0

                # Should have no stdout output when quiet
                assert result.stdout.strip() == ""

                # Should not have stderr output for normal operation
                assert result.stderr == ""

                # Should have created the output file
                assert temp_output.exists()

            except subprocess.TimeoutExpired:
                pytest.fail("-q command timed out")
            except FileNotFoundError:
                pytest.skip("mvn_tree_visualizer module not available for subprocess testing")

    def test_normal_output_without_quiet(self):
        """Test that normal output works when --quiet is not used."""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_output = Path(temp_dir) / "test_diagram.html"

            try:
                result = subprocess.run(
                    [
                        sys.executable,
                        "-m",
                        "mvn_tree_visualizer",
                        "examples/simple-project",
                        "--output",
                        str(temp_output),
                    ],
                    capture_output=True,
                    text=True,
                    timeout=8,
                    cwd=".",
                )

                # Should exit with code 0 (success)
                assert result.returncode == 0

                # Should have stdout output when not quiet
                assert len(result.stdout.strip()) > 0
                assert "Generating initial diagram..." in result.stdout
                assert "Diagram generated and saved" in result.stdout

                # Should not have stderr output for normal operation
                assert result.stderr == ""

                # Should have created the output file
                assert temp_output.exists()

            except subprocess.TimeoutExpired:
                pytest.fail("normal output command timed out")
            except FileNotFoundError:
                pytest.skip("mvn_tree_visualizer module not available for subprocess testing")

    def test_quiet_flag_still_shows_errors(self):
        """Test that --quiet still shows errors on stderr."""
        try:
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "mvn_tree_visualizer",
                    "nonexistent_directory",
                    "--quiet",
                ],
                capture_output=True,
                text=True,
                timeout=8,
                cwd=".",
            )

            # Should exit with non-zero code (error)
            assert result.returncode != 0

            # Should have no stdout output when quiet (even with errors)
            assert result.stdout.strip() == ""

            # Should have stderr output for errors even when quiet
            assert len(result.stderr.strip()) > 0
            assert "ERROR:" in result.stderr

        except subprocess.TimeoutExpired:
            pytest.fail("--quiet error test command timed out")
        except FileNotFoundError:
            pytest.skip("mvn_tree_visualizer module not available for subprocess testing")


class TestOpenFlag:
    """Test the --open flag functionality."""

    @patch("mvn_tree_visualizer.cli.webbrowser.open")
    def test_open_flag_with_html_output(self, mock_browser_open):
        """Test --open flag opens HTML output in browser."""
        from mvn_tree_visualizer.cli import generate_diagram

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_output = Path(temp_dir) / "test_diagram.html"

            # Call generate_diagram with open_browser=True
            generate_diagram(
                directory="examples/simple-project",
                output_file=str(temp_output),
                filename="maven_dependency_file",
                keep_tree=False,
                output_format="html",
                show_versions=False,
                theme="minimal",
                quiet=False,
                open_browser=True,
            )

            # Should have created the output file
            assert temp_output.exists()

            # Should have called webbrowser.open with the correct file URL
            mock_browser_open.assert_called_once()
            call_args = mock_browser_open.call_args[0]
            assert len(call_args) == 1
            assert call_args[0].startswith("file://")
            assert str(temp_output.resolve()) in call_args[0]

    @patch("mvn_tree_visualizer.cli.webbrowser.open")
    def test_open_flag_with_json_output_does_not_open(self, mock_browser_open):
        """Test --open flag does not open JSON output."""
        from mvn_tree_visualizer.cli import generate_diagram

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_output = Path(temp_dir) / "test_diagram.json"

            # Call generate_diagram with open_browser=True but JSON output
            generate_diagram(
                directory="examples/simple-project",
                output_file=str(temp_output),
                filename="maven_dependency_file",
                keep_tree=False,
                output_format="json",
                show_versions=False,
                theme="minimal",
                quiet=False,
                open_browser=True,
            )

            # Should have created the output file
            assert temp_output.exists()

            # Should NOT have called webbrowser.open for JSON format
            mock_browser_open.assert_not_called()

    @patch("mvn_tree_visualizer.cli.webbrowser.open")
    def test_open_flag_in_quiet_mode_does_not_open(self, mock_browser_open):
        """Test --open flag does not open in quiet mode."""
        from mvn_tree_visualizer.cli import generate_diagram

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_output = Path(temp_dir) / "test_diagram.html"

            # Call generate_diagram with open_browser=True but quiet=True
            generate_diagram(
                directory="examples/simple-project",
                output_file=str(temp_output),
                filename="maven_dependency_file",
                keep_tree=False,
                output_format="html",
                show_versions=False,
                theme="minimal",
                quiet=True,
                open_browser=True,
            )

            # Should have created the output file
            assert temp_output.exists()

            # Should NOT have called webbrowser.open in quiet mode
            mock_browser_open.assert_not_called()

    @patch("mvn_tree_visualizer.cli.webbrowser.open")
    def test_open_flag_handles_browser_error_gracefully(self, mock_browser_open):
        """Test --open flag handles browser opening errors gracefully."""
        from mvn_tree_visualizer.cli import generate_diagram

        # Make webbrowser.open raise an exception
        mock_browser_open.side_effect = Exception("Browser not available")

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_output = Path(temp_dir) / "test_diagram.html"

            # This should not raise an exception even if browser opening fails
            generate_diagram(
                directory="examples/simple-project",
                output_file=str(temp_output),
                filename="maven_dependency_file",
                keep_tree=False,
                output_format="html",
                show_versions=False,
                theme="minimal",
                quiet=False,
                open_browser=True,
            )

            # Should have created the output file
            assert temp_output.exists()

            # Should have attempted to call webbrowser.open
            mock_browser_open.assert_called_once()

    def test_open_flag_cli_integration(self):
        """Test --open flag integration via subprocess (without actually opening browser)."""
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_output = Path(temp_dir) / "test_diagram.html"

            try:
                with patch("mvn_tree_visualizer.cli.webbrowser.open"):
                    result = subprocess.run(
                        [
                            sys.executable,
                            "-m",
                            "mvn_tree_visualizer",
                            "examples/simple-project",
                            "--open",
                            "--output",
                            str(temp_output),
                        ],
                        capture_output=True,
                        text=True,
                        timeout=8,
                        cwd=".",
                    )

                    # Should exit with code 0 (success)
                    assert result.returncode == 0

                    # Should have created the output file
                    assert temp_output.exists()

                    # Output should mention opening browser
                    assert "Opening diagram in your default browser" in result.stdout

            except subprocess.TimeoutExpired:
                pytest.fail("--open CLI integration command timed out")
            except FileNotFoundError:
                pytest.skip("mvn_tree_visualizer module not available for subprocess testing")


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
                pytest.skip("mvn_tree_visualizer module not available for subprocess testing")
