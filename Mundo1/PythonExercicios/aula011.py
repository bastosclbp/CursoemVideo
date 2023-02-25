from rich import print
from rich.console import Console
console = Console()
console.print("Hello", "World!", style="bold red")
console.print(
    "Where there is a [bold cyan]Will[/bold cyan] there [u]is[/u] a [i]way[/i].")
