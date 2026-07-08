from agent.llms import mock_llm_json_response
from tools_helpers import tool_router


def run_agent(user_input: str, user_name: str):
    """
    A reusable function that runs the agent

    Agrs:
        user_input (str): The expression or query the tool wil run
        user_name (str) : The name of the current user

    Returns:
        dict: A dictionary containing the selected tool and its response after execution
    """

    # LLM decides which tool to use based on the user input
    selected_tool = mock_llm_json_response(user_input)

    # Execute the selected tool with the provided arguments
    response = tool_router(selected_tool, user_name)

    return {
        "tool_request": selected_tool,
        "response": response,
    }