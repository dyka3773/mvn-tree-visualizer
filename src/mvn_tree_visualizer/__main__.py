import argparse
from pathlib import Path

from .diagram import create_diagram
from .get_dependencies_in_one_file import merge_files


def main():
    pass


if __name__ == "__main__":
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

    args = parser.parse_args()
    directory: str = args.directory
    output_file: str = args.output
    filename: str = args.filename
    keep_tree: bool = args.keep_tree

    dir_to_create_files = Path(output_file).parent

    dir_to_create_intermediate_files = Path(dir_to_create_files)

    merge_files(
        output_file=dir_to_create_intermediate_files / "dependency_tree.txt",
        root_dir=directory,
        target_filename=filename,
    )

    create_diagram(
        keep_tree=keep_tree,
        intermediate_filename="dependency_tree.txt",
        output_filename=output_file,
    )

    print(f"Diagram generated and saved to {output_file}")
    print("You can open it in your browser to view the dependency tree.")
    print("Thank you for using mvn-tree-visualizer!")
