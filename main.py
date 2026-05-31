from ui.prompts import Prompt
from core.dowloader import Downloader
from rich.panel import Panel
from rich.console import Console

console = Console()


def main():
    prompt = Prompt()
    config = prompt.collect_config()

    downloader = Downloader(config)
    downloader.download()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print(
            Panel.fit(
                "[bold yellow]Download cancelled.[/bold yellow]",
                border_style="yellow"
            )
        )
