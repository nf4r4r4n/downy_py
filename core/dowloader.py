from yt_dlp import YoutubeDL


class Downloader:
    def __init__(self, config: dict = None):
        if config is None:
            print("Config is missing")
            return
        self._config = config

    def _build_opts(self) -> dict:
        return {
            "outtmpl": "%(title)s.%(ext)s",
            "quiet": False,
            "noprogress": False
        }

    def download(self):
        opts = self._build_opts()

        with YoutubeDL(opts) as ydl:
            ydl.download([self._config["url"]])
