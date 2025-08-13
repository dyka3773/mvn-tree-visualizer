"""Tests for CLI --quiet/-q flag functionality."""

import subprocess
import sys
import tempfile
from pathlib import Path

import pytest


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
