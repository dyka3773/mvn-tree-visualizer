# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!--next-version-placeholder-->

## [1.3.0] - 2025-07-09

### Added
- Watch mode functionality with `--watch` flag for automatic diagram regeneration
- File system monitoring using watchdog library for real-time updates
- New file_watcher module for decoupled file monitoring logic
- Enhanced error handling system with comprehensive user guidance
  - Clear error messages for missing dependency files with helpful Maven commands
  - Specific validation for directories, file permissions, and content
  - Detailed diagnostics for parsing errors and empty files
  - User-friendly error messages with emojis and actionable suggestions
- Custom exception classes for better error categorization
- Comprehensive test coverage for error scenarios

### Changed
- **BREAKING**: JSON output now uses simplified package names (artifact-id only) to match HTML output behavior
  - Root packages now show as "my-app" instead of "com.example:my-app"
  - Ensures consistency between HTML and JSON output formats
- Refactored CLI module to separate concerns and improve maintainability
- Improved error handling with timestamped console output and graceful failure modes
- Enhanced file processing with better encoding handling (UTF-8) and validation
- Updated dependency file merging logic with better error detection

### Fixed
- Removed unused imports and improved code organization
- Fixed intermediate file path handling in diagram generation

## [1.2.0] - 2025-07-09

### Added
- Comprehensive type hints throughout the entire codebase
- `--show-versions` flag to display dependency versions in both HTML and JSON outputs
- Support for complex dependency trees with real-world examples
- "Typing :: Typed" classifier in pyproject.toml to indicate type hint support
- CHANGELOG.md to track project changes

### Changed
- Enhanced CLI help text to reflect new features
- Improved JSON output structure for better programmatic access
- Updated documentation with version feature examples

### Fixed
- Type annotation issues and improved code clarity
- JSON serialization for complex dependency structures

## [1.1.0] - 2025-07-05

### Added
- JSON output format option for programmatic consumption
- Multi-file support for Maven modules (searches for multiple `maven_dependency_file`)
- File merging functionality for complex projects
- Comprehensive error handling for file operations
- Enhanced CLI with format selection

### Changed
- Improved project structure with organized outputs directory
- Better separation of concerns between HTML and JSON generation

### Fixed
- File handling issues with large dependency trees
- Output format validation and error messages

## [1.0.0] - 2025-07-01

### Added
- Initial release of mvn-tree-visualizer
- HTML diagram generation using Mermaid.js
- CLI interface for processing Maven dependency files
- Basic error handling and validation
- Support for Maven dependency tree parsing
- Interactive HTML output with visual dependency graphs
- Improved code documentation and readability with type hints
- Updated README.md with new feature documentation and usage examples

### Fixed
- Better static type checking support for development tools

## [1.1.0] - 2025-07-08

### Added
- JSON output format support alongside existing HTML format
- `--format` CLI argument to choose between HTML and JSON outputs
- Comprehensive test suite for both output formats
- GitHub Actions workflow for automated PyPI publishing

### Changed
- Decoupled output generation logic from core diagram creation
- Improved code modularity with separate output modules

### Fixed
- Enhanced project structure and maintainability

## [1.0.0] - Initial Release

### Added
- HTML diagram generation using Mermaid.js
- Interactive SVG export functionality
- File merging from multiple Maven dependency files
- Basic CLI interface with essential options
- Project documentation and contribution guidelines
