from tools_helpers.tool_router import tool_router
from llms.mock_llm import mock_llm_json_response


def app():
    """
    Main application function that runs the conceptual tool using an AI assistant.
    Demonstrating the complete tool-calling workflow with the AI assistant.
    """
    print("=" * 71 )
    print("           Welcome to the Conceptual Tool using AI Assistant!")
    print("=" * 71 )

    while True:
        user_input = input("\nEnter your request (or type 'exit' to quit): ").strip()

        if user_input.lower() == 'exit':
            print("Exiting the application. Goodbye!")
            break

        try:
            # LLM decides which tool to use based on the user input
            selected_tool = mock_llm_json_response(user_input)
            print("[Tool Selection]")
            print(selected_tool)

            # Execute the selected tool with the provided arguments
            response = tool_router(selected_tool)

            print("\n[Tool Execution Result]")
            print(response)
            print()
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    app()