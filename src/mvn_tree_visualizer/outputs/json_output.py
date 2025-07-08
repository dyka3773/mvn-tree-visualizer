import json

def create_json_output(dependency_tree: str, output_filename: str):
    lines = dependency_tree.strip().split("\n")
    tree = {}
    node_stack = []  # Stack to keep track of nodes and their depth

    for line in lines:
        if not line:
            continue
        if line.startswith("[INFO] "):
            line = line[7:]  # Remove the "[INFO] " prefix

        parts = line.split(":")
        if len(parts) < 3:
            continue

        # Root node
        if len(parts) == 4:
            group_id, artifact_id, _, version = parts
            node = {"id": f"{group_id}:{artifact_id}:{version}", "children": []}
            tree = node
            node_stack = [(node, 0)]  # Reset stack with root node at depth 0
        # Child node
        else:
            # This depth calculation is based on the mermaid logic's whitespace parsing
            depth = len(parts[0].split(" ")) - 1

            if len(parts) == 6:
                _, artifact_id, _, _, version, _ = parts
            else:
                _, artifact_id, _, version, _ = parts

            node = {"id": f"{artifact_id}:{version}", "children": []}

            # Go up the stack to find the correct parent
            while node_stack and node_stack[-1][1] >= depth:
                node_stack.pop()

            if node_stack:
                parent_node, _ = node_stack[-1]
                parent_node["children"].append(node)

            node_stack.append((node, depth))

    with open(output_filename, "w") as f:
        json.dump(tree, f, indent=4)
