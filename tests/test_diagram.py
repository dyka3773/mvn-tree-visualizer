from mvn_tree_visualizer.diagram import _convert_to_mermaid


def test_convert_to_mermaid_simple():
    dependency_tree = r"""[INFO] com.example:my-app:jar:1.0.0
[INFO] +- org.springframework.boot:spring-boot-starter-web:jar:2.5.4:compile
[INFO] |  +- org.springframework.boot:spring-boot-starter:jar:2.5.4:compile
[INFO] |  |  \- org.yaml:snakeyaml:jar:1.28:compile
[INFO] |  \- org.springframework:spring-webmvc:jar:5.3.9:compile
[INFO] \- org.apache.commons:commons-lang3:jar:3.12.0:compile
"""
    expected_mermaid_diagram = """graph LR
	my-app --> commons-lang3;
	my-app --> spring-boot-starter-web;
	my-app;
	spring-boot-starter --> snakeyaml;
	spring-boot-starter-web --> spring-boot-starter;
	spring-boot-starter-web --> spring-webmvc;"""

    assert _convert_to_mermaid(dependency_tree) == expected_mermaid_diagram


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
    expected_mermaid_diagram = """graph LR
	b --> d;
	b --> l;
	d --> f;
	d --> j;
	f --> h;
	my-app --> b;
	my-app --> n;
	my-app;"""

    assert _convert_to_mermaid(dependency_tree) == expected_mermaid_diagram


def test_convert_to_mermaid_multiple_top_level():
    dependency_tree = r"""[INFO] com.example:my-app:jar:1.0.0
[INFO] +- a:b:jar:1.0.0:compile
[INFO] \- c:d:jar:1.0.0:compile
"""
    expected_mermaid_diagram = """graph LR
	my-app --> b;
	my-app --> d;
	my-app;"""

    assert _convert_to_mermaid(dependency_tree) == expected_mermaid_diagram


def test_convert_to_mermaid_duplicate_dependencies():
    dependency_tree = r"""[INFO] com.example:my-app:jar:1.0.0
[INFO] +- a:b:jar:1.0.0:compile
[INFO] |  \- c:d:jar:1.0.0:compile
[INFO] \- e:f:jar:1.0.0:compile
[INFO]    \- c:d:jar:1.0.0:compile
"""
    expected_mermaid_diagram = """graph LR
	b --> d;
	f --> d;
	my-app --> b;
	my-app --> f;
	my-app;"""

    assert _convert_to_mermaid(dependency_tree) == expected_mermaid_diagram