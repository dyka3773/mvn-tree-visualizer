from mvn_tree_visualizer.outputs.html_output import _convert_to_mermaid


def test_convert_to_mermaid_simple():
    dependency_tree = r"""[INFO] com.example:my-app:jar:1.0.0
[INFO] +- org.springframework.boot:spring-boot-starter-web:jar:2.5.4:compile
[INFO] |  +- org.springframework.boot:spring-boot-starter:jar:2.5.4:compile
[INFO] |  |  \- org.yaml:snakeyaml:jar:1.28:compile
[INFO] |  \- org.springframework:spring-webmvc:jar:5.3.9:compile
[INFO] \- org.apache.commons:commons-lang3:jar:3.12.0:compile
"""

    actual_diagram = _convert_to_mermaid(dependency_tree)

    # Test that it's a valid Mermaid diagram
    assert actual_diagram.startswith("graph LR")

    # Test that key relationships are present (using sanitized node names)
    assert "my_app --> commons_lang3;" in actual_diagram
    assert "my_app --> spring_boot_starter_web;" in actual_diagram
    assert "spring_boot_starter_web --> spring_boot_starter;" in actual_diagram
    assert "spring_boot_starter_web --> spring_webmvc;" in actual_diagram
    assert "spring_boot_starter --> snakeyaml;" in actual_diagram

    # Test that styling classes are present
    assert "classDef rootNode" in actual_diagram
    assert "classDef leafNode" in actual_diagram
    assert "classDef intermediateNode" in actual_diagram

    # Test that node declarations are present
    assert 'my_app["my-app"]' in actual_diagram


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

    actual_diagram = _convert_to_mermaid(dependency_tree)

    # Test that it's a valid Mermaid diagram
    assert actual_diagram.startswith("graph LR")

    # Test key relationships are present
    assert "my_app --> b;" in actual_diagram
    assert "my_app --> n;" in actual_diagram
    assert "b --> d;" in actual_diagram
    assert "b --> l;" in actual_diagram
    assert "d --> f;" in actual_diagram
    assert "d --> j;" in actual_diagram
    assert "f --> h;" in actual_diagram

    # Test that all expected nodes are present
    assert 'my_app["my-app"]' in actual_diagram
    assert 'b["b"]' in actual_diagram
    assert 'd["d"]' in actual_diagram
    assert 'f["f"]' in actual_diagram
    assert 'h["h"]' in actual_diagram
    assert 'j["j"]' in actual_diagram
    assert 'l["l"]' in actual_diagram
    assert 'n["n"]' in actual_diagram


def test_convert_to_mermaid_multiple_top_level():
    dependency_tree = r"""[INFO] com.example:my-app:jar:1.0.0
[INFO] +- a:b:jar:1.0.0:compile
[INFO] \- c:d:jar:1.0.0:compile
"""

    actual_diagram = _convert_to_mermaid(dependency_tree)

    # Test that it's a valid Mermaid diagram
    assert actual_diagram.startswith("graph LR")

    # Test key relationships are present
    assert "my_app --> b;" in actual_diagram
    assert "my_app --> d;" in actual_diagram

    # Test that all expected nodes are present
    assert 'my_app["my-app"]' in actual_diagram
    assert 'b["b"]' in actual_diagram
    assert 'd["d"]' in actual_diagram


def test_convert_to_mermaid_duplicate_dependencies():
    dependency_tree = r"""[INFO] com.example:my-app:jar:1.0.0
[INFO] +- a:b:jar:1.0.0:compile
[INFO] |  \- c:d:jar:1.0.0:compile
[INFO] \- e:f:jar:1.0.0:compile
[INFO]    \- c:d:jar:1.0.0:compile
"""

    actual_diagram = _convert_to_mermaid(dependency_tree)

    # Test that it's a valid Mermaid diagram
    assert actual_diagram.startswith("graph LR")

    # Test key relationships are present, including duplicates
    assert "my_app --> b;" in actual_diagram
    assert "my_app --> f;" in actual_diagram
    assert "b --> d;" in actual_diagram
    assert "f --> d;" in actual_diagram

    # Test that all expected nodes are present
    assert 'my_app["my-app"]' in actual_diagram
    assert 'b["b"]' in actual_diagram
    assert 'f["f"]' in actual_diagram
    assert 'd["d"]' in actual_diagram


