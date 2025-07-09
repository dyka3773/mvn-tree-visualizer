import argparse
import time
from pathlib import Path
from typing import NoReturn

from .diagram import create_diagram
from .file_watcher import FileWatcher
from .get_dependencies_in_one_file import merge_files
from .outputs.html_output import create_html_diagram
from .outputs.json_output import create_json_output


def generate_diagram(
    directory: str,
    output_file: str,
    filename: str,
    keep_tree: bool,
    output_format: str,
    show_versions: bool,
) -> None:
    """Generate the dependency diagram."""
    dir_to_create_files = Path(output_file).parent
    dir_to_create_intermediate_files = Path(dir_to_create_files)

    try:
        intermediate_file_path: Path = dir_to_create_intermediate_files / "dependency_tree.txt"
        merge_files(
            output_file=intermediate_file_path,
            root_dir=directory,
            target_filename=filename,
        )

        dependency_tree = create_diagram(
            keep_tree=keep_tree,
            intermediate_filename=str(intermediate_file_path),
        )

        if output_format == "html":
            create_html_diagram(dependency_tree, output_file, show_versions)
        elif output_format == "json":
            create_json_output(dependency_tree, output_file, show_versions)

        timestamp = time.strftime("%H:%M:%S")
        print(f"[{timestamp}] Diagram generated and saved to {output_file}")

    except Exception as e:
        timestamp = time.strftime("%H:%M:%S")
        print(f"[{timestamp}] Error generating diagram: {e}")


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
