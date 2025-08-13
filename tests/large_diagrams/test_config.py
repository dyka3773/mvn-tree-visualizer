"""Tests for large diagram support configuration."""

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
