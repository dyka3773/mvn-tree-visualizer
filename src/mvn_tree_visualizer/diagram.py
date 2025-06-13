from pathlib import Path

from jinja2 import BaseLoader, Environment

from .TEMPLATE import HTML_TEMPLATE


def _convert_to_mermaid(dependency_tree: str) -> str:
    # generate a `graph LR` format for Mermaid
    lines = dependency_tree.strip().split("\n")
    mermaid_lines = set()

    previous_dependency = []

    for line in lines:
        if not line or line.startswith("[INFO]"):
            continue
        parts = line.split(":")

        if len(parts) < 3:
            continue

        if len(parts) == 4:
            group_id, artifact_id, app, version = parts
            mermaid_lines.add(f"\t{artifact_id};")

            if previous_dependency:  # Re initialize the list if it wasn't empty
                previous_dependency = []

            previous_dependency.append((artifact_id, 0))  # The second element is the depth
        else:
            depth = len(parts[0].split(" ")) - 1

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

    mermaid_diagram = f"graph LR\n{'\n'.join(sorted(mermaid_lines))}"
    return mermaid_diagram


def create_diagram(keep_tree: bool = False, intermediate_filename: str = "dependency_tree.txt", output_filename: str = "diagram.html"):
    with open(intermediate_filename, "r") as file:
        dependency_tree = file.read()

    mermaid_diagram = _convert_to_mermaid(dependency_tree)

    template = Environment(loader=BaseLoader).from_string(HTML_TEMPLATE)
    rendered = template.render(diagram_definition=mermaid_diagram)

    parent_dir = Path(output_filename).parent

    if not parent_dir.exists():
        parent_dir.mkdir(parents=True, exist_ok=True)

    with open(output_filename, "w") as f:
        f.write(rendered)

    if not keep_tree:
        import os

        os.remove(intermediate_filename)
