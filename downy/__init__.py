
"""
Downy - Interactive Media Downloader

A command-line tool for downloading audio and video from various online sources
with an interactive interface and progress tracking.
"""

from downy.ui.prompts import Prompt
from downy.core.downloader import Downloader


def main():
    """
    Main application entry point.

    Orchestrates the download workflow:
    1. Prompts user for media URL, type, and format
    2. Creates downloader instance with user configuration
    3. Initiates the download process

    Raises:
        KeyboardInterrupt: When user cancels the operation.
        ValueError: When required configuration is missing.
    """
    prompt = Prompt()
    config = prompt.collect_config()

    downloader = Downloader(config)
    downloader.download()
