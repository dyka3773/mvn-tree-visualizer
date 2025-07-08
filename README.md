# Maven Dependency Tree Visualizer

[![PyPI version](https://badge.fury.io/py/mvn-tree-visualizer.svg)](https://badge.fury.io/py/mvn-tree-visualizer)

A simple command-line tool to visualize the dependency tree of a Maven project in a graphical and interactive format.

This tool was born out of the frustration of not being able to easily visualize the dependency tree of a Maven project. The `mvn dependency:tree` command is great, but the output can be hard to read, especially for large projects. This tool aims to solve that problem by providing a simple way to generate an interactive diagram of the dependency tree.

## Features

*   **Interactive Diagrams:** Generates an interactive HTML diagram of your dependency tree using Mermaid.js.
*   **Easy to Use:** A simple command-line interface that gets the job done with minimal configuration.
*   **File Merging:** Automatically finds and merges multiple `maven_dependency_file` files from different subdirectories.
*   **Customizable Output:** Specify the output file name and location.
*   **SVG Export:** Download the generated diagram as an SVG file directly from the HTML page.

## How to Use

1.  **Generate the dependency file:**
    Run the following command in your terminal at the root of your Maven project. This will generate a file named `maven_dependency_file` in each module's `target` directory.

    ```bash
    mvn dependency:tree -DoutputFile=maven_dependency_file -DappendOutput=true
    ```
    > You can add other options like `-Dincludes="org.example"` to filter the dependencies.

2.  **Visualize the dependency tree:**
    Use the `mvn-tree-visualizer` command to generate the diagram.

    ```bash
    mvn_tree_visualizer --filename "maven_dependency_file" --output "diagram.html"
    ```

3.  **View the diagram:**
    Open the generated `diagram.html` file in your web browser to view the interactive dependency tree.

## Options

*   `--filename`: The name of the file containing the Maven dependency tree. Defaults to `maven_dependency_file`.
*   `--output`: The name of the output HTML file. Defaults to `diagram.html`.
*   `--directory`: The directory to scan for the Maven dependency file(s). Defaults to the current directory.
*   `--keep-tree`: Keep the intermediate `dependency_tree.txt` file after generating the diagram. Defaults to `False`.
*   `--help`: Show the help message and exit.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

Please read our [CONTRIBUTING.md](CONTRIBUTING.md) file for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.