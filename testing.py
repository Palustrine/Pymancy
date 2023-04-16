import random
import datetime
from time import sleep
from rich import print
from rich.panel import Panel
from rich.console import Console
from rich.layout import Layout
from colorama import just_fix_windows_console


just_fix_windows_console()
console = Console()
layout = Layout()

console.print("This style is bold", style="bold")
layout.split_column(Layout(name="upper"), Layout(name="lower"))
layout["lower"].split_row(Layout(name="left"), Layout(name="middle"), Layout(name="right"))
layout["middle"].split(Panel("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"))
print(layout)

# wahoo
'''exp = list(range(0,100,2))
with console.status("Levelling Up......", spinner='star2') as status:
    while exp:
        expx = exp.pop(0)
        sleep(1)
        console.log(f"[yellow]Levelled Up!!!!! {expx}")
    console.log(f"[green]Level 100")'''

class LoadingBar():
    # class for making loading bars and shit yaya
    def __init__(self):
        pass