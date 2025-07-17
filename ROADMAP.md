# Project Roadmap

This document outlines the future direction of the `mvn-tree-visualizer` project. It's a living document, and the priorities may change based on user feedback and community contributions.

## Recently Completed ✅

*   **Support for Multiple Output Formats:**
    *   [x] JSON output format
    *   [x] HTML output format
*   **Display Dependency Versions:**
    *   [x] `--show-versions` flag for both HTML and JSON
*   **Development Infrastructure:**
    *   [x] Comprehensive type hints
    *   [x] Unit tests with good coverage
    *   [x] CI/CD workflows
    *   [x] Documentation and examples
    *   [x] Issue templates and community guidelines
*   **Watch Mode Feature:**
    *   [x] `--watch` flag for automatic regeneration
    *   [x] File system monitoring with real-time updates
    *   [x] Graceful error handling during watch mode
*   **Enhanced Error Handling:**
    *   [x] Clear error messages for missing files with helpful guidance
    *   [x] Specific diagnostics for parsing errors and validation
    *   [x] Maven command suggestions when files are missing
    *   [x] Better error recovery and user guidance
*   **Code Quality Improvements:**
    *   [x] Modular code organization (exceptions.py, validation.py)
    *   [x] Enhanced test coverage for error scenarios
    *   [x] Clean separation of concerns in CLI module

## v1.3.0 - User Experience Improvements ✅

**Focus:** Making the tool more user-friendly and robust for daily use.

*   **Status:** Released July 9, 2025
*   **Completed Tasks:**
    *   [x] Watch mode functionality with `--watch` flag
    *   [x] Enhanced error handling system with comprehensive user guidance
    *   [x] Custom exception classes and validation modules
    *   [x] Comprehensive test coverage (22 tests)
    *   [x] Modular code organization improvements

## v1.4.0 - Visual and Theme Enhancements ✅ (Released)

**Focus:** Making the output more visually appealing and customizable.

**Status:** Released July 17, 2025

*   **Visual Themes (Completed):**
    *   [x] `--theme` option with multiple built-in themes (default/minimal, dark, light)
    *   [x] Standardized color scheme across all themes
    *   [x] Clean minimal design as default theme  
    *   [x] Enhanced dark theme with proper text visibility
    *   [x] Consistent graphDiv styling across themes
*   **Interactive Features (Completed):**
    *   [x] SVG download functionality
    *   [x] Pan and zoom controls with keyboard shortcuts
    *   [x] Full-screen diagram experience
    *   [x] Improved hover effects for nodes
*   **Template Enhancements (Completed):**
    *   [x] Enhanced template system with theme support
    *   [x] Improved Mermaid.js configuration options
    *   [x] Standardized color coding for node types (root=blue, intermediate=orange, leaf=green)
    *   [x] Comprehensive examples for all themes

## v1.5.0 - Interactive Features 🎯 (Next Release)

**Focus:** Enhanced interactivity and user experience.

**Priority:** High - Building on the solid theme foundation with interactive capabilities.

*   **Node Interaction Features (High Priority):**
    *   [ ] **Descendant Highlighting:** Click nodes to highlight only their downstream dependencies
    *   [ ] Tooltips with detailed dependency information (groupId, version, scope)
    *   [ ] Expandable/collapsible dependency groups for large trees
    *   [ ] Search and filter functionality within diagrams
*   **Enhanced Controls (Medium Priority):**
    *   [ ] PNG download option alongside SVG
    *   [ ] Zoom to fit specific dependency subtrees
    *   [ ] Better visual hierarchy controls for nested dependencies
*   **Performance & Layout (Medium Priority):**
    *   [ ] Better layout options for large dependency trees
    *   [ ] Performance optimizations for very large projects

## v1.6.0 - Advanced Features 🚀

**Focus:** Performance and advanced functionality for power users.

*   **Export Enhancements:**
    *   [ ] PNG, PDF export options
    *   [ ] SVG improvements and customization
    *   [ ] High-quality output for presentations
*   **Advanced Analysis:**
    *   [ ] Memory usage improvements for complex graphs
    *   [ ] Dependency statistics and analysis

## v1.7.0+ - Extended Capabilities 🔮

**Focus:** Advanced analysis and integration features.

*   **Dependency Analysis:**
    *   [ ] Dependency conflict detection and highlighting
    *   [ ] Dependency statistics and analysis
    *   [ ] Version mismatch warnings
*   **Integration Capabilities:**
    *   [ ] CI/CD pipeline integration examples
    *   [ ] Docker support and containerization
    *   [ ] Maven plugin version (if demand exists)

## Long-Term Vision (6-12 Months+)

*   **Web-Based Version:** A web-based version where users can paste their dependency tree and get a visualization without installing the CLI.
*   **IDE Integration:** Plugins for VS Code, IntelliJ IDEA, or Eclipse for direct dependency visualization.
*   **Multi-Language Support:** Extend beyond Maven to support Gradle, npm, pip, etc.

## Release Strategy

Each release follows this approach:
- **Incremental Value:** Each version adds meaningful value without breaking existing functionality
- **User-Driven:** Priority based on user feedback and common pain points
- **Quality First:** New features include comprehensive tests and documentation
- **Backward Compatibility:** CLI interface remains stable across minor versions

## Contributing

If you're interested in contributing to any of these features, please check out our [CONTRIBUTING.md](CONTRIBUTING.md) file for more information.

---

*Last updated: July 16, 2025*
