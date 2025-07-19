"""Enhanced HTML templates with the interactive features."""

from typing import Any, Dict

from .themes import MAX_ZOOM, MIN_ZOOM, STANDARD_COLORS, ZOOM_SCALE_SENSITIVITY, Theme


def get_html_template(theme: Theme) -> str:
    """Generate HTML template with theme-specific styling and interactive features."""

    # Build Mermaid configuration
    mermaid_config = {
        "startOnLoad": True,
        "sequence": {"useMaxWidth": False},
        "theme": theme.mermaid_theme,
        **theme.mermaid_config,
    }

    # Convert config to JavaScript object
    mermaid_config_js = _dict_to_js_object(mermaid_config)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Maven Dependency Diagram - {theme.name.title()} Theme</title>
    <style>
        #mySvgId {{
            height: 100%;
            width: 100%;
        }}
        
        /* Theme-specific styles */
        {theme.custom_css}
        
        /* Dark theme text visibility fixes */
        {
        ""
        if theme.name != "dark"
        else '''
        /* Force white text for all mermaid elements in dark theme */
        .node text, .edgeLabel text, text, .label text {
            fill: #ffffff !important;
            color: #ffffff !important;
        }
        
        /* Ensure node backgrounds are visible */
        .node rect, .node circle, .node ellipse, .node polygon {
            fill: #4a5568 !important;
            stroke: #e2e8f0 !important;
            stroke-width: 1px !important;
        }
        
        /* Edge styling for dark theme */
        .edge path, .flowchart-link {
            stroke: #a0aec0 !important;
            stroke-width: 2px !important;
        }
        
        /* Arrow styling */
        .arrowheadPath {
            fill: #a0aec0 !important;
            stroke: #a0aec0 !important;
        }
        '''
    }
        
        /* Improved node styling */
        .node {{
            cursor: pointer;
            transition: opacity 0.2s ease;
        }}
        
        .node:hover {{
            opacity: 0.8;
        }}
        
        /* Highlighting styles */
        .highlighted {{
            opacity: 1 !important;
            filter: drop-shadow(0 0 8px {STANDARD_COLORS["root_node"]});
        }}
        
        .dimmed {{
            opacity: 0.3;
        }}
    </style>
