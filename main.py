from utilities.greet import greet
from utilities.stop import stop
from tools_helpers.tool_router import tool_router
from llms.mock_llm import mock_llm_json_response


MAX_ITERATIONS = 5  # Limit the number of iterations to prevent infinite loops
STOP_WORDS = ["exit", "quit", "stop", "bye", "goodbye", "break"]  # Words to stop the application

def app():
    """
    Main application function that runs the conceptual tool using an AI assistant.
    Demonstrating the complete tool-calling workflow with the AI assistant.
    """
    print("=" * 71 )
    print("           Welcome to the Conceptual Tool using AI Assistant!")
    print("=" * 71 )

    user_name = input("Hello, I am your AI assistant. What is your name? ").strip()
    if not user_name:
        user_name = "User"
        
    if user_name.lower() in STOP_WORDS:
        print("Exiting the application. Goodbye!")
        return

    greeting = greet()
    print(f"\n{greeting} {user_name}! I am here to assist you with various tools.")
    print("You can ask me to perform calculations, search the web, get weather information, or summarize text.")
    print("How can I assist you today? (Type 'exit' to quit)")

    iteration_count = 0

    while iteration_count < MAX_ITERATIONS:
        user_input = input(f"\n{user_name}, Pls enter your request (or type 'exit' to quit): ").strip()

        if stop(user_input):
            print(f"Exiting the application. Goodbye! {user_name}")
            print(f"Thank you for using the 'Conceptual Tool Using AI' Assistant, {user_name}!")
            print("Hope to see you again soon!")
            break

        try:
            # LLM decides which tool to use based on the user input
            selected_tool = mock_llm_json_response(user_input)

            print("[Tool Selection]")
            print(selected_tool)

            # Execute the selected tool with the provided arguments
            response = tool_router(selected_tool, user_name)

            print("\n[Tool Execution Result]")
            print(response)
            print()
        
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        iteration_count += 1
    else:
        print(f"Maximum iterations reached. Exiting the application. Goodbye! {user_name}")
        print(f"Thank you for using the 'Conceptual Tool Using AI' Assistant")
        print("let's continue in a new session.")

if __name__ == "__main__":
    app()