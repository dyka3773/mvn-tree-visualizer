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

## Current Release: v1.3.0 🚀

*   **"Watch" Mode:** (In Progress)
    *   [ ] `--watch` flag for automatic regeneration
    *   [ ] File system monitoring with real-time updates
*   **Enhanced Error Handling:**
    *   [ ] Clear error messages for missing files
    *   [ ] Helpful parsing diagnostics
    *   [ ] Maven command suggestions
*   **Visual Themes:**
    *   [ ] `--theme` option with multiple themes
    *   [ ] Dark, light, and colorful theme options
    *   [ ] Better default styling

## Near-Term Goals (1-3 Months)

*   **Code Quality:**
    *   [ ] Separate parser module for better modularity
    *   [ ] Enhanced test coverage for new features
*   **User Experience:**
    *   [ ] Interactive features (tooltips, hover effects)
    *   [ ] Better layout options for large dependency trees
    *   [ ] Performance optimizations for very large projects

## Mid-Term Goals (3-6 Months)

*   **Advanced Features:**
    *   [ ] Dependency conflict detection and highlighting
    *   [ ] Export options (PNG, PDF, SVG improvements)
    *   [ ] Dependency statistics and analysis
*   **Integration Capabilities:**
    *   [ ] CI/CD pipeline integration examples
    *   [ ] Docker support and containerization
    *   [ ] Maven plugin version (if demand exists)

## Long-Term Goals (6-12 Months)

*   **Web-Based Version:** A web-based version where users can paste their dependency tree and get a visualization without installing the CLI.
*   **IDE Integration:** Plugins for VS Code, IntelliJ IDEA, or Eclipse for direct dependency visualization.
*   **Multi-Language Support:** Extend beyond Maven to support Gradle, npm, pip, etc.

## Contributing

If you're interested in contributing to any of these features, please check out our [CONTRIBUTING.md](CONTRIBUTING.md) file for more information.

---

*Last updated: July 9, 2025*
