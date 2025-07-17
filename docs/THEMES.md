# Theme System Documentation

The mvn-tree-visualizer v1.4.0 introduces a clean and focused theme system with two carefully designed themes.

## Available Themes

### 1. Minimal Theme (Default)
- **Description**: Clean monospace design with simple black borders and minimal styling
- **Use case**: Default choice for documentation, development, and general use
- **Colors**: Standardized blue for root nodes, orange for intermediate, green for leaves
- **Features**: Monospace fonts, clean lines, no decorative elements
- **Background**: White with black text and borders

### 2. Dark Theme  
- **Description**: Same minimal styling as default but optimized for low-light environments
- **Use case**: Late-night coding sessions, dark IDE environments, reducing eye strain
- **Colors**: Same standardized color scheme on enhanced dark backgrounds
- **Features**: Identical layout to minimal theme with inverted colors
- **Background**: Dark gray (`#2d3748`) with white text and light borders

## Standardized Color Scheme

Both themes use a consistent color scheme for better recognition:
- **Root Nodes**: Blue (#3B82F6) - Your main project dependencies
- **Intermediate Nodes**: Orange (#F59E0B) - Transitive dependencies with children
- **Leaf Nodes**: Green (#10B981) - Final dependencies with no children

## Usage

### CLI Usage
```bash
# Use minimal theme (default)
mvn-tree-visualizer /path/to/project

# Use dark theme
mvn-tree-visualizer /path/to/project --theme dark

# Combine with other options
mvn-tree-visualizer /path/to/project --theme dark --show-versions --output my-diagram.html
```

### Available Theme Options
- `minimal` - Clean minimal design (default)
- `dark` - Same minimal design with dark colors

## Interactive Features

### 1. Enhanced Controls
- **Download SVG**: Export diagram as scalable vector graphics
- **Note**: PNG download feature planned for future version

### 2. Node Interactions
- **Hover Effects**: Nodes show subtle opacity changes on hover
- **Click Functionality**: Currently disabled - planned for future version

### 3. Keyboard Shortcuts
- **Ctrl+S**: Download as SVG
- **Ctrl+R**: Reset pan/zoom to center

### 4. Pan and Zoom
- **Mouse Controls**: Drag to pan, scroll to zoom
- **Touch Support**: Mobile-friendly touch controls
- **Reset Controls**: Built-in reset and fit-to-screen

## Full-Screen Experience

The diagram takes up the full height of the browser window minus the control bar, providing maximum space for viewing complex dependency trees.

## Node Styling

The enhanced Mermaid generation includes intelligent node styling:

### Node Types
- **Root Nodes**: Blue styling for main project dependencies
- **Leaf Nodes**: Green styling for final dependencies
- **Intermediate Nodes**: Orange styling for transitive dependencies

### Enhanced Features
- **Sanitized IDs**: Safe Mermaid-compatible node identifiers
- **Proper Labels**: Clean display names with version support
- **Consistent Styling**: Identical appearance across both themes

## Browser Compatibility

The enhanced templates work with:
- Chrome/Chromium 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Examples

### Basic Theme Usage
```bash
# Generate with dark theme
mvn-tree-visualizer . --theme dark --output dark-deps.html

# Generate with minimal theme (default)
mvn-tree-visualizer . --output minimal-deps.html
```

### Watch Mode with Themes
```bash
# Watch for changes with dark theme
mvn-tree-visualizer . --theme dark --watch
```
