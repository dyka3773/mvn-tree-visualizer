# Maven Dependency Tree Visualizer

[![PyPI version](https://badge.fury.io/py/mvn-tree-visualizer.svg)](https://badge.fury.io/py/mvn-tree-visualizer)
![Python](https://img.shields.io/badge/python-3.13+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
[![Downloads](https://pepy.tech/badge/mvn-tree-visualizer)](https://pepy.tech/project/mvn-tree-visualizer)
[![CI](https://github.com/dyka3773/mvn-tree-visualizer/workflows/CI/badge.svg)](https://github.com/dyka3773/mvn-tree-visualizer/actions)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)

A simple command-line tool to visualize the dependency tree of a Maven project in a graphical and interactive format.

This tool was born out of the frustration of not being able to easily visualize the dependency tree of a Maven project. The `mvn dependency:tree` command is great, but the output can be hard to read, especially for large projects. This tool aims to solve that problem by providing a simple way to generate an interactive diagram or a structured JSON output of the dependency tree.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Examples](#examples)
- [Options](#options)
- [Performance](#performance)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Installation

Install the package from PyPI:

```bash
pip install mvn-tree-visualizer
```

## Features

- **🌐 Multiple Output Formats:**
  - **HTML:** Generates an interactive HTML diagram of your dependency tree using Mermaid.js.
  - **JSON:** Creates a structured JSON representation of the dependency tree, perfect for scripting or integration with other tools.
- **🔄 Watch Mode:** Automatically regenerates diagrams when Maven dependency files change using the `--watch` flag.
- **📋 Version Display:** Show or hide dependency versions in both HTML and JSON outputs using the `--show-versions` flag.
- **⚡ Easy to Use:** A simple command-line interface that gets the job done with minimal configuration.
- **📂 File Merging:** Automatically finds and merges multiple `maven_dependency_file` files from different subdirectories.
- **🎨 Customizable Output:** Specify the output file name and location.
- **💾 SVG Export:** Download the generated diagram as an SVG file directly from the HTML page.

## How to Use

### Step 1: Generate the dependency file

Run the following command in your terminal at the root of your Maven project. This will generate a file named `maven_dependency_file` in each module's `target` directory.

```bash
mvn dependency:tree -DoutputFile=maven_dependency_file -DappendOutput=true
```

> **💡 Tip:** You can add other options like `-Dincludes="org.example"` to filter the dependencies.

### Step 2: Visualize the dependency tree

Use the `mvn-tree-visualizer` command to generate the diagram.

#### HTML Output (Interactive Diagram)
```bash
mvn_tree_visualizer --filename "maven_dependency_file" --output "diagram.html" --format html
```

#### JSON Output (Structured Data)
```bash
mvn_tree_visualizer --filename "maven_dependency_file" --output "dependencies.json" --format json
```

#### With Version Information
```bash
mvn_tree_visualizer --filename "maven_dependency_file" --output "diagram.html" --show-versions
```

#### JSON Output with Versions
```bash
mvn_tree_visualizer --filename "maven_dependency_file" --output "dependencies.json" --format json --show-versions
```

#### Watch Mode (Auto-regeneration)
```bash
mvn_tree_visualizer --filename "maven_dependency_file" --output "diagram.html" --watch
```

> **💡 Tip:** In watch mode, the tool will monitor for changes to your Maven dependency files and automatically regenerate the diagram. Perfect for development workflows! Press `Ctrl+C` to stop watching.

### Step 3: View the output

- **HTML:** Open the generated `diagram.html` file in your web browser to view the interactive dependency tree.
- **JSON:** Use the `dependencies.json` file in your scripts or other tools.

## Examples

Check out the [`examples/`](examples/) directory for sample Maven dependency files and their outputs:

- **Simple Project**: Basic Spring Boot application with common dependencies
- **Complex Project**: Realistic microservice with comprehensive dependencies

Each example includes:
- Sample Maven dependency tree file
- Generated HTML and JSON outputs
- Usage instructions

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--filename` | The name of the file containing the Maven dependency tree | `maven_dependency_file` |
| `--output` | The name of the output file | `diagram.html` |
| `--format` | The output format (`html` or `json`) | `html` |
| `--show-versions` | Show dependency versions in the diagram | `False` |
| `--watch` | Watch for file changes and auto-regenerate diagram | `False` |
| `--directory` | The directory to scan for the Maven dependency file(s) | current directory |
| `--keep-tree` | Keep the intermediate `dependency_tree.txt` file | `False` |
| `--help` | Show the help message and exit | - |

## Performance

**For Large Projects:**
- Consider filtering dependencies at the Maven level using `-Dincludes` or `-Dexcludes` parameters
- The tool can handle projects with hundreds of dependencies efficiently

**Memory Usage:**
- Memory usage scales with the number of dependencies
- Typical projects (50-200 dependencies) use minimal memory
- Very large projects (1000+ dependencies) may require more memory

## Troubleshooting

### Common Issues

**"No dependency files found"**
- The tool now provides detailed guidance including:
  - Exact directory searched and filename expected
  - Maven commands to generate dependency files
  - Instructions to ensure you're in a directory with pom.xml

**"Empty or invalid output"**
- Enhanced error messages now include:
  - Specific error details (encoding, permissions, empty files)
  - Validation of file content and format
  - Suggestions for fixing common parsing issues

**"Browser doesn't display the diagram"**
- Ensure you're opening the HTML file in a modern browser
- Check browser console for JavaScript errors
- Try a different browser (Chrome, Firefox, Safari)

**"Permission denied errors"**
- Improved diagnostics for:
  - Directory read/write permissions
  - File access issues
  - Output directory creation problems

### Getting Help

- Check the [examples](examples/) directory for working samples
- Review the [issues](https://github.com/dyka3773/mvn-tree-visualizer/issues) page
- Create a new issue with your Maven dependency file sample

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

Please read our [CONTRIBUTING.md](CONTRIBUTING.md) file for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
