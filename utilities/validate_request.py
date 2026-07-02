from guardrails.valid_tools import VALID_TOOLS


def validate_request(request: dict) -> bool:
    """
    Validates the structure and content of a request dictionary.

    Args:
        request (dict): The request dictionary to validate.

    Returns:
        bool: True if the request is valid, False otherwise.
    """
    REQUIRED_KEYS = ["tool_name", "args"]
    REQUIRED_ARG_KEYS = {
        "calculator": ["expression"],
        "web_search": ["query"],
        "get_weather": ["location"],
        "text_summarizer": ["text"],
        "show_dlq": ["query"]
    }

    # Example validation logic - replace with actual validation rules
    if not isinstance(request, dict):
        raise TypeError("Request must be a dictionary.")   

    for key in REQUIRED_KEYS:
        if key not in request:
            raise ValueError(f"Missing required key: {key}")
        
    tool = request["tool_name"]
    for arg_key in REQUIRED_ARG_KEYS[tool]:
        if arg_key not in request["args"]:
            raise ValueError(f"Missing required argument key: {arg_key} for tool '{request['tool_name']}'")
        
    if not isinstance(request["args"], dict):
        raise TypeError("The 'args' value must be a dictionary.")
    
    if not isinstance(request["tool_name"], str):
        raise TypeError("The 'tool_name' value must be a string.")
    
    if not request["tool_name"]:
        raise ValueError("The 'tool_name' value cannot be empty.")
    
    if not request["args"]:
        raise ValueError("The 'args' dictionary cannot be empty.")
    
    if not all(isinstance(k, str) for k in request["args"].keys()):
        raise TypeError("All keys in the 'args' dictionary must be strings.")
    
    if not all(isinstance(v, (str, int, float, bool)) for v in request["args"].values()):
        raise TypeError("All values in the 'args' dictionary must be of type str, int, float, or bool.")
    
    if not all(request["args"].values()):
        raise ValueError("All values in the 'args' dictionary must be non-empty.")
    
    if not all(k.strip() for k in request["args"].keys()):
        raise ValueError("All keys in the 'args' dictionary must be non-empty strings.")
    
    if request["tool_name"] not in VALID_TOOLS:
        raise ValueError(f"Tool '{request['tool_name']}' is not recognized or supported.")

    return True