from yt_dlp import YoutubeDL


class Downloader:
    def __init__(self, config: dict = None):
        if config is None:
            print("Config is missing")
            return
        self._config = config

    def _build_opts(self) -> dict:
        opts = {
            "outtmpl": "downloads/%(title)s.%(ext)s",
            "quiet": False,
            "noprogress": False
        }

        if self._config["media_type"] == "audio":
            opts["format"] = "bestaudio/best"
            opts["postprocessors"] = [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": self._config["format"],
                    "preferredquality": "192"
                }
            ]
        else:
            opts["format"] = "bestvideo+bestaudio/best"
            opts["merge_output_format"] = self._config["format"]
            opts["postprocessors"] = []

        return opts

    def download(self):
        opts = self._build_opts()

        with YoutubeDL(opts) as ydl:
            ydl.download([self._config["url"]])
