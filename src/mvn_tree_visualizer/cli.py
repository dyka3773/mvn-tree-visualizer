import argparse
import time
from pathlib import Path
from typing import NoReturn

from .diagram import create_diagram
from .exceptions import DependencyFileNotFoundError, DependencyParsingError, MvnTreeVisualizerError, OutputGenerationError
from .file_watcher import FileWatcher
from .get_dependencies_in_one_file import merge_files
from .outputs.html_output import create_html_diagram
from .outputs.json_output import create_json_output
from .validation import find_dependency_files, print_maven_help, validate_dependency_files, validate_output_directory


def generate_diagram(
    directory: str,
    output_file: str,
    filename: str,
    keep_tree: bool,
    output_format: str,
    show_versions: bool,
) -> None:
    """Generate the dependency diagram with comprehensive error handling."""
    timestamp = time.strftime("%H:%M:%S")

    try:
        # Validate inputs
        validate_dependency_files(directory, filename)
        validate_output_directory(output_file)

        # Show what files we found
        dependency_files = find_dependency_files(directory, filename)
        if len(dependency_files) > 1:
            print(f"[{timestamp}] Found {len(dependency_files)} dependency files")

        # Setup paths
        dir_to_create_files = Path(output_file).parent
        dir_to_create_intermediate_files = Path(dir_to_create_files)
        intermediate_file_path: Path = dir_to_create_intermediate_files / "dependency_tree.txt"

        # Merge dependency files
        try:
            merge_files(
                output_file=intermediate_file_path,
                root_dir=directory,
                target_filename=filename,
            )
        except FileNotFoundError as e:
            raise DependencyParsingError(f"Error reading dependency file: {e}\nThe file may have been moved or deleted during processing.")
        except PermissionError as e:
            raise DependencyParsingError(f"Permission denied while reading dependency files: {e}\nPlease check file permissions and try again.")
        except UnicodeDecodeError as e:
            raise DependencyParsingError(
                f"Error decoding dependency file content: {e}\n"
                f"The file may contain invalid characters or use an unsupported encoding.\n"
                f"Please ensure the file is in UTF-8 format."
            )

        # Validate merged content
        if not intermediate_file_path.exists() or intermediate_file_path.stat().st_size == 0:
            raise DependencyParsingError(
                "Generated dependency tree file is empty.\n"
                "This usually means the Maven dependency files contain no valid dependency information.\n"
                "Please check that your Maven dependency files were generated correctly."
            )

        # Create diagram from merged content
        try:
            dependency_tree = create_diagram(
                keep_tree=keep_tree,
                intermediate_filename=str(intermediate_file_path),
            )
        except FileNotFoundError:
            raise DependencyParsingError("Intermediate dependency tree file was not found.\nThis is an internal error - please report this issue.")
        except Exception as e:
            raise DependencyParsingError(f"Error processing dependency tree: {e}\nThe dependency file format may be invalid or corrupted.")

        # Validate that we have content to work with
        if not dependency_tree.strip():
            raise DependencyParsingError(
                "Dependency tree is empty after processing.\n"
                "Please check that your Maven dependency files contain valid dependency information.\n"
                "You can verify this by opening the files and checking their content."
            )

        # Generate output
        try:
            if output_format == "html":
                create_html_diagram(dependency_tree, output_file, show_versions)
            elif output_format == "json":
                create_json_output(dependency_tree, output_file, show_versions)
            else:
                raise OutputGenerationError(f"Unsupported output format: {output_format}")
        except PermissionError:
            raise OutputGenerationError(
                f"Permission denied writing to '{output_file}'.\nPlease check that you have write permissions to this location."
            )
        except OSError as e:
            raise OutputGenerationError(
                f"Error writing output file '{output_file}': {e}\nPlease check that you have enough disk space and write permissions."
            )
        except Exception as e:
            raise OutputGenerationError(f"Error generating {output_format.upper()} output: {e}")

        print(f"[{timestamp}] ✅ Diagram generated and saved to {output_file}")

    except MvnTreeVisualizerError as e:
        # Our custom errors already have helpful messages
        print(f"[{timestamp}] ❌ Error: {e}")
        if isinstance(e, DependencyFileNotFoundError):
            print_maven_help()
    except KeyboardInterrupt:
        print(f"\n[{timestamp}] ⏹️  Operation cancelled by user")
    except Exception as e:
        # Unexpected errors
        print(f"[{timestamp}] ❌ Unexpected error: {e}")
        print("This is an internal error. Please report this issue with the following details:")
        print(f"  - Directory: {directory}")
        print(f"  - Filename: {filename}")
        print(f"  - Output: {output_file}")
        print(f"  - Format: {output_format}")
        import traceback

        traceback.print_exc()


def cli() -> NoReturn:
    parser = argparse.ArgumentParser(
        prog="mvn-tree-visualizer",
        description="Generate a dependency diagram from a file.",
    )
    parser.add_argument(
        "directory",
        type=str,
        nargs="?",
        default=".",
        help="The directory to scan for the Maven dependency file(s). Default is the current directory.",
    )

    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="diagram.html",
        help="The output file for the generated diagram. Default is 'diagram.html'.",
    )

    parser.add_argument(
        "--format",
        type=str,
        default="html",
        choices=["html", "json"],
        help="The output format. Default is 'html'.",
    )

    parser.add_argument(
        "-f",
        "--filename",
        type=str,
        default="maven_dependency_file",
        help="The name of the file to read the Maven dependencies from. Default is 'maven_dependency_file'.",
    )
    parser.add_argument(
        "--keep-tree",
        type=bool,
        default=False,
        help="Keep the dependency tree file after generating the diagram. Default is False.",
    )

    parser.add_argument(
        "--show-versions",
        action="store_true",
        help="Show dependency versions in the diagram. Applicable to both HTML and JSON output formats.",
    )

    parser.add_argument(
        "--watch",
        action="store_true",
        help="Watch for changes in Maven dependency files and automatically regenerate the diagram.",
    )

    args = parser.parse_args()
    directory: str = args.directory
    output_file: str = args.output
    filename: str = args.filename
    keep_tree: bool = args.keep_tree
    output_format: str = args.format
    show_versions: bool = args.show_versions
    watch_mode: bool = args.watch

    # Generate initial diagram
    print("Generating initial diagram...")
    generate_diagram(directory, output_file, filename, keep_tree, output_format, show_versions)

    if not watch_mode:
        print("You can open it in your browser to view the dependency tree.")
        print("Thank you for using mvn-tree-visualizer!")
        return

    # Watch mode
    def regenerate_callback():
        """Callback function for file watcher."""
        generate_diagram(directory, output_file, filename, keep_tree, output_format, show_versions)

    watcher = FileWatcher(directory, filename, regenerate_callback)
    watcher.start()

    try:
        watcher.wait()
    finally:
        print("Thank you for using mvn-tree-visualizer!")


if __name__ == "__main__":
    cli()
