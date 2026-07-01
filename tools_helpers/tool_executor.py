from tools_helpers.valid_tools import valid_tools


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
    if tool_name not in valid_tools:
        raise ValueError(f"Tool '{tool_name}' is not recognized.")

    tool = valid_tools[tool_name]
    return tool(*args, **kwargs)