"""Integration tests for the GitHub issue #7 - Maximum Text Size for diagram (mermaid error)."""

from mvn_tree_visualizer.enhanced_template import _dict_to_js_object, get_html_template
from mvn_tree_visualizer.themes import MAX_EDGES_LARGE_PROJECTS, MAX_TEXT_SIZE_LARGE_PROJECTS, get_theme


class TestGitHubIssue7Fix:
    """Test suite specifically for GitHub issue #7 - Large dependency tree handling."""

    def test_massive_dependency_tree_config(self):
        """Test that configuration can handle massive dependency trees like reported in issue #7."""
        # Test both themes mentioned in the issue
        for theme_name in ["minimal", "dark"]:
            theme = get_theme(theme_name)

            # Verify the exact values mentioned in the issue screenshot
            assert theme.mermaid_config["maxTextSize"] == MAX_TEXT_SIZE_LARGE_PROJECTS
            assert theme.mermaid_config["maxEdges"] == MAX_EDGES_LARGE_PROJECTS

            # Check that the configuration is properly converted to JavaScript
            mermaid_config_js = _dict_to_js_object(theme.mermaid_config)
            assert f'"maxTextSize": {MAX_TEXT_SIZE_LARGE_PROJECTS}' in mermaid_config_js
            assert f'"maxEdges": {MAX_EDGES_LARGE_PROJECTS}' in mermaid_config_js

    def test_zoom_improvements_for_large_diagrams(self):
        """Test that zoom improvements address the 'can't zoom in enough' issue mentioned."""
        theme = get_theme("minimal")
        html = get_html_template(theme)

        # Verify much higher max zoom for detailed inspection
        assert "maxZoom: MAX_ZOOM" in html  # Using constant instead of hardcoded value

        # Verify much lower min zoom for overview of large diagrams
        assert "minZoom: MIN_ZOOM" in html  # Using constant instead of hardcoded value

        # Verify smoother zoom increments for better navigation
        assert "zoomScaleSensitivity: ZOOM_SCALE_SENSITIVITY" in html

    def test_navigation_controls_for_large_diagrams(self):
        """Test that navigation controls help with large diagrams (search functionality removed)."""
        theme = get_theme("minimal")
        html = get_html_template(theme)

        # Verify core navigation buttons are present
        navigation_buttons = ["zoomInButton", "zoomOutButton", "resetZoomButton"]

        for button in navigation_buttons:
            assert f'id="{button}"' in html

        # Verify search button is removed
        assert 'id="findNode"' not in html

    def test_mermaid_error_prevention_config(self):
        """Test that the configuration prevents the original Mermaid errors."""
        for theme_name in ["minimal", "dark"]:
            theme = get_theme(theme_name)
            config = theme.mermaid_config

            # Test that maxTextSize is large enough to prevent text overflow errors
            # The original error occurred with default limits
            assert config["maxTextSize"] >= MAX_TEXT_SIZE_LARGE_PROJECTS

            # Test that maxEdges is large enough for complex dependency trees
            assert config["maxEdges"] >= MAX_EDGES_LARGE_PROJECTS

            # Verify these are integers (not strings) to prevent type errors
            assert isinstance(config["maxTextSize"], int)
            assert isinstance(config["maxEdges"], int)

    def test_backward_compatibility_maintained(self):
        """Test that the fix doesn't break existing functionality."""
        theme = get_theme("minimal")

        # Verify existing theme configuration is maintained
        assert "theme" in theme.mermaid_config
        assert "themeVariables" in theme.mermaid_config

        # Verify standard colors are still applied
        theme_vars = theme.mermaid_config["themeVariables"]
        assert "primaryColor" in theme_vars
        assert "primaryTextColor" in theme_vars
        assert "lineColor" in theme_vars

    def test_javascript_config_generation(self):
        """Test that the enhanced configuration is properly converted to JavaScript."""
        theme = get_theme("minimal")

        # Test the _dict_to_js_object function with our enhanced config
        js_config = _dict_to_js_object(theme.mermaid_config)

        # Verify the JavaScript object is valid and contains our enhancements
        assert f'"maxTextSize": {MAX_TEXT_SIZE_LARGE_PROJECTS}' in js_config
        assert f'"maxEdges": {MAX_EDGES_LARGE_PROJECTS}' in js_config
        assert '"theme": "neutral"' in js_config

        # Verify proper JavaScript object structure
        assert js_config.startswith("{")
        assert js_config.endswith("}")
        assert js_config.count('"maxTextSize":') == 1
        assert js_config.count('"maxEdges":') == 1

    def test_real_world_scenario_simulation(self):
        """Test simulating the real-world scenario from the issue."""
        # Simulate a large project scenario
        theme = get_theme("dark")  # User mentioned using dark theme
        html = get_html_template(theme)

        # Verify all the enhancements work together
        enhancements = {
            "maxTextSize": MAX_TEXT_SIZE_LARGE_PROJECTS,  # Prevents Mermaid text errors
            "maxEdges": MAX_EDGES_LARGE_PROJECTS,  # Handles large dependency count
        }

        text_enhancements = [
            "maxZoom: MAX_ZOOM",  # Allows detailed inspection
            "minZoom: MIN_ZOOM",  # Allows full overview
        ]

        # Check config values
        for key, value in enhancements.items():
            if key in theme.mermaid_config:
                assert theme.mermaid_config[key] == value

        # Check text content
        for enhancement in text_enhancements:
            assert enhancement in html

    def test_issue_specific_values_exactly_match(self):
        """Test that our fix exactly matches the values shown in the issue screenshot."""
        # The screenshot showed these exact values being manually set
        expected_max_text_size = MAX_TEXT_SIZE_LARGE_PROJECTS  # Exactly as shown in screenshot
        expected_max_edges = MAX_EDGES_LARGE_PROJECTS  # As mentioned for large projects

        for theme_name in ["minimal", "dark"]:
            theme = get_theme(theme_name)

            assert theme.mermaid_config["maxTextSize"] == expected_max_text_size
            assert theme.mermaid_config["maxEdges"] == expected_max_edges

    def test_performance_considerations(self):
        """Test that the enhancements don't negatively impact performance for smaller projects."""
        theme = get_theme("minimal")
        html = get_html_template(theme)

        # Verify that zoom controls have reasonable bounds to prevent performance issues
        assert "beforeZoom: function(oldScale, newScale)" in html
        assert "return newScale >= MIN_ZOOM && newScale <= MAX_ZOOM;" in html
