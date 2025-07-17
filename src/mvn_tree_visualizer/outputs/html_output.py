from pathlib import Path
from typing import List, Set, Tuple

from jinja2 import BaseLoader, Environment

from ..enhanced_template import get_html_template
from ..themes import STANDARD_COLORS, get_theme


def create_html_diagram(dependency_tree: str, output_filename: str, show_versions: bool = False, theme: str = "minimal") -> None:
    """Create HTML diagram with theme support."""
    theme_obj = get_theme(theme)
    mermaid_diagram: str = _convert_to_mermaid(dependency_tree, show_versions)

    # Use enhanced template with theme
    html_template = get_html_template(theme_obj)
    template = Environment(loader=BaseLoader).from_string(html_template)
    rendered: str = template.render(diagram_definition=mermaid_diagram)

    parent_dir: Path = Path(output_filename).parent
    if not parent_dir.exists():
        parent_dir.mkdir(parents=True, exist_ok=True)
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(rendered)


def _convert_to_mermaid(dependency_tree: str, show_versions: bool = False) -> str:
    """Convert dependency tree to enhanced Mermaid diagram with styling."""
    lines: List[str] = dependency_tree.strip().split("\n")
    relationships: Set[str] = set()
    node_styles: Set[str] = set()
    previous_dependency: List[Tuple[str, int]] = []

    # Track root and leaf nodes for styling, and store all node declarations
    all_nodes: Set[str] = set()
    parent_nodes: Set[str] = set()
    child_nodes: Set[str] = set()
    node_declarations: Set[str] = set()

    for line in lines:
        if not line:
            continue
        if line.startswith("[INFO] "):
            line = line[7:]  # Remove the "[INFO] " prefix
        parts: List[str] = line.split(":")
        if len(parts) < 3:
            continue

        if len(parts) == 4:
            group_id, artifact_id, app, version = parts
            if show_versions:
                node_label: str = f"{artifact_id}:{version}"
                safe_node_id: str = _sanitize_node_id(f"{artifact_id}_{version}")
            else:
                node_label: str = artifact_id
                safe_node_id: str = _sanitize_node_id(artifact_id)

            node_declarations.add(f'\t{safe_node_id}["{node_label}"];')
            all_nodes.add(safe_node_id)
            if previous_dependency:  # Re initialize the list if it wasn't empty
                previous_dependency = []
            previous_dependency.append((safe_node_id, 0))  # The second element is the depth
        else:
            depth: int = len(parts[0].split(" ")) - 1
            if len(parts) == 6:
                dirty_group_id, artifact_id, app, ejb_client, version, dependency = parts
            else:
                dirty_group_id, artifact_id, app, version, dependency = parts

            if show_versions:
                node_label: str = f"{artifact_id}:{version}"
                safe_node_id: str = _sanitize_node_id(f"{artifact_id}_{version}")
            else:
                node_label: str = artifact_id
                safe_node_id: str = _sanitize_node_id(artifact_id)

            node_declarations.add(f'\t{safe_node_id}["{node_label}"];')
            all_nodes.add(safe_node_id)
            child_nodes.add(safe_node_id)

            if previous_dependency[-1][1] < depth:
                parent_id = previous_dependency[-1][0]
                parent_nodes.add(parent_id)
                relationships.add(f"\t{parent_id} --> {safe_node_id};")
                previous_dependency.append((safe_node_id, depth))
            else:
                # remove all dependencies that are deeper or equal to the current depth
                while previous_dependency and previous_dependency[-1][1] >= depth:
                    previous_dependency.pop()
                parent_id = previous_dependency[-1][0]
                parent_nodes.add(parent_id)
                relationships.add(f"\t{parent_id} --> {safe_node_id};")
                previous_dependency.append((safe_node_id, depth))

    # Add styling classes
    root_nodes = all_nodes - child_nodes
    leaf_nodes = all_nodes - parent_nodes

    # Add node styling
    for node in root_nodes:
        node_styles.add(f"\tclass {node} rootNode;")
    for node in leaf_nodes:
        node_styles.add(f"\tclass {node} leafNode;")
    for node in parent_nodes.intersection(child_nodes):
        node_styles.add(f"\tclass {node} intermediateNode;")

    # Build the complete diagram with standardized colors
    diagram_parts = [
        "graph LR",
        *sorted(node_declarations),
        *sorted(relationships),
        "",
        f"classDef rootNode fill:{STANDARD_COLORS['root_node']}20,stroke:{STANDARD_COLORS['root_node']},stroke-width:3px,color:#000;",
        f"classDef leafNode fill:{STANDARD_COLORS['leaf_node']}20,stroke:{STANDARD_COLORS['leaf_node']},stroke-width:2px,color:#000;",
        f"classDef intermediateNode fill:{STANDARD_COLORS['intermediate_node']}20,stroke:{STANDARD_COLORS['intermediate_node']},stroke-width:2px,color:#000;",
        "",
        *sorted(node_styles),
    ]

    return "\n".join(diagram_parts)


def _sanitize_node_id(node_id: str) -> str:
    """Sanitize node ID for Mermaid compatibility."""
    # Replace special characters that could break Mermaid syntax
    import re

    sanitized = re.sub(r"[^a-zA-Z0-9_]", "_", node_id)
    # Ensure it starts with a letter or underscore
    if sanitized and not sanitized[0].isalpha() and sanitized[0] != "_":
        sanitized = "_" + sanitized
    return sanitized or "node"
