import subprocess
import sys
import time

from interfaces.cli_interface_components import (
    menue_exit, print_header, type_print, clear_screen
)
from interfaces import(
    menu, about, run_demo, system_check
)
from launchers import streamlit_launcher, cli_launcher
from interfaces.streamlit_interface_component import spinner


def launcher():
    clear_screen()

    type_print("=" * 71)
    type_print(
        "           Welcome to the Conceptual Tool using AI Assistant!"
    )
    type_print("=" * 71)
    time.sleep(2)

    while True:
        clear_screen()

        spinner("Initializing")
        time.sleep(2)

        print_header()

        choice = menu()

        if choice == "1":
            cli_launcher()

            menue_exit()

        elif choice == "2":
            spinner("Launching Streamlit...")
            time.sleep(0.3)

            streamlit_launcher()

            menue_exit()

        elif choice == "3":
            system_check()

            menue_exit()
        
        elif choice == "4":
            about()

            menue_exit()
        
        elif choice == "5":
            run_demo()

            menue_exit()

        elif choice == "0":
            type_print("\nGoodbye")

            sys.exit()

        else:
            type_print("\nInvalid choice")

            input("Press Enter to continue... ")

if __name__ == "__main__":
    launcher()