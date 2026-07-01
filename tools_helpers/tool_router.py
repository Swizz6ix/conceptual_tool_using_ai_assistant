import json

from utility.validate_request import validate_request
from tools_helpers.tool_executor import tool_executor


def tool_router(query: dict) -> str:
    """
    Routes the user's query to the appropriate tool based on the selected tool.

    Args:
        query (str): The user's query or request.

    Returns:
        str: The result of the selected tool's operation.
    """
    data = json.loads(query)

    validate_request(data)

    # Select the appropriate tool based on the query
    selected_tool = data["tool_name"]

    if selected_tool == "calculator":
        # Extract the mathematical expression from the query
        expression = data["args"]["expression"]
        result = tool_executor(selected_tool, expression)
        return f"Result of the calculation: {result}"

    elif selected_tool == "web_search":
        # Perform a web search with the given query
        results = tool_executor(selected_tool, data["args"]["query"])
        return f"Web search results: {results}"

    elif selected_tool == "text_summarizer":
        # Summarize the text provided in the query
        summary = tool_executor(selected_tool, data["args"]["text"])
        return f"Summary of the text: {summary}"

    elif selected_tool == "get_weather":
        # Get weather information based on the location provided in the query
        weather_info = tool_executor(selected_tool, data["args"]["location"])
        return f"Weather information: {weather_info}"

    else:
        return "No suitable tool found for the given query."