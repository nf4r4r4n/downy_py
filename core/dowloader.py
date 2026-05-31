from yt_dlp import YoutubeDL
from ui.display import create_progress


class Downloader:
    def __init__(self, config: dict = None):
        if config is None:
            print("Config is missing")
            return
        self._config = config
        self._progress = create_progress()
        self._task_id = self._progress.add_task(
            "[green]Downloading...",
            total=100
        )

    def progrss_hook(self, data):
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
                description="[bold green]Processing..."
            )

    def _build_opts(self) -> dict:
        opts = {
            "outtmpl": "downloads/%(title)s.%(ext)s",
            "progress_hooks": [self.progrss_hook],
            "quiet": True,
            "noprogress": True
        }

        if self._config["media_type"] == "audio":
            opts.update({
                "format": "bestaudio/best",
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": self._config["format"],
                        "preferredquality": "192"
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
        opts = self._build_opts()

        with self._progress:
            with YoutubeDL(opts) as ydl:
                ydl.download([self._config["url"]])
