# CLI Tests

This directory contains modular tests for CLI functionality. Each file focuses on a specific CLI feature or flag, making tests easier to maintain and understand.

## Structure

```
tests/cli/
├── __init__.py              # Package initialization
├── test_version.py          # Tests for --version/-v flag
├── test_quiet.py            # Tests for --quiet/-q flag  
├── test_open.py             # Tests for --open flag
└── test_timestamp.py        # Tests for --timestamp-output flag
```

## Test Organization

### `test_version.py`
- Tests version string formatting and validation
- Tests both `--version` and `-v` flags
- Tests version precedence over other arguments
- Tests edge cases like package not found

### `test_quiet.py`
- Tests output suppression with `--quiet`/`-q` flags
- Tests that errors still show in quiet mode
- Tests normal vs quiet behavior comparison

### `test_open.py`
- Tests automatic browser opening with `--open` flag
- Tests HTML vs JSON format behavior
- Tests quiet mode interaction
- Tests error handling for browser failures

### `test_timestamp.py`
- Tests timestamp filename generation with `--timestamp-output`
- Tests format consistency and path handling
- Tests interaction with other flags
- Tests both HTML and JSON output formats

## Benefits of This Structure

1. **Single Responsibility**: Each file tests one specific feature
2. **Easy Navigation**: Developers can quickly find tests for a specific flag
3. **Maintainable**: Changes to one feature don't affect other test files
4. **Modular**: Can run tests for specific features independently
5. **Clear Naming**: File names clearly indicate what functionality is tested

## Running Tests

```bash
# Run all CLI tests
pytest tests/cli/ -v

# Run specific feature tests
pytest tests/cli/test_version.py -v
pytest tests/cli/test_open.py -v

# Run specific test class
pytest tests/cli/test_version.py::TestVersionFlag -v
```
