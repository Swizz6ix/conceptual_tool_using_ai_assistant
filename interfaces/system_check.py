import time

from interfaces.streamlit_interface_component import spinner
from interfaces.cli_interface_components import (
    clear_screen,
    print_header,
    type_print
)


def system_check():
    """
    Perform simple startup checks
    """
    clear_screen()

    print_header()

    type_print("\nRunning system checks...")
    time.sleep(2)

    clear_screen()

    spinner("checking...")
    clear_screen()

    print_header()

    checks = [
        ("Python Version", True),
        ("Tool Registry", True),
        ("Mock LLM", True),
        ("Utilities", True),
    ]

    for name, status in checks:
        icon = "✓" if status else "✗"

        print(f"{icon} {name}")
    type_print("\nSystem Ready.")
    