# Examples

This directory contains example Maven dependency files and their corresponding outputs to demonstrate the capabilities of mvn-tree-visualizer, including the enhanced features for large dependency trees.

## Simple Project Example

The `simple-project/` directory contains a modern Spring Boot 3.2 web application with:
- **Spring Boot 3.2.0** - Latest stable version with Spring 6.1
- **Apache Commons Lang3** - Utility library
- **JUnit Jupiter 5.10.1** - Modern testing framework

### 📁 Available Examples:
- `diagram-minimal.html` - Clean light theme optimized for readability
- `diagram-dark.html` - Dark theme perfect for low-light environments  
- `dependencies.json` - JSON output for programmatic integration

### 🛠️ Generation Commands:
```bash
cd examples/simple-project

# Generate with different themes
mvn-tree-visualizer --filename maven_dependency_file --output diagram-minimal.html
mvn-tree-visualizer --filename maven_dependency_file --output diagram-dark.html --theme dark

# Generate JSON output for automation
mvn-tree-visualizer --filename maven_dependency_file --output dependencies.json --format json
```

## Complex Project Example

The `complex-project/` directory demonstrates a **real-world enterprise microservice** with extensive dependencies:

- **Spring Boot 3.2.0** with Web, Data JPA, and Actuator
- **Database**: MySQL Connector with Hibernate ORM
- **Monitoring**: Prometheus metrics and Micrometer
- **Utilities**: Google Guava, Apache Commons
- **Testing**: Comprehensive test stack with Testcontainers
- **🎯 Over 100+ dependencies** - Perfect for testing large diagram capabilities!

### 📁 Available Examples:
- `diagram-minimal.html` - Clean visualization with version numbers
- `diagram-dark.html` - Dark theme with complete dependency details

### 🛠️ Generation Commands:
```bash
cd examples/complex-project

# Generate with version numbers (recommended for enterprise projects)
mvn-tree-visualizer --filename maven_dependency_file --output diagram-minimal.html --show-versions
mvn-tree-visualizer --filename maven_dependency_file --output diagram-dark.html --theme dark --show-versions
```

## 🎨 Theme Comparison

### Minimal Theme Features:
- **Clean white background** for presentations and documentation
- **Black text and borders** for high contrast and printing
- **Monospace font** (Monaco/Menlo) for technical readability
- **Optimized spacing** for large dependency trees

### Dark Theme Features:
- **Forest green background** with enhanced visibility fixes
- **White text forced rendering** solves Mermaid.js dark theme issues
- **Perfect for long coding sessions** and low-light environments
- **Enhanced contrast** for better node distinction

## 🔍 Enhanced Navigation Features

Both examples demonstrate the powerful navigation capabilities:

### Zoom Controls:
- **Zoom In/Out Buttons**: `+` and `-` for precise control
- **Reset Button**: `Ctrl+R` to return to full view
- **Mouse Wheel**: Smooth zooming with 0.2 sensitivity
- **Extreme Zoom Range**: 0.01x (full overview) to 50x (detailed inspection)

### Keyboard Shortcuts:
- `Ctrl+R` - Reset zoom and center
- `+` / `=` - Zoom in
- `-` - Zoom out  
- `s` - Download SVG

### Large Diagram Optimizations:
- **No text size limits** - Handles projects with 1000+ dependencies
- **Smooth performance** even with complex enterprise dependency trees
- **Memory efficient** rendering with optimized edge handling

## 🔧 Technical Details

### Mermaid.js Configuration:
```javascript
maxTextSize: 900000000    // Virtually unlimited text rendering
maxEdges: 20000          // Supports massive dependency graphs
minZoom: 0.01           // 100x zoom out for full overview
maxZoom: 50             // 50x zoom in for detailed inspection
```

### Color Coding:
- **🔵 Blue nodes** - Root project dependencies
- **🟠 Orange nodes** - Intermediate dependencies  
- **🟢 Green nodes** - Leaf dependencies (no further deps)

## 📊 Use Cases

### Development Teams:
- **Dependency analysis** and version conflict resolution
- **Architecture reviews** and dependency health checks
- **Documentation** for technical specifications

### Enterprise Projects:
- **Compliance audits** with complete dependency visibility
- **Security analysis** of transitive dependencies
- **Performance optimization** by identifying heavy dependency chains

## 🎯 Getting Started

1. **Generate your dependency file**:
   ```bash
   mvn dependency:tree -DoutputFile=maven_dependency_file -DappendOutput=true
   ```

2. **Create visualizations**:
   ```bash
   # Basic diagram
   mvn-tree-visualizer --filename maven_dependency_file --output diagram.html
   
   # With versions for detailed analysis
   mvn-tree-visualizer --filename maven_dependency_file --output diagram.html --show-versions
   
   # Dark theme for coding sessions
   mvn-tree-visualizer --filename maven_dependency_file --output diagram.html --theme dark
   ```

3. **Open in browser** and explore with enhanced zoom and navigation controls!

## Use Cases

### 1. Quick Dependency Overview
```bash
mvn-tree-visualizer --filename maven_dependency_file --output overview.html
```
- Clean view without version numbers
- Easy to identify dependency relationships

### 2. Detailed Analysis with Versions
```bash
mvn-tree-visualizer --filename maven_dependency_file --output detailed.html --show-versions
```
- Shows all version information
- Useful for debugging version conflicts

### 3. Scripting and Automation
```bash
mvn-tree-visualizer --filename maven_dependency_file --output deps.json --format json
```
- Machine-readable JSON format
- Perfect for CI/CD pipelines and automated analysis

### 4. Multi-module Projects
```bash
mvn-tree-visualizer --directory ./my-project --output multi-module.html
```
- Automatically finds and merges dependency files from subdirectories
- Comprehensive view of entire project structure
