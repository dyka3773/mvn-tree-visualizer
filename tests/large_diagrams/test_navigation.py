"""Tests for enhanced navigation features in HTML templates."""

from mvn_tree_visualizer.enhanced_template import get_html_template
from mvn_tree_visualizer.themes import get_theme


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

        # Check for control group structure
        assert 'class="control-group"' in html
        assert 'class="control-label"' in html
        assert "Navigation:" in html

    def test_both_themes_have_enhanced_features(self):
        """Test that both minimal and dark themes have enhanced navigation features."""
        for theme_name in ["minimal", "dark"]:
            theme = get_theme(theme_name)
            html = get_html_template(theme)

            # Check that both themes have the enhanced features
            assert "zoomInButton" in html
            assert "zoomOutButton" in html
            assert "resetZoomButton" in html
            assert "minZoom: MIN_ZOOM" in html
            assert "maxZoom: MAX_ZOOM" in html
