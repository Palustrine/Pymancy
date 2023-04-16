from rich.console import Console
from rich.theme import Theme
console = Console()

#test_theme = Theme({})
console.print([1, 2, 3])
console.print("[blue underline]Looks like a link")
console.print(locals())
console.print("FOO", style="white on blue")