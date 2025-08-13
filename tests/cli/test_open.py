"""Tests for CLI --open flag functionality."""

import subprocess
import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

import pytest


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
