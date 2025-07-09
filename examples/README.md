# Examples

This directory contains example Maven dependency files and their corresponding outputs to demonstrate the capabilities of mvn-tree-visualizer.

## Simple Project Example

The `simple-project/` directory contains a basic Maven project with common dependencies:
- Spring Boot Starter Web
- Apache Commons Lang3
- JUnit (test scope)

**To generate outputs:**
```bash
cd examples/simple-project
mvn_tree_visualizer --filename maven_dependency_file --output diagram.html
mvn_tree_visualizer --filename maven_dependency_file --output dependencies.json --format json
```

## Complex Project Example

The `complex-project/` directory contains a more realistic microservice project with:
- Spring Boot Web + Data JPA
- MySQL Connector
- Google Guava
- Comprehensive test dependencies

**To generate outputs:**
```bash
cd examples/complex-project
mvn_tree_visualizer --filename maven_dependency_file --output diagram.html --show-versions
mvn_tree_visualizer --filename maven_dependency_file --output dependencies.json --format json --show-versions
```

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
