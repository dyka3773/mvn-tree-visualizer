# Test Structure Documentation

## Overview
This document describes the organization and structure of our test suite, which has been refactored to follow single-responsibility principles and improve maintainability.

## Test Organization

### Modular Test Structure
We have moved away from monolithic test files containing multiple test classes to focused, single-purpose modules:

#### CLI Tests (`tests/cli/`)
- **`test_version.py`** - Version flag functionality (`--version`, `-v`)
- **`test_quiet.py`** - Quiet mode functionality (`--quiet`, `-q`)  
- **`test_open.py`** - Auto-open browser functionality (`--open`)
- **`test_timestamp.py`** - Timestamp output functionality (`--timestamp-output`)

Each CLI test module contains a single test class focused on one specific CLI feature.

#### Large Diagram Tests (`tests/large_diagrams/`)
- **`test_config.py`** - Mermaid configuration for large diagrams
- **`test_navigation.py`** - Enhanced navigation controls and zoom features
- **`test_compatibility.py`** - Backward compatibility testing
- **`test_errors.py`** - Error handling scenarios

Each large diagram test module contains a single test class focused on one aspect of large diagram support.

### Standalone Test Files
- **`test_github_issue_7.py`** - Specific GitHub issue #7 fix testing (single class)
- **`test_html_output.py`** - HTML output generation testing (function-based tests)
- **`test_json_output.py`** - JSON output generation testing (function-based tests)
- **`test_watch_mode.py`** - File watching mode testing (function-based tests)

## Benefits of Current Structure

1. **Single Responsibility**: Each test file has a clear, focused purpose
2. **Maintainability**: Changes to one feature don't affect tests for other features
3. **Readability**: Easier to find and understand tests for specific functionality
4. **Parallel Testing**: Better support for parallel test execution
5. **Modularity**: Easy to add new feature tests without modifying existing files

## Test Execution

### Run All Tests
```bash
python -m pytest tests/ -v
```

### Run Specific Module Tests
```bash
# CLI functionality tests
python -m pytest tests/cli/ -v

# Large diagram tests  
python -m pytest tests/large_diagrams/ -v

# Specific feature tests
python -m pytest tests/cli/test_open.py -v
```

## Test Count Summary
- **CLI Tests**: 23 tests across 4 modules
- **Large Diagram Tests**: 14 tests across 4 modules  
- **Other Tests**: 31 tests in standalone modules
- **Total**: 68 tests

## Refactoring History
- **Before**: Monolithic files with multiple test classes (e.g., `test_cli.py` with 4 classes)
- **After**: Focused modules with single test classes or related functions
- **Result**: Improved maintainability and clearer test organization
