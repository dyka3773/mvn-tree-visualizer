"""Tests for CLI --version/-v flag functionality."""

import subprocess
import sys
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
