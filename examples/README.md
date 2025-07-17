# Examples

This directory contains example Maven dependency files and their corresponding outputs to demonstrate the capabilities of mvn-tree-visualizer.

## Simple Project Example

The `simple-project/` directory contains a basic Maven project with common dependencies:
- Spring Boot Starter Web
- Apache Commons Lang3
- JUnit (test scope)

**Available Examples:**
- `diagram-dark.html` - Dark theme optimized for low-light environments
- `diagram-minimal.html` - Light theme with minimal styling
- `dependencies.json` - JSON output for programmatic use

**To generate outputs:**
```bash
cd examples/simple-project

# Generate with different themes
mvn_tree_visualizer --filename maven_dependency_file --output diagram-minimal.html
mvn_tree_visualizer --filename maven_dependency_file --output diagram-dark.html --theme dark

# Generate JSON output
mvn_tree_visualizer --filename maven_dependency_file --output dependencies.json --format json
```

## Complex Project Example

The `complex-project/` directory contains a more realistic microservice project with:
- Spring Boot Web + Data JPA
- MySQL Connector
- Google Guava
- Comprehensive test dependencies

**Available Examples:**
- `diagram-minimal.html` - Clean minimal theme
- `diagram-dark.html` - Dark theme optimized for low-light environments

**To generate outputs:**
```bash
cd examples/complex-project

# Generate with different themes and versions
mvn_tree_visualizer --filename maven_dependency_file --output diagram-minimal.html --show-versions
mvn_tree_visualizer --filename maven_dependency_file --output diagram-dark.html --theme dark --show-versions
```

## Theme Comparison

You can easily compare all themes by opening the different diagram files:

### Color Scheme (Consistent Across All Themes)
- **Root nodes**: Blue - Your main project dependencies
- **Intermediate nodes**: Orange - Transitive dependencies with children
- **Leaf nodes**: Green - Final dependencies with no children

### Theme Characteristics
- **Default**: Clean minimal design with monospace fonts and simple borders
- **Dark**: Dark backgrounds with bright text, optimized for low-light environments  

## Use Cases

### 1. Quick Dependency Overview
```bash
mvn_tree_visualizer --filename maven_dependency_file --output overview.html
```
- Clean view without version numbers
- Easy to identify dependency relationships

### 2. Detailed Analysis with Versions
```bash
mvn_tree_visualizer --filename maven_dependency_file --output detailed.html --show-versions
```
- Shows all version information
- Useful for debugging version conflicts

### 3. Scripting and Automation
```bash
mvn_tree_visualizer --filename maven_dependency_file --output deps.json --format json
```
- Machine-readable JSON format
- Perfect for CI/CD pipelines and automated analysis

### 4. Multi-module Projects
```bash
mvn_tree_visualizer --directory ./my-project --output multi-module.html
```
- Automatically finds and merges dependency files from subdirectories
- Comprehensive view of entire project structure
