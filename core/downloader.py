"""
Core download functionality for Downy.

This module handles the actual media downloading process using yt-dlp,
including progress tracking and format conversion.
"""

from yt_dlp import YoutubeDL
from ui.display import create_progress
import config as cfg


class Downloader:
    """
    Handles media downloading with progress tracking.

    This class manages the download workflow including progress reporting,
    format conversion (audio/video), and error handling.

    Attributes:
        _config (dict): Download configuration containing URL, media type, and format.
        _progress (Progress): Rich Progress instance for displaying download progress.
        _task_id (TaskID): ID of the current progress task.
    """

    def __init__(self, config: dict = None):
        """
        Initialize the Downloader with configuration.

        Args:
            config (dict, optional): Configuration dictionary containing:
                - url (str): URL of the media to download
                - media_type (str): Type of media ('audio' or 'video')
                - format (str): Output format (e.g., 'mp3', 'mp4')

        Raises:
            ValueError: If config is None or missing required keys.
        """
        if config is None:
            raise ValueError("Config is missing")
        self._config = config
        self._progress = create_progress()
        self._task_id = self._progress.add_task(
            cfg.PROGRESS_MESSAGE_DOWNLOADING,
            total=100
        )

    def _progress_hook(self, data):
        """
        Callback for yt-dlp progress updates.

        Updates the progress display with download status, percentage, speed, etc.
        Called by yt-dlp during download and post-processing phases.

        Args:
            data (dict): Status dictionary from yt-dlp containing:
                - status (str): Current phase ('downloading' or 'finished')
                - downloaded_bytes (int): Bytes downloaded so far
                - total_bytes (int): Total bytes to download
                - total_bytes_estimate (int): Estimated total if unknown
        """
        status = data.get("status")

        if status == "downloading":
            downloaded = data.get("downloaded_bytes", 0)

            total = (
                data.get("total_bytes")
                or data.get("total_bytes_estimate")
                or 0
            )

            if total > 0:
                self._progress.update(
                    self._task_id,
                    completed=downloaded,
                    total=total
                )

        elif status == "finished":
            self._progress.update(
                self._task_id,
                description=cfg.PROGRESS_MESSAGE_PROCESSING
            )

    def _build_opts(self) -> dict:
        """
        Build yt-dlp options dictionary based on configuration.

        Constructs the complete set of options for yt-dlp including:
        - Output template and format
        - Audio/video specific settings
        - Post-processing (format conversion, codec selection)
        - Progress hooks and extractor arguments

        Returns:
            dict: Complete yt-dlp options dictionary ready for YoutubeDL initialization.
        """
        opts = {
            "outtmpl": cfg.OUTPUT_TEMPLATE,
            "progress_hooks": [self._progress_hook],
            **cfg.YOUTUBE_DL_OPTS,
            "extractor_args": {
                "youtube": {
                    "player_js_version": ["actual"]
                }
            }
        }

        if self._config["media_type"] == "audio":
            opts.update({
                "format": "bestaudio/best",
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": self._config["format"],
                        "preferredquality": cfg.AUDIO_QUALITY
                    }
                ]
            })
        else:
            opts.update({
                "format": "bestvideo+bestaudio/best",
                "merge_output_format": self._config["format"]
            })

        return opts

    def download(self):
        """
        Execute the media download process.

        Builds download options, initializes yt-dlp with progress tracking,
        and downloads the media file(s) from the configured URL. The actual
        download and any format conversion happens within this method.

        Raises:
            Various exceptions from yt-dlp for network issues, format errors, etc.
        """
        opts = self._build_opts()

        with self._progress:
            with YoutubeDL(opts) as ydl:
                ydl.download([self._config["url"]])
