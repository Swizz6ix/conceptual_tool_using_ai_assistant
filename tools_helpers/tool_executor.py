from guardrails import (
    timeout, retries, cached, VALID_TOOLS
)


@cached(maxsize=128)
@retries(max_attempts=5, max_delay=15.0)  # Retry up to 3 times with a 5-second delay between attempts
@timeout(60) # Set a timeout of 5 seconds for tool execution
def tool_executor(tool_name: str, *args, **kwargs):
    """
    Executes the specified tool with the provided arguments.

    Args:
        tool_name (str): The name of the tool to execute.
        *args: Positional arguments to pass to the tool.
        **kwargs: Keyword arguments to pass to the tool.
    Returns:
        The result of the tool execution.
    """
    if tool_name not in VALID_TOOLS:
        raise ValueError(f"Tool '{tool_name}' is not recognized.")

    tool = VALID_TOOLS[tool_name]['function']

    return tool(*args, **kwargs)