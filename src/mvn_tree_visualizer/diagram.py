import os


def create_diagram(
    keep_tree: bool = False,
    intermediate_filename: str = "dependency_tree.txt",
) -> str:
    """Create diagram from dependency tree file."""
    try:
        with open(intermediate_filename, "r", encoding="utf-8") as file:
            dependency_tree: str = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Dependency tree file '{intermediate_filename}' not found")
    except PermissionError:
        raise PermissionError(f"Permission denied reading '{intermediate_filename}'")
    except UnicodeDecodeError as e:
        raise UnicodeDecodeError(e.encoding, e.object, e.start, e.end, f"Error decoding '{intermediate_filename}': {e.reason}")

    if not keep_tree:
        try:
            os.remove(intermediate_filename)
        except OSError:
            # If we can't remove the intermediate file, it's not critical
            pass

    return dependency_tree
