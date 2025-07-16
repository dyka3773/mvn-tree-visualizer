# GitHub Copilot Instructions for mvn-tree-visualizer

## Project Overview
This is a Python CLI tool that parses Maven dependency trees (`mvn dependency:tree` output) and generates interactive HTML diagrams (using Mermaid.js) or JSON outputs. The tool supports watch mode for real-time regeneration and has a modular architecture focused on error handling and user experience.

## Architecture & Key Components

### Core Flow
1. **Input Validation** (`validation.py`) - Find and validate Maven dependency files
2. **File Merging** (`get_dependencies_in_one_file.py`) - Combine multiple dependency files
3. **Parsing** (`diagram.py`) - Read merged dependency tree
4. **Output Generation** (`outputs/`) - Generate HTML (Mermaid.js) or JSON
5. **Watch Mode** (`file_watcher.py`) - Monitor files for changes using watchdog

### Module Structure
```
src/mvn_tree_visualizer/
├── cli.py              # Entry point with comprehensive error handling
├── exceptions.py       # Custom exception hierarchy
├── validation.py       # File discovery and validation logic
├── diagram.py          # Core dependency tree processing
├── file_watcher.py     # Real-time file monitoring
├── get_dependencies... # Multi-file merging logic
├── TEMPLATE.py         # Jinja2 HTML template for Mermaid.js
└── outputs/
    ├── html_output.py  # Mermaid diagram generation
    └── json_output.py  # Structured JSON output
```

## Development Conventions

### Error Handling Pattern
- Use custom exceptions from `exceptions.py`: `DependencyFileNotFoundError`, `DependencyParsingError`, `OutputGenerationError`
- Provide actionable error messages with Maven commands and file paths
- Follow the pattern in `cli.py:generate_diagram()` for comprehensive error handling

### Testing Approach
- Use pytest with descriptive test names like `test_convert_to_mermaid_deeper_tree()`
- Test both positive cases and error conditions
- Include realistic Maven dependency tree samples in test data
- Run tests with: `uv run pytest tests/ -v`

### Package Management
- Uses `uv` as package manager - always use `uv run` for commands
- Core dependencies: `jinja2` (templating), `watchdog` (file monitoring)
- Entry point: `mvn-tree-visualizer` command maps to `cli:cli`

### Code Quality
- Lint with: `uv run ruff check .`
- Type hints required throughout (project uses Python 3.13+)
- Follow existing patterns for file validation and path handling

## Critical Implementation Details

### Maven Dependency Parsing
- Input format: `[INFO] groupId:artifactId:type:version:scope` with tree structure using `+`, `|`, `\`
- Handle both 4-part and 5-part dependency strings (see `html_output.py:_convert_to_mermaid`)
- Depth calculation based on whitespace: `depth = len(parts[0].split(" ")) - 1`

### File Discovery Pattern
- Multi-file support: searches directory tree for `maven_dependency_file` (configurable)
- Merges files from different Maven modules into single intermediate file
- Validates file existence, permissions, and content before processing

### Output Generation
- HTML uses Mermaid.js with `graph LR` format
- Version display controlled by `--show-versions` flag
- JSON output maintains tree structure with parent-child relationships

### Watch Mode Implementation
- Uses watchdog library for cross-platform file monitoring
- Monitors specific filename pattern across directory tree
- Debounces changes and provides timestamped feedback

## Common Development Tasks

### Adding New Output Formats
1. Create new module in `outputs/` directory
2. Follow pattern from `html_output.py` and `json_output.py`
3. Add format option to CLI and update `generate_diagram()` in `cli.py`

### Error Message Improvements
- All user-facing errors should include specific file paths and suggested Maven commands
- Use `print_maven_help()` pattern for guiding users to generate dependency files
- Test error scenarios in addition to happy path

### Testing New Features
- Include realistic Maven dependency trees in test data
- Test both single-module and multi-module project scenarios
- Verify error handling with invalid/missing files

Remember: This tool processes Maven output files, not Maven projects directly. Users must run `mvn dependency:tree -DoutputFile=maven_dependency_file` first.
