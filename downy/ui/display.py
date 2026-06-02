"""
Progress display utilities for Downy.

This module provides formatted progress bar creation and display using the Rich library,
showing download progress with speed, ETA, and percentage information.
"""

from rich.progress import (
    Progress,
    BarColumn,
    TextColumn,
    DownloadColumn,
    TransferSpeedColumn,
    TimeRemainingColumn
)


def create_progress() -> Progress:
    """
    Create and configure a Rich Progress display for download tracking.
    
    Constructs a Progress instance with the following columns:
    - Task description (blue text)
    - Progress bar
    - Completion percentage
    - Downloaded bytes/total bytes
    - Download speed
    - Estimated time remaining
    
    Returns:
        Progress: Configured Rich Progress instance ready for displaying download progress.
    
    Example:
        >>> progress = create_progress()
        >>> task_id = progress.add_task("[green]Downloading...", total=100)
        >>> with progress:
        ...     progress.update(task_id, completed=50)
    """
    return Progress(
        TextColumn("[bold blue]{task.description}"),
        BarColumn(),
        "[progress.percentage]{task.percentage:>3.0f}%",
        DownloadColumn(),
        TransferSpeedColumn(),
        TimeRemainingColumn()
    )
