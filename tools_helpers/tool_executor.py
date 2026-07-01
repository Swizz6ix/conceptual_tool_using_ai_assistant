from guardrails.timeout import timeout
from guardrails.retries import retries
from guardrails.valid_tools import VALID_TOOLS


@timeout(5)  # Set a timeout of 5 seconds for tool execution
@retries(max_attempts=3, delay=5)  # Retry up to 3 times with a 5-second delay between attempts
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