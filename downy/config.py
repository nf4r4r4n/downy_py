"""
Configuration constants for Downy - Media Downloader

This module contains all hardcoded configuration values used throughout the application.
Centralizing configuration makes it easier to customize behavior and maintain consistency.
"""

# Output configuration
OUTPUT_TEMPLATE = "downloads/%(title)s.%(ext)s"

# YoutubeDL options
YOUTUBE_DL_OPTS = {
    "quiet": True,
    "noprogress": True,
    "jsc_executable": "node",
}

# Audio quality settings
AUDIO_QUALITY = "192"  # kbps

# Supported formats
AUDIO_FORMATS = ["aac", "flac", "mp3", "m4a", "opus", "vorbis", "wav"]
VIDEO_FORMATS = ["mkv", "mp4"]

# UI icons (Nerd Font)
ICON_PROMPT = "\ueab6"      # Prompt icon
ICON_POINTER = "\uf4c3"     # Pointer/selection icon

# Progress display
PROGRESS_MESSAGE_DOWNLOADING = "[green]Downloading..."
PROGRESS_MESSAGE_PROCESSING = "[bold green]Processing..."
