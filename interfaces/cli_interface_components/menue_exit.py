import sys

from interfaces.cli_interface_components.type_print import type_print


def menue_exit():
    type_print("\nPress '0' to exit\n")
    type_print("         or")
    type_print("\nPress Enter to return to the launcher\n")

    close = input("\n#... ")
    if close == "0":
        sys.exit()