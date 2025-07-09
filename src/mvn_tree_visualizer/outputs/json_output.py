import json
from typing import Any, Dict, List, Tuple


def create_json_output(dependency_tree: str, output_filename: str, show_versions: bool = False) -> None:
    lines: List[str] = dependency_tree.strip().split("\n")
    tree: Dict[str, Any] = {}
    node_stack: List[Tuple[Dict[str, Any], int]] = []  # Stack to keep track of nodes and their depth

    for line in lines:
        if not line:
            continue
        if line.startswith("[INFO] "):
            line = line[7:]  # Remove the "[INFO] " prefix

        parts: List[str] = line.split(":")
        if len(parts) < 3:
            continue

        # Root node
        if len(parts) == 4:
            group_id, artifact_id, _, version = parts
            if show_versions:
                node_id: str = f"{artifact_id}:{version}"
            else:
                node_id: str = artifact_id
            node: Dict[str, Any] = {"id": node_id, "children": []}
            tree = node
            node_stack = [(node, 0)]  # Reset stack with root node at depth 0
        # Child node
        else:
            # This depth calculation is based on the mermaid logic's whitespace parsing
            depth: int = len(parts[0].split(" ")) - 1

            if len(parts) == 6:
                _, artifact_id, _, _, version, _ = parts
            else:
                _, artifact_id, _, version, _ = parts

            if show_versions:
                node_id: str = f"{artifact_id}:{version}"
            else:
                node_id: str = artifact_id

            node: Dict[str, Any] = {"id": node_id, "children": []}

            # Go up the stack to find the correct parent
            while node_stack and node_stack[-1][1] >= depth:
                node_stack.pop()

            if node_stack:
                parent_node: Dict[str, Any]
                parent_node, _ = node_stack[-1]
                parent_node["children"].append(node)

            node_stack.append((node, depth))

    with open(output_filename, "w") as f:
        json.dump(tree, f, indent=4)
