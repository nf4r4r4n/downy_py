from ui.prompts import Prompt
from core.downloader import Downloader
from rich.pretty import pprint


def main():
    prompt = Prompt()
    config = prompt.collect_config()
    pprint(config, expand_all=True)

    downloader = Downloader(config)
    downloader.download()


if __name__ == "__main__":
    main()
