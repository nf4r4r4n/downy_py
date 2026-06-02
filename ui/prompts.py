"""
User interface prompts for Downy.

This module handles interactive user prompts for collecting download configuration
including media URL, type (audio/video), and output format selection.
"""

import questionary
import config


class Prompt:
    """
    Interactive prompt manager for collecting download configuration.
    
    Guides the user through selecting media URL, media type (audio/video),
    and output format. Manages format options dynamically based on media type selection.
    
    Attributes:
        _url (str): User-provided media URL.
        _media_type (str): Selected media type ('audio' or 'video').
        _audio_formats (list[str]): Available audio format options.
        _video_formats (list[str]): Available video format options.
        _format_choices (list[str]): Active format choices based on media type.
    """
    def __init__(self):
        """
        Initialize the Prompt manager with default values and available formats.
        
        Sets up initial state with empty URL/media_type and loads supported
        audio/video formats from configuration.
        """
        self._url: str = ""
        self._media_type: str = ""
        self._audio_formats: list[str] = config.AUDIO_FORMATS
        self._video_formats: list[str] = config.VIDEO_FORMATS
        self._format_choices: list[str] = []

    def collect_config(self) -> dict:
        """
        Collect complete download configuration from the user.
        
        Interactively prompts for:
        1. Media URL
        2. Media type (audio or video)
        3. Output format (based on selected media type)
        
        Returns:
            dict: Configuration dictionary with keys:
                - url (str): Media source URL
                - media_type (str): 'audio' or 'video'
                - format (str): Output format (e.g., 'mp3', 'mp4')
        
        Raises:
            KeyboardInterrupt: When user cancels any prompt.
        """
        self._url = self._ask_url()
        self._media_type = self._ask_media_type()

        if self._media_type == "audio":
            self._format_choices = self._audio_formats[:]
        else:
            self._format_choices = self._video_formats[:]

        format = questionary.select(
            "Choose the format:",
            qmark=config.ICON_PROMPT,
            pointer=config.ICON_POINTER,
            choices=self._format_choices
        ).ask()

        if format is None:
            raise KeyboardInterrupt

        return {
            "url": self._url,
            "media_type": self._media_type,
            "format": format
        }

    def _ask_url(self) -> str:
        """
        Prompt user for the media URL.
        
        Displays an interactive text input field for the user to enter
        the URL of the media to download.
        
        Returns:
            str: The media URL provided by the user.
        
        Raises:
            KeyboardInterrupt: When user cancels the prompt.
        """
        result = questionary.text(
            "Enter URL:",
            qmark=config.ICON_PROMPT,
        ).ask()

        if result is None:
            raise KeyboardInterrupt

        return result

    def _ask_media_type(self) -> str:
        """
        Prompt user to select media type.
        
        Displays a selection menu for choosing between audio or video download.
        Defaults to 'audio' if no choice is made.
        
        Returns:
            str: Selected media type - either 'audio' or 'video'.
        
        Raises:
            KeyboardInterrupt: When user cancels the prompt.
        """
        result = questionary.select(
            "Choose the media type:",
            qmark=config.ICON_PROMPT,
            pointer=config.ICON_POINTER,
            choices=["audio", "video"],
            default="audio"
        ).ask()

        if result is None:
            raise KeyboardInterrupt

        return result
