"""Tests for error handling and edge cases for enhanced features."""

from mvn_tree_visualizer.enhanced_template import get_html_template
from mvn_tree_visualizer.themes import THEMES, get_theme


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
