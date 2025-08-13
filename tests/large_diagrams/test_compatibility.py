"""Tests for backward compatibility with existing functionality."""

from mvn_tree_visualizer.enhanced_template import get_html_template
from mvn_tree_visualizer.themes import get_theme


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
