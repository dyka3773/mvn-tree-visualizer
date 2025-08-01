# Project Roadmap

This document outlines the evolution and future direction of the `mvn-tree-visualizer` project. Major milestones show the progression from a basic tool to an enterprise-ready solution.

## 🎉 Recently Completed ✅

### v1.6.0 - Mistake Release (Released)

**Focus:** Enhance automatic documentation generation and prerelease configs

**Status:** Released July 24, 2025

### Previous Major Releases ✅

*   **v1.5 - GitHub Issue #7 Resolution and Navigation Enhancements** (July 19, 2025)
    *   [x] **Support for Massive Dependency Trees**: Enhanced Mermaid configuration with `maxTextSize: 900000000` and `maxEdges: 20000`
    *   [x] **Advanced Zoom Controls**: 50x zoom range with smooth mouse wheel support
    *   [x] **Keyboard Shortcuts**: `Ctrl+R` for reset, `+/-` for zoom, `Ctrl+S` for download

*   **v1.4 - Visual and Theme Enhancements** (July 17, 2025)
    *   [x] Professional minimal and dark themes
    *   [x] Enhanced HTML templates with interactive features
    *   [x] SVG download functionality and improved user experience

*   **v1.3 - User Experience Improvements** (July 9, 2025)
    *   [x] Watch mode functionality with `--watch` flag
    *   [x] Enhanced error handling system with comprehensive guidance
    *   [x] Custom exception classes and validation modules
    *   [x] Comprehensive test coverage and modular organization

*   **Core Foundation** (Earlier versions)
    *   [x] Multiple output formats (HTML and JSON)
    *   [x] Dependency version display with `--show-versions`
    *   [x] Multi-module Maven project support
    *   [x] CI/CD workflows and comprehensive documentation
    *   [x] `--theme` option with multiple built-in themes (default/minimal, dark, light)
## 🔮 Future Development

### Candidate Features for Upcoming Releases

**Philosophy:** Small, practical improvements that provide immediate value to users. Features will be selected based on user feedback, development bandwidth, and priority.

#### Essential CLI Features
*   [ ] **`--quiet` / `-q` flag:** Suppress all console output except errors
    *   **Use Case:** Perfect for CI/CD pipelines and scripted usage
*   [ ] **`--version` / `-v` flag:** Display the current version of the tool
    *   **Use Case:** Essential for any CLI tool, currently missing

#### User Experience Enhancements
*   [ ] **Alternative output filename patterns:** `--timestamp-output` flag to auto-append timestamp
    *   **Use Case:** Useful for version tracking (e.g., `diagram-2025-08-01-143022.html`)
*   [ ] **`--open` flag:** Automatically open generated diagram in default browser
    *   **Implementation:** Platform-agnostic using Python's `webbrowser` module
*   [ ] **Custom title support:** `--title "My Project Dependencies"`
    *   **Use Case:** Personalize diagrams with meaningful project names
*   [ ] **Progress indicators:** Simple feedback during long operations
    *   **Implementation:** "Parsing dependencies..." → "Generating diagram..." → "Done!"

#### Configuration & Customization
*   [ ] **Configuration file support:** `.mvnviz.conf` file for default options
    *   **Use Case:** Avoid typing same flags repeatedly, team consistency
*   [ ] **`--exclude-scopes` option:** Filter out test, provided, or other scopes
*   [ ] **`--max-depth` option:** Limit dependency tree depth for overview mode

#### Output & Analysis Improvements
*   [ ] **Basic dependency statistics:** Show total counts in CLI output and HTML comments

#### Enterprise & Integration Features
*   [ ] **Docker container:** Official container images for CI/CD
*   [ ] **GitHub Actions integration:** Pre-built actions for automated diagram generation

## 🎯 Technical Debt & Maintenance

### Ongoing Improvements
*   **Performance Optimization:** Continuous improvements for larger and more complex projects
*   **Browser Compatibility:** Ensure compatibility with all major browsers and versions
*   **Accessibility:** Enhanced accessibility features for users with disabilities
*   **Documentation:** Comprehensive API documentation and developer guides

### Code Quality
*   **Test Coverage:** Maintain high test coverage with focus on edge cases
*   **Type Safety:** Full type annotation coverage and strict type checking
*   **Security:** Regular security audits and dependency updates
*   **Performance:** Continuous profiling and optimization of critical paths

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
- **Small & Focused:** Features are kept small and manageable for faster delivery
- **Feature Selection:** Features are chosen from the candidate list based on current priorities and available development time

## Contributing

If you're interested in contributing to any of these features, please check out our [CONTRIBUTING.md](CONTRIBUTING.md) file for more information.

---

*Last updated: August 1, 2025*
