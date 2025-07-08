def create_diagram(
    keep_tree: bool = False,
    intermediate_filename: str = "dependency_tree.txt",
):
    with open(intermediate_filename, "r") as file:
        dependency_tree = file.read()

    if not keep_tree:
        import os

        os.remove(intermediate_filename)
    
    return dependency_tree
