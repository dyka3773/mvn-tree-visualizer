# Test Watch Mode

This directory contains a simple test to demonstrate the watch mode functionality.

## How to Test

1. **Start watch mode:**
   ```bash
   mvn_tree_visualizer --filename test_maven_file --output watch-test.html --watch
   ```

2. **Modify the test file** while the watch is running to see automatic regeneration.

3. **Stop with Ctrl+C** when done testing.

## What to Expect

- Initial diagram generation
- Console message about watching for changes
- Automatic regeneration when the dependency file changes
- Timestamps for each regeneration
- Clean shutdown with Ctrl+C
