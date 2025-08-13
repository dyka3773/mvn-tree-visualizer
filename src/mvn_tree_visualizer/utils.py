import time
from pathlib import Path


def add_timestamp_to_filename(filename: str) -> str:
    """Add timestamp to filename before the extension.

    Args:
        filename: Original filename (e.g., 'diagram.html', 'output.json', 'folder/diagram.html')

    Returns:
        Timestamped filename (e.g., 'diagram-2025-08-13-203045.html')
    """
    timestamp = time.strftime("%Y-%m-%d-%H%M%S")
    path = Path(filename)

    # Handle paths by preserving directory and only modifying the filename
    if path.parent != Path("."):
        # Has a directory component
        directory = path.parent
        stem = path.stem
        suffix = path.suffix
        timestamped_name = f"{stem}-{timestamp}{suffix}"
        return str(directory / timestamped_name)
    else:
        # No directory component
        stem = path.stem
        suffix = path.suffix
        return f"{stem}-{timestamp}{suffix}"
