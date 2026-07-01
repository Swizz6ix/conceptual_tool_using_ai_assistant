import json

from utilities.validate_request import validate_request
from tools_helpers.tool_executor import tool_executor
from llms.mock_llm import mock_llm_tool_response


def tool_router(query: dict, user_name: str) -> str:
    """
    validate tool request, execute appropriate tool based on the selected tool,
    and return the result.

    Args:
        query (dict): The request data.
        user_name (str): The name of the user.

    Returns:
        str: The result of the selected tool's operation.
    """
    data = json.loads(query)

    validate_request(data)

    # Select the appropriate tool based on the query
    selected_tool = data["tool_name"]

    # Dynamically execute the selected tool with the provided arguments
    result = tool_executor(selected_tool, **data["args"])

    # Let the LLM format the final response based on the tool's output
    return mock_llm_tool_response(selected_tool, result, user_name)