def test_convert_to_mermaid_with_show_versions():
    dependency_tree = r"""[INFO] com.example:my-app:jar:1.0.0
[INFO] +- org.springframework.boot:spring-boot-starter-web:jar:2.5.4:compile
[INFO] |  \- org.springframework.boot:spring-boot-starter:jar:2.5.4:compile
[INFO] \- org.apache.commons:commons-lang3:jar:3.12.0:compile
"""

    actual_diagram = _convert_to_mermaid(dependency_tree, show_versions=True)

    # Test that it's a valid Mermaid diagram
    assert actual_diagram.startswith("graph LR")

    # Test that version information is included in node labels
    assert '"my-app:1.0.0"' in actual_diagram
    assert '"spring-boot-starter-web:2.5.4"' in actual_diagram
    assert '"commons-lang3:3.12.0"' in actual_diagram

    # Test relationships with sanitized IDs
    assert "my_app_1_0_0 --> commons_lang3_3_12_0;" in actual_diagram
    assert "my_app_1_0_0 --> spring_boot_starter_web_2_5_4;" in actual_diagram


def test_convert_to_mermaid_with_show_versions_false():
    dependency_tree = r"""[INFO] com.example:my-app:jar:1.0.0
[INFO] +- org.springframework.boot:spring-boot-starter-web:jar:2.5.4:compile
[INFO] |  \- org.springframework.boot:spring-boot-starter:jar:2.5.4:compile
[INFO] \- org.apache.commons:commons-lang3:jar:3.12.0:compile
"""

    actual_diagram = _convert_to_mermaid(dependency_tree, show_versions=False)

    # Test that it's a valid Mermaid diagram
    assert actual_diagram.startswith("graph LR")

    # Test that versions are NOT in node labels
    assert '"my-app"' in actual_diagram
    assert '"spring-boot-starter-web"' in actual_diagram
    assert '"commons-lang3"' in actual_diagram

    # Test relationships without version info
    assert "my_app --> commons_lang3;" in actual_diagram
    assert "my_app --> spring_boot_starter_web;" in actual_diagram


def test_convert_to_mermaid_real_life_example():
    dependency_tree = r"""[INFO] [dependency:tree]
[INFO] org.apache.maven.plugins:maven-dependency-plugin:maven-plugin:2.0-alpha-5-SNAPSHOT
[INFO] \- org.apache.maven.doxia:doxia-site-renderer:jar:1.0-alpha-8:compile
[INFO]    \- org.codehaus.plexus:plexus-velocity:jar:1.1.3:compile
[INFO]       \- velocity:velocity:jar:1.4:compile
"""

    actual_diagram = _convert_to_mermaid(dependency_tree)

    # Test that it's a valid Mermaid diagram
    assert actual_diagram.startswith("graph LR")

    # Test key relationships are present
    assert "maven_dependency_plugin --> doxia_site_renderer;" in actual_diagram
    assert "doxia_site_renderer --> plexus_velocity;" in actual_diagram
    assert "plexus_velocity --> velocity;" in actual_diagram


def test_convert_to_mermaid_real_life_example_show_versions():
    dependency_tree = r"""[INFO] [dependency:tree]
[INFO] org.apache.maven.plugins:maven-dependency-plugin:maven-plugin:2.0-alpha-5-SNAPSHOT
[INFO] \- org.apache.maven.doxia:doxia-site-renderer:jar:1.0-alpha-8:compile
[INFO]    \- org.codehaus.plexus:plexus-velocity:jar:1.1.3:compile
[INFO]       \- velocity:velocity:jar:1.4:compile
"""

    actual_diagram = _convert_to_mermaid(dependency_tree, show_versions=True)

    # Test that it's a valid Mermaid diagram
    assert actual_diagram.startswith("graph LR")

    # Test that version information is included
    assert '"maven-dependency-plugin:2.0-alpha-5-SNAPSHOT"' in actual_diagram
    assert '"doxia-site-renderer:1.0-alpha-8"' in actual_diagram
    assert '"plexus-velocity:1.1.3"' in actual_diagram
    assert '"velocity:1.4"' in actual_diagram

    # Test relationships with sanitized IDs
    assert "maven_dependency_plugin_2_0_alpha_5_SNAPSHOT --> doxia_site_renderer_1_0_alpha_8;" in actual_diagram
