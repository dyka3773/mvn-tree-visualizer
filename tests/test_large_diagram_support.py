"""Tests for large diagram support and enhanced navigation features."""

from mvn_tree_visualizer.enhanced_template import get_html_template
from mvn_tree_visualizer.themes import MAX_EDGES_LARGE_PROJECTS, MAX_TEXT_SIZE_LARGE_PROJECTS, THEMES, get_theme


class TestLargeDiagramSupport:
    """Test suite for large dependency tree handling."""

    def test_mermaid_config_has_large_limits(self):
        """Test that both themes have increased maxTextSize and maxEdges for large projects."""
        for theme_name in THEMES.keys():
            theme = get_theme(theme_name)

            # Verify that both themes have the large diagram configuration
            assert "maxTextSize" in theme.mermaid_config
            assert "maxEdges" in theme.mermaid_config

            # Check that the values are set to handle large projects
            assert theme.mermaid_config["maxTextSize"] == MAX_TEXT_SIZE_LARGE_PROJECTS
            assert theme.mermaid_config["maxEdges"] == MAX_EDGES_LARGE_PROJECTS

    def test_minimal_theme_large_config(self):
        """Test that minimal theme has proper large diagram configuration."""
        theme = get_theme("minimal")

        expected_config_keys = ["theme", "themeVariables", "maxTextSize", "maxEdges"]

        for key in expected_config_keys:
            assert key in theme.mermaid_config

        # Test specific values for minimal theme
        assert theme.mermaid_config["theme"] == "neutral"
        assert theme.mermaid_config["maxTextSize"] == MAX_TEXT_SIZE_LARGE_PROJECTS
        assert theme.mermaid_config["maxEdges"] == MAX_EDGES_LARGE_PROJECTS

    def test_dark_theme_large_config(self):
        """Test that dark theme has proper large diagram configuration."""
        theme = get_theme("dark")

        expected_config_keys = ["theme", "themeVariables", "maxTextSize", "maxEdges"]

        for key in expected_config_keys:
            assert key in theme.mermaid_config

        # Test specific values for dark theme
        assert theme.mermaid_config["theme"] == "forest"
        assert theme.mermaid_config["maxTextSize"] == MAX_TEXT_SIZE_LARGE_PROJECTS
        assert theme.mermaid_config["maxEdges"] == MAX_EDGES_LARGE_PROJECTS


class TestEnhancedNavigation:
    """Test suite for enhanced navigation features in HTML templates."""

    def test_enhanced_zoom_controls_present(self):
        """Test that enhanced zoom controls are included in HTML output."""
        theme = get_theme("minimal")
        html = get_html_template(theme)

        # Check for navigation control buttons
        assert 'id="zoomInButton"' in html
        assert 'id="zoomOutButton"' in html
        assert 'id="resetZoomButton"' in html

        # Check for button labels
        assert "Zoom In (+)" in html
        assert "Zoom Out (-)" in html
        assert "Reset (Ctrl+R)" in html

    def test_improved_zoom_configuration(self):
        """Test that improved zoom settings are configured in the JavaScript."""
        theme = get_theme("minimal")
        html = get_html_template(theme)

        # Check for improved zoom limits
        assert "minZoom: MIN_ZOOM" in html  # Much lower min zoom for large diagrams
        assert "maxZoom: MAX_ZOOM" in html  # Much higher max zoom for detail inspection
        assert "zoomScaleSensitivity: ZOOM_SCALE_SENSITIVITY" in html  # Smoother zoom increments
        assert "mouseWheelZoomEnabled: true" in html
        assert "preventMouseEventsDefault: true" in html

    def test_enhanced_keyboard_shortcuts(self):
        """Test that enhanced keyboard shortcuts are implemented."""
        theme = get_theme("minimal")
        html = get_html_template(theme)

        # Check for keyboard shortcut handling
        assert "Ctrl+R" in html  # Reset shortcut

        # Check for specific shortcuts
        shortcuts_to_check = [
            "case 's':",  # Download
            "case 'r':",  # Reset
            "case '=':",  # Zoom in
            "case '+':",  # Zoom in alternative
            "case '-':",  # Zoom out
        ]

        for shortcut in shortcuts_to_check:
            assert shortcut in html

    def test_pan_and_zoom_error_handling(self):
        """Test that proper error handling is in place for pan and zoom operations."""
        theme = get_theme("minimal")
        html = get_html_template(theme)

        # Check for error prevention
        assert "catch (error)" in html  # Generic error handling
        assert "beforeZoom: function(oldScale, newScale)" in html
        assert "return newScale >= MIN_ZOOM && newScale <= MAX_ZOOM;" in html

    def test_control_group_organization(self):
        """Test that controls are properly organized in groups."""
        theme = get_theme("minimal")
        html = get_html_template(theme)

        # Check for control group organization
        assert 'class="control-group"' in html
        assert 'class="control-label"' in html
        assert "Navigation:" in html

    def test_both_themes_have_enhanced_features(self):
        """Test that both minimal and dark themes have the enhanced features."""
        for theme_name in ["minimal", "dark"]:
            theme = get_theme(theme_name)
            html = get_html_template(theme)

            # Essential enhanced navigation features
            assert "zoomInButton" in html
            assert "minZoom: MIN_ZOOM" in html
            assert "maxZoom: MAX_ZOOM" in html


