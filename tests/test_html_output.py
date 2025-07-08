from mvn_tree_visualizer.outputs.html_output import _convert_to_mermaid


def test_convert_to_mermaid_simple():
    dependency_tree = r"""[INFO] com.example:my-app:jar:1.0.0
[INFO] +- org.springframework.boot:spring-boot-starter-web:jar:2.5.4:compile
[INFO] |  +- org.springframework.boot:spring-boot-starter:jar:2.5.4:compile
[INFO] |  |  \- org.yaml:snakeyaml:jar:1.28:compile
[INFO] |  \- org.springframework:spring-webmvc:jar:5.3.9:compile
[INFO] \- org.apache.commons:commons-lang3:jar:3.12.0:compile
"""
    expected_mermaid_diagram_lines = {
    "graph LR",
    "\tmy-app --> commons-lang3;",
    "\tmy-app --> spring-boot-starter-web;",
    "\tmy-app;",
    "\tspring-boot-starter --> snakeyaml;",
    "\tspring-boot-starter-web --> spring-boot-starter;",
    "\tspring-boot-starter-web --> spring-webmvc;",
    }

    actual_lines = set(_convert_to_mermaid(dependency_tree).strip().split('\n'))
    assert actual_lines == expected_mermaid_diagram_lines


def test_convert_to_mermaid_deeper_tree():
    dependency_tree = r"""[INFO] com.example:my-app:jar:1.0.0
[INFO] +- a:b:jar:1.0.0:compile
[INFO] |  +- c:d:jar:1.0.0:compile
[INFO] |  |  +- e:f:jar:1.0.0:compile
[INFO] |  |  |  \- g:h:jar:1.0.0:compile
[INFO] |  |  \- i:j:jar:1.0.0:compile
[INFO] |  \- k:l:jar:1.0.0:compile
[INFO] \- m:n:jar:1.0.0:compile
"""
    expected_mermaid_diagram_lines = {
        "graph LR",
        "\tb --> d;",
        "\tb --> l;",
        "\td --> f;",
        "\td --> j;",
        "\tf --> h;",
        "\tmy-app --> b;",
        "\tmy-app --> n;",
        "\tmy-app;",
    }

    actual_lines = set(_convert_to_mermaid(dependency_tree).strip().split('\n'))
    assert actual_lines == expected_mermaid_diagram_lines


def test_convert_to_mermaid_multiple_top_level():
    dependency_tree = r"""[INFO] com.example:my-app:jar:1.0.0
[INFO] +- a:b:jar:1.0.0:compile
[INFO] \- c:d:jar:1.0.0:compile
"""
    expected_mermaid_diagram_lines = {
        "graph LR",
        "\tmy-app --> b;",
        "\tmy-app --> d;",
        "\tmy-app;",
    }

    actual_lines = set(_convert_to_mermaid(dependency_tree).strip().split('\n'))
    assert actual_lines == expected_mermaid_diagram_lines


def test_convert_to_mermaid_duplicate_dependencies():
    dependency_tree = r"""[INFO] com.example:my-app:jar:1.0.0
[INFO] +- a:b:jar:1.0.0:compile
[INFO] |  \- c:d:jar:1.0.0:compile
[INFO] \- e:f:jar:1.0.0:compile
[INFO]    \- c:d:jar:1.0.0:compile
"""
    expected_mermaid_diagram_lines = {
        "graph LR",
        "\tb --> d;",
        "\tf --> d;",
        "\tmy-app --> b;",
        "\tmy-app --> f;",
        "\tmy-app;",
    }
    
    actual_lines = set(_convert_to_mermaid(dependency_tree).strip().split('\n'))
    assert actual_lines == expected_mermaid_diagram_lines
