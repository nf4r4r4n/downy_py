from ui.prompts import Prompt
from core.dowloader import Downloader


def main():
    prompt = Prompt()
    config = prompt.collect_config()

    downloader = Downloader(config)
    try:
        downloader.download()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
