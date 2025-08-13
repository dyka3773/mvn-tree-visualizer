# Project Roadmap

This document outlines the evolution and future direction of the `mvn-tree-visualizer` project. Major milestones show the progression from a basic tool to an enterprise-ready solution.

## 🎉 Recently Completed ✅

### v1.8.0 - User Experience & Test Architecture Improvements (In Progress)

**Focus:** Practical CLI enhancements and improved maintainability

**Status:** Ready for Release - August 13, 2025

**Completed Features:**
*   [x] **`--open` flag:** Automatically open generated HTML diagrams in default browser
    *   Platform-agnostic implementation using Python's `webbrowser` module
    *   Intelligent handling: only works with HTML output, graceful error handling
    *   Combined functionality with quiet mode and other flags
*   [x] **`--timestamp-output` flag:** Auto-append timestamp to output filenames
    *   Format: `diagram_20250813_143022.html` for version tracking
    *   Works with both HTML and JSON output formats
    *   Perfect for CI/CD and avoiding file overwrites
*   [x] **Comprehensive Test Architecture Refactoring:**
    *   Modular test structure: Split monolithic test files into focused modules
    *   `tests/cli/` - Individual CLI feature testing (version, quiet, open, timestamp)
    *   `tests/large_diagrams/` - Focused large diagram feature testing
    *   Single-responsibility principle: Each test file has one clear purpose
    *   Improved maintainability and parallel test execution support

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

#### User Experience Enhancements
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

*Last updated: August 13, 2025*
