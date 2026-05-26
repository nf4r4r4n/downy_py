from yt_dlp import YoutubeDL
from ui.prompts import Config


class Downloader:
    def __init__(self, config: Config):
        self._config: Config = config

    def build_options(self) -> dict:
        return {
            "outtmpl": "%(title)s.%(ext)",
            "quiet": False,
            "noprogress": False,
        }

    def download(self):
        options = self.build_options()

        with YoutubeDL(options) as ydl:
            ydl.download([self._config.url])
