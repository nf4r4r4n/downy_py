import questionary


class Prompt:
    def __init__(self):
        self._url: str = ""
        self._media_type: str = ""
        self._audio_formats: [str] = [
            "mp3",
            "m4a",
            "aac",
            "opus",
            "ogg",
            "vorbis",
            "flac",
            "wav",
            "alac"
        ]
        self._video_formats: [str] = [
            "mp4",
            "webm",
            "mkv",
            "mov",
            "flv",
            "avi"
        ]
        self._format_choices: [str] = []

    def collect_config(self) -> dict:
        self._url = self._ask_url()
        self._media_type = self._ask_media_type()

        if self._media_type == "audio":
            self._format_choices = self._audio_formats[:]
        else:
            self._format_choices = self._video_formats[:]

        format = questionary.select(
            "Choose the format:",
            qmark="\ueab6",
            pointer="\uf4c3",
            choices=self._format_choices
        ).ask()

        return {
            "url": self._url,
            "media_type": self._media_type,
            "format": format
        }

    def _ask_url(self):
        return questionary.text(
            "Enter URL:",
            qmark="\ueab6",
        ).ask()

    def _ask_media_type(self):
        return questionary.select(
            "Choose the media type:",
            qmark="\ueab6",
            pointer="\uf4c3",
            choices=["audio", "video"],
            default="audio"
        ).ask()
