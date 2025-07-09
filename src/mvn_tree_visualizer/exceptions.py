"""Custom exceptions for mvn-tree-visualizer."""


class MvnTreeVisualizerError(Exception):
    """Base exception for mvn-tree-visualizer errors."""

    pass


class DependencyFileNotFoundError(MvnTreeVisualizerError):
    """Raised when no dependency files are found."""

    pass


class DependencyParsingError(MvnTreeVisualizerError):
    """Raised when there's an error parsing dependency files."""

    pass


class OutputGenerationError(MvnTreeVisualizerError):
    """Raised when there's an error generating output files."""

    pass
