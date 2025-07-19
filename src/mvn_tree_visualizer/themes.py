"""Theme configurations for mvn-tree-visualizer diagrams."""

from typing import Any, Dict

# Mermaid configuration constants for large project support
MAX_TEXT_SIZE_LARGE_PROJECTS = 900000000  # Increase max text size for large dependency trees
MAX_EDGES_LARGE_PROJECTS = 20000  # Increase max edges for large projects

# Zoom configuration constants for enhanced navigation
MIN_ZOOM = 0.01  # Minimum zoom level for large diagram overview
MAX_ZOOM = 50  # Maximum zoom level for detailed inspection
ZOOM_SCALE_SENSITIVITY = 0.2  # Smoother zoom increments


class Theme:
    """Base theme configuration class."""

    def __init__(
        self,
        name: str,
        mermaid_theme: str = "default",
        background_color: str = "#ffffff",
        custom_css: str = "",
        mermaid_config: Dict[str, Any] = None,
    ):
        self.name = name
        self.mermaid_theme = mermaid_theme
        self.background_color = background_color
        self.custom_css = custom_css
        self.mermaid_config = mermaid_config or {}


# Standard color scheme for consistency across themes
# Root nodes: Blue shades, Intermediate nodes: Orange shades, Leaf nodes: Green shades
STANDARD_COLORS = {
    "root_node": "#3B82F6",  # Blue for root nodes
    "intermediate_node": "#F59E0B",  # Orange for intermediate nodes
    "leaf_node": "#10B981",  # Green for leaf nodes
}

# Predefined themes
THEMES = {
    "minimal": Theme(
        name="minimal",
        mermaid_theme="neutral",
        background_color="#ffffff",
        custom_css="""
        body {
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
            margin: 0;
            padding: 20px;
            background-color: #ffffff;
            color: #000000;
            line-height: 1.6;
            height: 100vh;
            box-sizing: border-box;
        }
        #graphDiv {
            background-color: #ffffff;
            border: 1px solid #000000;
            padding: 20px;
            margin-bottom: 20px;
            height: calc(100vh - 120px);
            overflow: hidden;
        }
        .controls {
            margin-bottom: 20px;
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            align-items: center;
        }
        .control-group {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .control-label {
            font-size: 12px;
            font-weight: normal;
            color: #000000;
            text-transform: uppercase;
        }
        .toggle-btn {
            background-color: #000000;
            color: white;
            border: none;
            padding: 8px 16px;
            cursor: pointer;
            font-family: inherit;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: opacity 0.2s;
        }
        .toggle-btn:hover {
            opacity: 0.8;
        }
        """,
        mermaid_config={
            "theme": "neutral",
            "themeVariables": {
                "primaryColor": STANDARD_COLORS["root_node"],
                "primaryTextColor": "#000000",
                "primaryBorderColor": "#000000",
                "lineColor": "#000000",
                "secondaryColor": "#f5f5f5",
                "tertiaryColor": "#ffffff",
            },
            "maxTextSize": MAX_TEXT_SIZE_LARGE_PROJECTS,  # Increase max text size for large dependency trees
            "maxEdges": MAX_EDGES_LARGE_PROJECTS,  # Increase max edges for large projects
        },
    ),
    "dark": Theme(
        name="dark",
        mermaid_theme="forest",
        background_color="#2d3748",
        custom_css="""
        body {
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
            margin: 0;
            padding: 20px;
            background-color: #2d3748;
            color: #f7fafc;
            line-height: 1.6;
            height: 100vh;
            box-sizing: border-box;
        }
        #graphDiv {
            background-color: #2d3748;
            border: 1px solid #e2e8f0;
            padding: 20px;
            margin-bottom: 20px;
            height: calc(100vh - 120px);
            overflow: hidden;
        }
        .controls {
            margin-bottom: 20px;
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            align-items: center;
        }
        .control-group {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .control-label {
            font-size: 12px;
            font-weight: normal;
            color: #f7fafc;
            text-transform: uppercase;
        }
        .toggle-btn {
            background-color: #f7fafc;
            color: #2d3748;
            border: none;
            padding: 8px 16px;
            cursor: pointer;
            font-family: inherit;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: opacity 0.2s;
        }
        .toggle-btn:hover {
            opacity: 0.8;
        }
        """,
        mermaid_config={
            "theme": "forest",
            "themeVariables": {
                "primaryColor": STANDARD_COLORS["root_node"],
                "primaryTextColor": "#ffffff",
                "primaryBorderColor": "#e2e8f0",
                "lineColor": "#a0aec0",
                "secondaryColor": "#4a5568",
                "tertiaryColor": "#2d3748",
                "background": "#2d3748",
                "mainBkg": "#4a5568",
                "nodeBkg": "#4a5568",
                "clusterBkg": "#2d3748",
                "edgeLabelBackground": "#2d3748",
                "nodeTextColor": "#ffffff",
                "textColor": "#ffffff",
            },
            "maxTextSize": MAX_TEXT_SIZE_LARGE_PROJECTS,  # Increase max text size for large dependency trees
            "maxEdges": MAX_EDGES_LARGE_PROJECTS,  # Increase max edges for large projects
        },
    ),
}


def get_theme(theme_name: str) -> Theme:
    """Get a theme by name, fallback to minimal if not found."""
    return THEMES.get(theme_name, THEMES["minimal"])


def get_available_themes() -> list[str]:
    """Get list of available theme names."""
    return list(THEMES.keys())
