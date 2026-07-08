import time

from interfaces.cli_interface_components import (clear_screen, type_print)
from interfaces.streamlit_interface_component import spinner


def run_demo():
    """
    Runs the demo version of the Conceptual AI Agent
    """
    clear_screen()

    type_print("You: calculate 25 * 16")
    spinner("thinking...")
    time.sleep(2)

    print()
    type_print("Assistant: ")
    type_print("400")
    time.sleep(2)

    clear_screen()

    type_print("You: What is the weather like in PortHarcourt")
    spinner("thinking...")
    time.sleep(2)

    print()
    type_print("Assistant: ")
    type_print("here is the weather information in PortHarcourt is...")
    time.sleep(2)

    clear_screen()

    type_print("summarize the following text:...")
    spinner("thinking...")
    time.sleep(2)

    print()
    type_print("Assistant: ")
    type_print("here is the summary of the text:...")
    time.sleep(2)

    clear_screen()

    type_print("what is python?")
    spinner("thinking...")
    time.sleep(2)

    print()
    type_print("Assistant: ")
    type_print("here are the search results for your query...")
    time.sleep(2)

    clear_screen()
