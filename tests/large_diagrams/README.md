# Large Diagrams Tests

This directory contains modular tests for large diagram support features. Each file focuses on a specific aspect of the large diagram functionality.

## Structure

```
tests/large_diagrams/
├── __init__.py              # Package initialization
├── test_config.py           # Tests for Mermaid configuration limits
├── test_navigation.py       # Tests for enhanced UI navigation features
├── test_compatibility.py    # Tests for backward compatibility
└── test_errors.py           # Tests for error handling and edge cases
```

## Test Organization

### `test_config.py`
- Tests Mermaid configuration for large projects
- Tests maxTextSize and maxEdges limits
- Tests theme-specific configurations
- Tests that all themes support large diagrams

### `test_navigation.py`
- Tests enhanced zoom controls (buttons and keyboard shortcuts)
- Tests improved zoom configuration and limits
- Tests pan and zoom error handling
- Tests UI control organization
- Tests that navigation features work across themes

### `test_compatibility.py`
- Tests that existing download functionality is preserved
- Tests that existing Mermaid config is maintained
- Tests that dark theme fixes are preserved
- Ensures new features don't break existing functionality

### `test_errors.py`
- Tests error handling for invalid themes
- Tests Mermaid configuration structure validation
- Tests edge cases and fallback behavior
- Tests that error scenarios still include enhancements

## Benefits of This Structure

1. **Logical Separation**: Each file tests a different aspect of large diagram support
2. **Focused Testing**: Configuration, navigation, compatibility, and errors are separate concerns
3. **Maintainable**: Changes to navigation don't affect configuration tests
4. **Clear Purpose**: File names clearly indicate what aspect is being tested
5. **Modular Execution**: Can run tests for specific aspects independently

## Running Tests

```bash
# Run all large diagram tests
pytest tests/large_diagrams/ -v

# Run specific aspect tests
pytest tests/large_diagrams/test_config.py -v
pytest tests/large_diagrams/test_navigation.py -v

# Run specific test class
pytest tests/large_diagrams/test_config.py::TestLargeDiagramSupport -v
```