class TestBackwardCompatibility:
    """Test that existing functionality still works with the enhancements."""

    def test_existing_download_functionality_preserved(self):
        """Test that existing SVG download functionality is preserved."""
        theme = get_theme("minimal")
        html = get_html_template(theme)

        # Check that download functionality is still present
        assert 'id="downloadButton"' in html
        assert "downloadSVG" in html
        assert "Download SVG" in html
        assert "dependency-diagram.svg" in html

    def test_existing_mermaid_config_preserved(self):
        """Test that existing Mermaid configuration is preserved alongside new features."""
        theme = get_theme("minimal")

        # Check that existing theme variables are still present
        assert "primaryColor" in theme.mermaid_config["themeVariables"]
        assert "primaryTextColor" in theme.mermaid_config["themeVariables"]
        assert "lineColor" in theme.mermaid_config["themeVariables"]

        # Check that theme name is preserved
        assert theme.mermaid_config["theme"] == "neutral"

    def test_existing_dark_theme_fixes_preserved(self):
        """Test that existing dark theme text visibility fixes are preserved."""
        theme = get_theme("dark")
        html = get_html_template(theme)

        # Check for dark theme specific fixes
        assert "Force white text for all mermaid elements in dark theme" in html
        assert "fill: #ffffff !important;" in html
        assert "color: #ffffff !important;" in html


class TestErrorScenarios:
    """Test error handling and edge cases for enhanced features."""

    def test_invalid_theme_fallback_includes_enhancements(self):
        """Test that fallback theme includes the enhanced features."""
        # Get invalid theme (should fallback to minimal)
        theme = get_theme("nonexistent_theme")
        html = get_html_template(theme)

        # Verify fallback theme has enhancements
        assert theme.name == "minimal"
        assert "maxTextSize" in theme.mermaid_config
        assert "zoomInButton" in html

    def test_mermaid_config_structure_validation(self):
        """Test that Mermaid configuration has proper structure."""
        for theme_name in THEMES.keys():
            theme = get_theme(theme_name)
            config = theme.mermaid_config

            # Verify required structure
            assert isinstance(config, dict)
            assert isinstance(config.get("themeVariables"), dict)
            assert isinstance(config.get("maxTextSize"), int)
            assert isinstance(config.get("maxEdges"), int)

            # Verify reasonable values
            assert config["maxTextSize"] > 0
            assert config["maxEdges"] > 0
