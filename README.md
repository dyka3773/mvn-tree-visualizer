# mvn-tree-visualizer

This project provides a simple command line tool to visualize the dependency tree of a Maven project in a graphical format.

## How to Use
1. Run the following command in your terminal to generate the dependency tree and save it to a file:
   ```bash
   mvn dependency:tree -DoutputFile=maven_dependency_file -DappendOutput=true
   ```
   > Feel free to add other options to the command as needed. eg `-Dincludes="org.example"`
2. Use the `mvn-tree-visualizer` command to visualize the dependency tree:
   ```bash
    python -m mvn_tree_visualizer --filename "maven_dependency_file" --output "diagram.html"
    ```
3. Open the generated `diagram.html` file in your web browser to view the dependency tree.

## Options
- `--filename`: The name of the file containing the Maven dependency tree. Default is `maven_dependency_file`.
- `--output`: The name of the output HTML file. Default is `diagram.html`.
- `--directory`: The directory to scan for the Maven dependency file(s). Default is the current directory.
- `--keep-tree`: Keep the tree structure file when processing is complete in the same directory as the output file. Default is false.
- `--help`: Show help message and exit.

