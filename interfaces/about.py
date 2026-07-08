from interfaces.cli_interface_components import type_print
from interfaces.cli_interface_components import (
    print_header, clear_screen
)

def about():
    """
    Prints the about of the APP
    """
    clear_screen()

    print_header()

    type_print("     ABOUT")
    type_print("=" * 20)

    type_print(
        """
              TOOLS
        --------------------

        ✓ Calculator Tool

        ✓ Weather Tool

        ✓ Web Search Tool

        ✓ Text Summarizer
        """
    )

    type_print(

        """
        Application Features
        --------------------

        ✓ Tools

        ✓ Mock LLM Tool Calling

        ✓ Tool Router

        ✓ Validation Layer

        ✓ Retry Decorator

        ✓ Exponential Backoff

        ✓ Dead Letter Queue

        ✓ Timeout Decorator

        ✓ Cache Decorator

        ✓ Streamlit Dashboard

        ✓ Command-Line Interface
        """
    )

    type_print(
        """
            Architecture
        -------------------

             User
              │
              ▼
            Mock LLM
              │
              ▼
         JSON Tool Call
              │
              ▼
          Validation
              │
              ▼
          Tool Router
              │
              ▼
          Tool Executor
              │
              ▼
             Tool
              │
              ▼
          Response Formatter
        """
    )