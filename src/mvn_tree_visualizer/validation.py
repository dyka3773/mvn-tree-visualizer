"""Validation utilities for mvn-tree-visualizer."""

import os
from pathlib import Path

from .exceptions import DependencyFileNotFoundError, OutputGenerationError


def find_dependency_files(directory: str, filename: str) -> list[str]:
    """Find all dependency files in the directory tree."""
    found_files = []
    for dirpath, _, filenames in os.walk(directory):
        if filename in filenames:
            found_files.append(os.path.join(dirpath, filename))
    return found_files


def print_maven_help() -> None:
    """Print helpful Maven commands for generating dependency files."""
    print("\n💡 To generate a Maven dependency file, try one of these commands:")
    print("   mvn dependency:tree -DoutputFile=maven_dependency_file")
    print("   mvn dependency:tree > maven_dependency_file")
    print("   mvn dependency:tree -DoutputFile=maven_dependency_file -DoutputType=text")
    print("\n📍 Make sure you're in a directory with a pom.xml file.")


def validate_directory(directory: str) -> None:
    """Validate that the directory exists and is accessible."""
    if not os.path.exists(directory):
        raise DependencyFileNotFoundError(f"Directory '{directory}' does not exist.\nPlease check the path and try again.")

    if not os.path.isdir(directory):
        raise DependencyFileNotFoundError(f"'{directory}' is not a directory.\nPlease provide a valid directory path.")

    if not os.access(directory, os.R_OK):
        raise DependencyFileNotFoundError(f"Cannot read from directory '{directory}'.\nPlease check your permissions and try again.")


def validate_dependency_files(directory: str, filename: str) -> list[str]:
    """Validate that dependency files exist and are readable."""
    validate_directory(directory)

    dependency_files = find_dependency_files(directory, filename)

    if not dependency_files:
        abs_directory = os.path.abspath(directory)
        raise DependencyFileNotFoundError(
            f"No '{filename}' files found in '{abs_directory}' or its subdirectories.\n\n"
            f"📂 Searched in: {abs_directory}\n"
            f"🔍 Looking for: {filename}\n"
            f"\n💡 To generate a Maven dependency file, run:"
            f"\n   mvn dependency:tree -DoutputFile={filename}"
            f"\n\n📍 Make sure you're in a directory with a pom.xml file."
        )

    # Validate that files are readable
    unreadable_files = []
    for file_path in dependency_files:
        if not os.access(file_path, os.R_OK):
            unreadable_files.append(file_path)

    if unreadable_files:
        files_list = "\n".join(f"  - {f}" for f in unreadable_files)
        raise DependencyFileNotFoundError(
            f"Found {len(dependency_files)} dependency file(s), but cannot read {len(unreadable_files)} of them:\n"
            f"{files_list}\n\n"
            f"Please check file permissions and try again."
        )

    return dependency_files


def validate_output_directory(output_file: str) -> None:
    """Validate that the output directory exists and is writable."""
    output_dir = Path(output_file).parent

    if not output_dir.exists():
        try:
            output_dir.mkdir(parents=True, exist_ok=True)
        except PermissionError:
            raise OutputGenerationError(f"Cannot create output directory '{output_dir}'.\nPlease check your permissions and try again.")
        except Exception as e:
            raise OutputGenerationError(f"Failed to create output directory '{output_dir}': {e}")

    if not os.access(output_dir, os.W_OK):
        raise OutputGenerationError(f"Cannot write to output directory '{output_dir}'.\nPlease check your permissions and try again.")
