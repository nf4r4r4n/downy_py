from ui.prompts import Prompt
from rich.pretty import pprint
import questionary
from core.dowloader import Downloader


def main():
    prompt = Prompt()
    config = prompt.collect_config()

    pprint(config, expand_all=True)
    config_is_ok = questionary.confirm(
        "Would you continue with this config?"
    ).ask()

    if config_is_ok:
        downloader = Downloader(config)
        try:
            downloader.download()
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
