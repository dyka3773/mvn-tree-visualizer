# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.2.0] - 2025-07-09

### Added
- Comprehensive type hints throughout the entire codebase
- `--show-versions` flag to display dependency versions in both HTML and JSON outputs
- Support for complex dependency trees with real-world examples
- "Typing :: Typed" classifier in pyproject.toml to indicate type hint support
- CHANGELOG.md to track project changes

### Changed
- Enhanced CLI help text to reflect new features
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