</head>
<body>
    <div class="controls">
        <div class="control-group">
            <button id="downloadButton" class="toggle-btn">Download SVG</button>
            <!-- Note: PNG download feature to be implemented in future version -->
        </div>
        <div class="control-group">
            <span class="control-label">Navigation:</span>
            <button id="zoomInButton" class="toggle-btn">Zoom In (+)</button>
            <button id="zoomOutButton" class="toggle-btn">Zoom Out (-)</button>
            <button id="resetZoomButton" class="toggle-btn">Reset (Ctrl+R)</button>
        </div>
    </div>
    
    <div id="graphDiv"></div>
    
    <script src="https://cdn.jsdelivr.net/npm/svg-pan-zoom@3.5.0/dist/svg-pan-zoom.min.js"></script>
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11.9.0/dist/mermaid.esm.min.mjs';
        
        // Initialize mermaid with theme configuration
        mermaid.initialize({mermaid_config_js});

        // Global variables
        let panZoomInstance = null;
        
        const MIN_ZOOM = {MIN_ZOOM};
        const MAX_ZOOM = {MAX_ZOOM};
        const ZOOM_SCALE_SENSITIVITY = {ZOOM_SCALE_SENSITIVITY};
        
        const drawDiagram = async function () {{
            const element = document.querySelector('#graphDiv');
            const graphDefinition = `{{{{diagram_definition}}}}`;
            
            try {{
                const {{ svg }} = await mermaid.render('mySvgId', graphDefinition);
                element.innerHTML = svg.replace(/[ ]*max-width:[ 0-9\\.]*px;/i , '');
                
                // Initialize pan & zoom with improved settings for large diagrams
                panZoomInstance = svgPanZoom('#mySvgId', {{
                    zoomEnabled: true,
                    controlIconsEnabled: true,
                    fit: true,
                    center: true,
                    minZoom: MIN_ZOOM,  // Allow zooming out further for large diagrams
                    maxZoom: MAX_ZOOM,  // Allow much higher zoom for detailed inspection
                    zoomScaleSensitivity: ZOOM_SCALE_SENSITIVITY,  // Smoother zoom increments
                    mouseWheelZoomEnabled: true,
                    preventMouseEventsDefault: true,
                    beforeZoom: function(oldScale, newScale) {{
                        // Prevent zooming beyond reasonable limits
                        return newScale >= MIN_ZOOM && newScale <= MAX_ZOOM;
                    }}
                }});
                
                // Setup node interactions
                setupNodeInteractions();
                
            }} catch (error) {{
                console.error('Error rendering diagram:', error);
                element.innerHTML = `<p style="color: red; padding: 20px;">Error rendering diagram: ${{error.message}}</p>`;
            }}
        }};
        
        const setupNodeInteractions = function() {{
            const nodes = document.querySelectorAll('#mySvgId .node');
            
            nodes.forEach(node => {{
                node.style.cursor = 'pointer';
            }});
        }};
        
        // Button event listeners
        document.getElementById('downloadButton').addEventListener('click', function() {{
            downloadSVG();
        }});
        
        document.getElementById('zoomInButton').addEventListener('click', function() {{
            if (panZoomInstance) {{
                panZoomInstance.zoomIn();
            }}
        }});
        
        document.getElementById('zoomOutButton').addEventListener('click', function() {{
            if (panZoomInstance) {{
                panZoomInstance.zoomOut();
            }}
        }});
        
        document.getElementById('resetZoomButton').addEventListener('click', function() {{
            if (panZoomInstance) {{
                panZoomInstance.reset();
            }}
        }});
        
        const downloadSVG = function() {{
            const svg = document.querySelector('#mySvgId');
            let svgData = new XMLSerializer().serializeToString(svg);
            
            // Clean up pan & zoom controls
            svgData = svgData.replace(/<g\\b[^>]*\\bclass="svg-pan-zoom-.*?".*?>.*?<\\/g>/g, '');
            svgData = svgData.replace(/<\\/g><\\/svg>/, '</svg>');
            
            const svgBlob = new Blob([svgData], {{type: 'image/svg+xml;charset=utf-8'}});
            const svgUrl = URL.createObjectURL(svgBlob);
            const downloadLink = document.createElement('a');
            downloadLink.href = svgUrl;
            downloadLink.download = 'dependency-diagram.svg';
            document.body.appendChild(downloadLink);
            downloadLink.click();
            document.body.removeChild(downloadLink);
            URL.revokeObjectURL(svgUrl);
        }};
        
        // Initialize the diagram
        await drawDiagram();
        
        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {{
            if (e.ctrlKey || e.metaKey) {{
                switch(e.key) {{
                    case 's':
                        e.preventDefault();
                        downloadSVG();
                        break;
                    case 'r':
                        e.preventDefault();
                        if (panZoomInstance) {{
                            panZoomInstance.reset();
                        }}
                        break;
                    case '=':
                    case '+':
                        e.preventDefault();
                        if (panZoomInstance) {{
                            panZoomInstance.zoomIn();
                        }}
                        break;
                    case '-':
                        e.preventDefault();
                        if (panZoomInstance) {{
                            panZoomInstance.zoomOut();
                        }}
                        break;
                }}
            }} else {{
                // Non-Ctrl shortcuts
                switch(e.key) {{
                    case '+':
                    case '=':
                        if (panZoomInstance) {{
                            panZoomInstance.zoomIn();
                        }}
                        break;
                    case '-':
                        if (panZoomInstance) {{
                            panZoomInstance.zoomOut();
                        }}
                        break;
                }}
            }}
        }});
        
    </script>
</body>
</html>"""


def _dict_to_js_object(d: Dict[str, Any], indent: int = 0) -> str:
    """Convert Python dict to JavaScript object string."""
    if not isinstance(d, dict):
        if isinstance(d, str):
            return f'"{d}"'
        elif isinstance(d, bool):
            return str(d).lower()
        else:
            return str(d)

    items = []
    for key, value in d.items():
        if isinstance(value, dict):
            value_str = _dict_to_js_object(value, indent + 1)
        elif isinstance(value, str):
            value_str = f'"{value}"'
        elif isinstance(value, bool):
            value_str = str(value).lower()
        else:
            value_str = str(value)

        items.append(f'"{key}": {value_str}')

    return "{" + ", ".join(items) + "}"
