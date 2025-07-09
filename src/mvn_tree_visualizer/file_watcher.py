"""File watcher functionality for monitoring Maven dependency files."""

import time
from typing import Callable

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class DependencyFileHandler(FileSystemEventHandler):
    """Handler for file system events to trigger diagram regeneration."""

    def __init__(
        self,
        filename: str,
        callback: Callable[[], None],
    ):
        """Initialize the file handler.

        Args:
            filename: Name of the file to monitor for changes
            callback: Function to call when file changes are detected
        """
        self.filename = filename
        self.callback = callback

    def on_modified(self, event):
        """Handle file modification events."""
        if not event.is_directory and event.src_path.endswith(self.filename):
            print(f"Detected change in {event.src_path}")
            self.callback()


class FileWatcher:
    """File system watcher for monitoring Maven dependency files."""

    def __init__(self, directory: str, filename: str, callback: Callable[[], None]):
        """Initialize the file watcher.

        Args:
            directory: Directory to watch for file changes
            filename: Name of the file to monitor
            callback: Function to call when file changes are detected
        """
        self.directory = directory
        self.filename = filename
        self.callback = callback
        self.observer = Observer()
        self.event_handler = DependencyFileHandler(filename, callback)

    def start(self) -> None:
        """Start watching for file changes."""
        print(f"Watching for changes in '{self.filename}' files in '{self.directory}'...")
        print("Press Ctrl+C to stop watching.")

        self.observer.schedule(self.event_handler, self.directory, recursive=True)
        self.observer.start()

    def stop(self) -> None:
        """Stop watching for file changes."""
        print("\nStopping file watcher...")
        self.observer.stop()
        self.observer.join()

    def wait(self) -> None:
        """Wait for file changes (blocking)."""
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()
