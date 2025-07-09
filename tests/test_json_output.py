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
        "id": "my-app",
        "children": [
            {"id": "spring-boot-starter-web", "children": [{"id": "spring-boot-starter", "children": []}]},
            {"id": "commons-lang3", "children": []},
        ],
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
        "id": "my-app",
        "children": [
            {
                "id": "b",
                "children": [
                    {
                        "id": "d",
                        "children": [{"id": "f", "children": [{"id": "h", "children": []}]}, {"id": "j", "children": []}],
                    },
                    {"id": "l", "children": []},
                ],
            },
            {"id": "n", "children": []},
        ],
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
        "id": "my-app",
        "children": [
            {"id": "b", "children": [{"id": "d", "children": []}]},
            {"id": "f", "children": [{"id": "d", "children": []}]},
        ],
    }

    output_filename = "test_output_duplicates.json"
    create_json_output(dependency_tree, output_filename)

    with open(output_filename, "r") as f:
        actual_json = json.load(f)

    os.remove(output_filename)
    assert actual_json == expected_json


def test_create_json_output_with_show_versions_true():
    dependency_tree = r"""[INFO] com.example:my-app:jar:1.0.0
[INFO] +- org.springframework.boot:spring-boot-starter-web:jar:2.5.4:compile
[INFO] |  \- org.springframework.boot:spring-boot-starter:jar:2.5.4:compile
[INFO] \- org.apache.commons:commons-lang3:jar:3.12.0:compile
"""
    expected_json = {
        "id": "my-app:1.0.0",
        "children": [
            {"id": "spring-boot-starter-web:2.5.4", "children": [{"id": "spring-boot-starter:2.5.4", "children": []}]},
            {"id": "commons-lang3:3.12.0", "children": []},
        ],
    }

    output_filename = "test_output_show_versions_true.json"
    create_json_output(dependency_tree, output_filename, show_versions=True)

    with open(output_filename, "r") as f:
        actual_json = json.load(f)

    os.remove(output_filename)
    assert actual_json == expected_json


def test_create_json_output_with_show_versions_false():
    dependency_tree = r"""[INFO] com.example:my-app:jar:1.0.0
[INFO] +- org.springframework.boot:spring-boot-starter-web:jar:2.5.4:compile
[INFO] |  \- org.springframework.boot:spring-boot-starter:jar:2.5.4:compile
[INFO] \- org.apache.commons:commons-lang3:jar:3.12.0:compile
"""
    expected_json = {
        "id": "my-app",
        "children": [
            {"id": "spring-boot-starter-web", "children": [{"id": "spring-boot-starter", "children": []}]},
            {"id": "commons-lang3", "children": []},
        ],
    }

    output_filename = "test_output_show_versions_false.json"
    create_json_output(dependency_tree, output_filename, show_versions=False)

    with open(output_filename, "r") as f:
        actual_json = json.load(f)

    os.remove(output_filename)
    assert actual_json == expected_json


def test_create_json_output_real_life_example():
    dependency_tree = r"""[INFO] [dependency:tree]
[INFO] org.apache.maven.plugins:maven-dependency-plugin:maven-plugin:2.0-alpha-5-SNAPSHOT
[INFO] \- org.apache.maven.doxia:doxia-site-renderer:jar:1.0-alpha-8:compile
[INFO]    \- org.codehaus.plexus:plexus-velocity:jar:1.1.3:compile
[INFO]       \- velocity:velocity:jar:1.4:compile
"""
    expected_json = {
        "id": "maven-dependency-plugin",
        "children": [
            {
                "id": "doxia-site-renderer",
                "children": [{"id": "plexus-velocity", "children": [{"id": "velocity", "children": []}]}],
            }
        ],
    }

    output_filename = "test_output_real_life.json"
    create_json_output(dependency_tree, output_filename)

    with open(output_filename, "r") as f:
        actual_json = json.load(f)

    os.remove(output_filename)
    assert actual_json == expected_json


def test_create_json_output_real_life_example_show_versions():
    dependency_tree = r"""[INFO] [dependency:tree]
[INFO] org.apache.maven.plugins:maven-dependency-plugin:maven-plugin:2.0-alpha-5-SNAPSHOT
[INFO] \- org.apache.maven.doxia:doxia-site-renderer:jar:1.0-alpha-8:compile
[INFO]    \- org.codehaus.plexus:plexus-velocity:jar:1.1.3:compile
[INFO]       \- velocity:velocity:jar:1.4:compile
"""
    expected_json = {
        "id": "maven-dependency-plugin:2.0-alpha-5-SNAPSHOT",
        "children": [
            {
                "id": "doxia-site-renderer:1.0-alpha-8",
                "children": [{"id": "plexus-velocity:1.1.3", "children": [{"id": "velocity:1.4", "children": []}]}],
            }
        ],
    }

    output_filename = "test_output_real_life_show_versions.json"
    create_json_output(dependency_tree, output_filename, show_versions=True)

    with open(output_filename, "r") as f:
        actual_json = json.load(f)

    os.remove(output_filename)
    assert actual_json == expected_json
