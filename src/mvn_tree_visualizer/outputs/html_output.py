from pathlib import Path
from typing import List, Tuple, Set
from jinja2 import BaseLoader, Environment
from ..TEMPLATE import HTML_TEMPLATE


def create_html_diagram(dependency_tree: str, output_filename: str) -> None:
    mermaid_diagram: str = _convert_to_mermaid(dependency_tree)
    template = Environment(loader=BaseLoader).from_string(HTML_TEMPLATE)
    rendered: str = template.render(diagram_definition=mermaid_diagram)
    parent_dir: Path = Path(output_filename).parent
    if not parent_dir.exists():
        parent_dir.mkdir(parents=True, exist_ok=True)
    with open(output_filename, "w") as f:
        f.write(rendered)


def _convert_to_mermaid(dependency_tree: str) -> str:
    # generate a `graph LR` format for Mermaid
    lines: List[str] = dependency_tree.strip().split("\n")
    mermaid_lines: Set[str] = set()
    previous_dependency: List[Tuple[str, int]] = []
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
            mermaid_lines.add(f"\t{artifact_id};")
            if previous_dependency:  # Re initialize the list if it wasn't empty
                previous_dependency = []
            previous_dependency.append((artifact_id, 0))  # The second element is the depth
        else:
            depth: int = len(parts[0].split(" ")) - 1
            if len(parts) == 6:
                dirty_group_id, artifact_id, app, ejb_client, version, dependency = parts
            else:
                dirty_group_id, artifact_id, app, version, dependency = parts
            if previous_dependency[-1][1] < depth:
                mermaid_lines.add(f"\t{previous_dependency[-1][0]} --> {artifact_id};")
                previous_dependency.append((artifact_id, depth))
            else:
                # remove all dependencies that are deeper or equal to the current depth
                while previous_dependency and previous_dependency[-1][1] >= depth:
                    previous_dependency.pop()
                mermaid_lines.add(f"\t{previous_dependency[-1][0]} --> {artifact_id};")
                previous_dependency.append((artifact_id, depth))
    return "graph LR\n" + "\n".join(mermaid_lines)
