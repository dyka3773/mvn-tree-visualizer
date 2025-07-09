# Integration Guide

This guide covers how to integrate mvn-tree-visualizer into your development workflow, CI/CD pipelines, and automation scripts.

## CI/CD Integration

### GitHub Actions

Add dependency visualization to your GitHub Actions workflow:

```yaml
name: Dependency Visualization
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  visualize-dependencies:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.13'
    
    - name: Install mvn-tree-visualizer
      run: pip install mvn-tree-visualizer
    
    - name: Generate dependency tree
      run: mvn dependency:tree -DoutputFile=maven_dependency_file
    
    - name: Create dependency visualization
      run: |
        mvn_tree_visualizer --filename maven_dependency_file --output dependencies.json --format json
        mvn_tree_visualizer --filename maven_dependency_file --output dependencies.html
    
    - name: Upload artifacts
      uses: actions/upload-artifact@v3
      with:
        name: dependency-visualizations
        path: |
          dependencies.json
          dependencies.html
```

### Jenkins

```groovy
pipeline {
    agent any
    
    stages {
        stage('Generate Dependencies') {
            steps {
                sh 'mvn dependency:tree -DoutputFile=maven_dependency_file'
                sh 'pip install mvn-tree-visualizer'
                sh 'mvn_tree_visualizer --filename maven_dependency_file --output dependencies.json --format json'
            }
        }
        
        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'dependencies.json', fingerprint: true
            }
        }
    }
}
```

## Automation Scripts

### Python Script Example

```python
import subprocess
import json
import os

def analyze_dependencies(project_path):
    """Analyze Maven dependencies for a project."""
    
    # Generate Maven dependency tree
    subprocess.run([
        'mvn', 'dependency:tree', 
        '-DoutputFile=maven_dependency_file'
    ], cwd=project_path, check=True)
    
    # Generate JSON output
    subprocess.run([
        'mvn_tree_visualizer', 
        '--filename', 'maven_dependency_file',
        '--output', 'dependencies.json',
        '--format', 'json'
    ], cwd=project_path, check=True)
    
    # Load and process JSON
    with open(os.path.join(project_path, 'dependencies.json'), 'r') as f:
        deps = json.load(f)
    
    return deps

# Usage
deps = analyze_dependencies('/path/to/project')
print(f"Project has {len(deps.get('children', []))} direct dependencies")
```

### Shell Script Example

```bash
#!/bin/bash
# analyze_dependencies.sh

PROJECT_DIR=${1:-"."}
OUTPUT_DIR=${2:-"./dependency-analysis"}

echo "Analyzing dependencies for project in: $PROJECT_DIR"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Generate Maven dependency tree
cd "$PROJECT_DIR"
mvn dependency:tree -DoutputFile=maven_dependency_file

# Generate visualizations
mvn_tree_visualizer --filename maven_dependency_file --output "$OUTPUT_DIR/dependencies.html"
mvn_tree_visualizer --filename maven_dependency_file --output "$OUTPUT_DIR/dependencies.json" --format json
mvn_tree_visualizer --filename maven_dependency_file --output "$OUTPUT_DIR/dependencies-with-versions.json" --format json --show-versions

echo "Analysis complete! Check $OUTPUT_DIR for results."
```

## JSON Output Processing

### Analyzing Dependencies

```python
import json

def count_dependencies(json_file):
    """Count total dependencies in the tree."""
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    def count_recursive(node):
        count = 1  # Count current node
        for child in node.get('children', []):
            count += count_recursive(child)
        return count
    
    return count_recursive(data) - 1  # Exclude root

def find_dependency(json_file, dependency_name):
    """Find all occurrences of a dependency."""
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    found = []
    
    def search_recursive(node, path=[]):
        if dependency_name in node['id']:
            found.append({
                'id': node['id'],
                'path': path + [node['id']]
            })
        
        for child in node.get('children', []):
            search_recursive(child, path + [node['id']])
    
    search_recursive(data)
    return found

# Usage
total_deps = count_dependencies('dependencies.json')
spring_deps = find_dependency('dependencies.json', 'spring')
```

### Generating Reports

```python
def generate_dependency_report(json_file, output_file):
    """Generate a markdown report from dependency JSON."""
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    report = []
    report.append(f"# Dependency Report for {data['id']}")
    report.append("")
    
    def analyze_level(node, level=0):
        indent = "  " * level
        report.append(f"{indent}- {node['id']}")
        
        for child in node.get('children', []):
            analyze_level(child, level + 1)
    
    analyze_level(data)
    
    with open(output_file, 'w') as f:
        f.write('\n'.join(report))

# Usage
generate_dependency_report('dependencies.json', 'dependency-report.md')
```

## Docker Integration

### Dockerfile Example

```dockerfile
FROM maven:3.8-openjdk-17 AS maven-deps
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:tree -DoutputFile=maven_dependency_file

FROM python:3.13-slim AS visualizer
RUN pip install mvn-tree-visualizer
COPY --from=maven-deps /app/maven_dependency_file .
RUN mvn_tree_visualizer --filename maven_dependency_file --output dependencies.json --format json

FROM nginx:alpine
COPY --from=visualizer /dependencies.json /usr/share/nginx/html/
```

## Best Practices

1. **Version Control**: Include dependency visualizations in your CI/CD but not in version control
2. **Performance**: Use JSON format for large projects and automated processing
3. **Security**: Sanitize dependency file content when processing in automated systems
4. **Monitoring**: Track dependency changes over time using the JSON output
5. **Documentation**: Include dependency diagrams in your project documentation

## Advanced Use Cases

### Dependency Diff Analysis

```python
def compare_dependencies(old_json, new_json):
    """Compare two dependency JSON files."""
    # Implementation for comparing dependency changes
    pass
```

### Multi-project Analysis

```bash
# Analyze all Maven projects in a directory
find . -name "pom.xml" -exec dirname {} \; | while read project; do
    echo "Processing $project"
    cd "$project"
    mvn dependency:tree -DoutputFile=maven_dependency_file
    mvn_tree_visualizer --filename maven_dependency_file --output "../analysis/$(basename $project).json" --format json
    cd - > /dev/null
done
```

This integration guide helps you incorporate mvn-tree-visualizer into your development workflow for better dependency management and visualization.
