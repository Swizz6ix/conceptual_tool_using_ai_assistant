import time

from interfaces.cli_interface_components import type_print


def menu():
    """
    This is the menue of the cli interface.
    """

    type_print("\nChoose an interface:\n")
    time.sleep(0.2)

    type_print("1. Command Line")
    time.sleep(0.2)

    type_print("2. Streamlit Dashboard")
    time.sleep(0.2)

    type_print("3. System check")
    time.sleep(0.2)

    type_print("4. About")
    time.sleep(0.2)

    type_print("5. Run Demo")
    time.sleep(0.2)

    type_print("0. Exit")
    time.sleep(0.2)

    return input("\nPls enter your choice: ").strip()