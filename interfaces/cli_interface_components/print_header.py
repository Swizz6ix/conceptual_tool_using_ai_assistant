from datetime import datetime
import sys

from interfaces.cli_interface_components import clear_screen
from interfaces.cli_interface_components.type_print import type_print

print(type(type_print))
print(type_print)


APP_NAME = "Conceptual Tool using AI Assistant!"
VERSION = "1.0.0"

def print_header():
    """
    Displays application banner.
    """
    clear_screen()

    type_print("╔" + "═" * 68 + "╗")
    type_print("║{:^68}║".format(APP_NAME))
    type_print("║{:^68}║".format(f"Version {VERSION}"))
    type_print("╚" + "═" * 68 + "╝")

    type_print(f"Python : {sys.version.split()[0]}")
    type_print(f"Platform: {sys.platform}")
    type_print(f"Date    : {datetime.now():%Y-%m-%d %H:%M:%S}")

    type_print("-" * 70)