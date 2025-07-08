import os


def create_diagram(
    keep_tree: bool = False,
    intermediate_filename: str = "dependency_tree.txt",
) -> str:
    with open(intermediate_filename, "r") as file:
        dependency_tree: str = file.read()

    if not keep_tree:
        os.remove(intermediate_filename)

    return dependency_tree
