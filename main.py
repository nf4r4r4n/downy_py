from ui.prompts import Prompt
from rich.pretty import pprint


def main():
    prompt = Prompt()
    config = prompt.collect_config()
    pprint(config, expand_all=True)


if __name__ == "__main__":
    main()
