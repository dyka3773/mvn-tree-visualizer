import json
import os
from mvn_tree_visualizer.outputs.json_output import create_json_output

def test_create_json_output_simple():
    dependency_tree = r"""[INFO] com.example:my-app:jar:1.0.0
[INFO] +- org.springframework.boot:spring-boot-starter-web:jar:2.5.4:compile
[INFO] |  \- org.springframework.boot:spring-boot-starter:jar:2.5.4:compile
[INFO] \- org.apache.commons:commons-lang3:jar:3.12.0:compile
"""
    expected_json = {
        "id": "com.example:my-app:1.0.0",
        "children": [
            {
                "id": "spring-boot-starter-web:2.5.4",
                "children": [
                    {
                        "id": "spring-boot-starter:2.5.4",
                        "children": []
                    }
                ]
            },
            {
                "id": "commons-lang3:3.12.0",
                "children": []
            }
        ]
    }

    output_filename = "test_output.json"
    create_json_output(dependency_tree, output_filename)

    with open(output_filename, "r") as f:
        actual_json = json.load(f)

    os.remove(output_filename)
    assert actual_json == expected_json

def test_create_json_output_deeper_tree():
    dependency_tree = r"""[INFO] com.example:my-app:jar:1.0.0
[INFO] +- a:b:jar:1.0.0:compile
[INFO] |  +- c:d:jar:1.0.0:compile
[INFO] |  |  +- e:f:jar:1.0.0:compile
[INFO] |  |  |  \- g:h:jar:1.0.0:compile
[INFO] |  |  \- i:j:jar:1.0.0:compile
[INFO] |  \- k:l:jar:1.0.0:compile
[INFO] \- m:n:jar:1.0.0:compile
"""
    expected_json = {
        "id": "com.example:my-app:1.0.0",
        "children": [
            {
                "id": "b:1.0.0",
                "children": [
                    {
                        "id": "d:1.0.0",
                        "children": [
                            {"id": "f:1.0.0", "children": [{"id": "h:1.0.0", "children": []}]},
                            {"id": "j:1.0.0", "children": []}
                        ]
                    },
                    {"id": "l:1.0.0", "children": []}
                ]
            },
            {"id": "n:1.0.0", "children": []}
        ]
    }

    output_filename = "test_output_deep.json"
    create_json_output(dependency_tree, output_filename)

    with open(output_filename, "r") as f:
        actual_json = json.load(f)

    os.remove(output_filename)
    assert actual_json == expected_json

def test_create_json_output_duplicate_dependencies():
    dependency_tree = r"""[INFO] com.example:my-app:jar:1.0.0
[INFO] +- a:b:jar:1.0.0:compile
[INFO] |  \- c:d:jar:1.0.0:compile
[INFO] \- e:f:jar:1.0.0:compile
[INFO]    \- c:d:jar:1.0.0:compile
"""
    expected_json = {
        "id": "com.example:my-app:1.0.0",
        "children": [
            {"id": "b:1.0.0", "children": [{"id": "d:1.0.0", "children": []}]},
            {"id": "f:1.0.0", "children": [{"id": "d:1.0.0", "children": []}]}
        ]
    }

    output_filename = "test_output_duplicates.json"
    create_json_output(dependency_tree, output_filename)

    with open(output_filename, "r") as f:
        actual_json = json.load(f)

    os.remove(output_filename)
    assert actual_json == expected_json