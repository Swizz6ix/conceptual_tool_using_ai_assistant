import re


def extract_location_from_prompt(prompt: str) -> str:
    """
    Extracts a location from the given prompt.

    Args:
        prompt (str): The input prompt from which to extract the location.

    Returns:
        str: The extracted location, or an empty string if no location is found.
    """
    patterns = [
        r"\bin\s+([A-Za-z\s]+)",  # Matches "in <location>"
        r"\bat\s+([A-Za-z\s]+)",  # Matches "at <location>"
        r"\bfrom\s+([A-Za-z\s]+)",  # Matches "from <location>"
        r"\bto\s+([A-Za-z\s]+)",  # Matches "to <location>"
        r"\bnear\s+([A-Za-z\s]+)",  # Matches "near <location>"
        r"\bfor\s+([A-Za-z\s]+)",  # Matches "for <location>"
    ]

    for pattern in patterns:
        match = re.search(pattern, prompt, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return "Unknown Location"  # Return a default value if no location is found