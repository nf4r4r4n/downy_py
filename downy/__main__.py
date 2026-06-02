from rich.console import Console
from rich.panel import Panel
from . import main

if __name__ == "__main__":
    console = Console()
    try:
        main()
    except KeyboardInterrupt:
        console.print(
            Panel.fit(
                "[bold yellow]Download cancelled.[/bold yellow]",
                border_style="yellow"
            )
        )
    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
