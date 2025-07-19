# Maven Dependency Tree Visualizer - AI Coding Agent Instructions

## Architecture Overview

This is a **command-line tool** that converts Maven dependency tree output into interactive HTML diagrams and JSON data. The tool follows a **pipeline architecture**:

1. **Input Processing**: Merges multiple `maven_dependency_file` files from different Maven modules (`get_dependencies_in_one_file.py`)
2. **Data Transformation**: Parses Maven tree format and converts to Mermaid diagram syntax (`diagram.py`, `outputs/html_output.py`)
3. **Output Generation**: Creates themed HTML with interactive features or structured JSON (`outputs/`)
4. **Watch Mode**: Real-time file monitoring for development workflows (`file_watcher.py`)

## Key Components & Data Flow

### Core Pipeline (`cli.py`)
- Entry point validates inputs → merges dependency files → generates outputs
- **Error handling is comprehensive** - uses custom exception hierarchy in `exceptions.py`
- Supports both HTML (interactive) and JSON (programmatic) output formats

### Multi-Module Maven Support (`get_dependencies_in_one_file.py`)
- **Critical pattern**: Recursively finds and merges `maven_dependency_file` from all subdirectories
- Maven projects often have complex module structures - tool handles this automatically
- Generated intermediate file `dependency_tree.txt` is cleaned up unless `--keep-tree` is used

### Mermaid.js Conversion (`outputs/html_output.py`)
- **Node classification logic**: Root (blue), intermediate (orange), leaf (green) based on dependency relationships
- **Sanitization pattern**: Maven artifact names → valid Mermaid node IDs (hyphens to underscores)
- Tracks parent/child relationships to determine node types for consistent styling

### Theme System (`themes.py`, `enhanced_template.py`)
- **Consistent color scheme** across all themes via `STANDARD_COLORS`
- Dark theme has specific text visibility fixes for Mermaid.js compatibility
- Template includes pan/zoom, download functionality, keyboard shortcuts

## Maven Integration Workflow

The tool expects this Maven command to be run first:
```bash
mvn dependency:tree -DoutputFile=maven_dependency_file -DappendOutput=true
```

**Why this matters**: The tool is designed around Maven's specific output format and file placement in `target/` directories.

## Development Conventions

### Error Handling
- Custom exception hierarchy: `MvnTreeVisualizerError` → specific error types
- **Pattern**: Validate early, fail fast with helpful error messages including Maven commands
- File operations wrapped with encoding and permission checks

### Testing Patterns (`tests/`)
- **Key test pattern**: Use temporary directories for file operations
- Mock file system events for watch mode testing
- Mermaid output validation focuses on relationships and styling classes

### Code Organization
- **Outputs as pluggable modules**: `outputs/html_output.py`, `outputs/json_output.py`
- Validation logic centralized in `validation.py`
- Theme configuration as data classes, not inheritance

## Critical Implementation Details

### Watch Mode (`file_watcher.py`)
- Uses `watchdog` library with custom event handlers
- Monitors for changes to any file named `maven_dependency_file` in directory tree
- Callback-based architecture for diagram regeneration

### Version Display Logic
- `--show-versions` flag affects both HTML and JSON output
- Version info stripped/included during Mermaid conversion, not at template level

### File Path Handling
- **Windows compatibility**: Uses `pathlib.Path` consistently
- Intermediate files created in output directory, not temp
- Directory creation is recursive (`parents=True, exist_ok=True`)

## Common Debugging Workflows

1. **No dependency files found**: Check if Maven command was run and generated files in `target/` dirs
2. **Empty diagrams**: Verify Maven output format and encoding (UTF-8 expected)
3. **Theme rendering issues**: Dark theme has specific CSS overrides for Mermaid.js text visibility
4. **Watch mode not triggering**: Ensure file names match exactly (`maven_dependency_file`)

## Extension Points

- **New output formats**: Add modules to `outputs/` directory following existing pattern
- **Custom themes**: Extend `THEMES` dict in `themes.py` with `Theme` objects
- **New validation rules**: Add to `validation.py` following existing error patterns
