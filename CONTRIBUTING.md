# Contributing to mvn-tree-visualizer

First off, thank you for considering contributing to `mvn-tree-visualizer`! It's people like you that make open source so great.

## Where do I go from here?

If you've noticed a bug or have a feature request, [make one](https://github.com/dyka3773/mvn-tree-visualizer/issues/new)! It's generally best if you get confirmation of your bug or approval for your feature request this way before starting to code.

### Fork & create a branch

If this is something you think you can fix, then [fork `mvn-tree-visualizer`](https://github.com/dyka3773/mvn-tree-visualizer/fork) and create a branch with a descriptive name.

A good branch name would be (where issue #123 is the ticket you're working on):

```bash
git checkout -b 123-add-a-feature
```

### Get the code

```bash
git clone https://github.com/your-username/mvn-tree-visualizer.git
cd mvn-tree-visualizer
```

### Set up the development environment

We use `uv` for dependency management. To set up the development environment, run:

```bash
uv sync --dev
```

This will install all the dependencies needed for development, including the ones for running tests.

### Make your changes

Make your changes to the code. Make sure to add tests for your changes!

### Run the tests

To run the tests, run:

```bash
pytest
```

### Commit and push

```bash
git commit -m "Your descriptive commit message"
git push origin 123-add-a-feature
```

### Create a pull request

Go to the GitHub repository and create a pull request.

## Style guide

We use `ruff` for linting and formatting. Please make sure your code conforms to the style guide by running:

```bash
ruff check .
ruff format .
```

## Code of Conduct

We have a [Code of Conduct](CODE_OF_CONDUCT.md), please follow it in all your interactions with the project.
