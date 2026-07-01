import re


def extract_query_from_prompt(prompt: str) -> str:
    """
    Extracts a query from the given prompt.

    Args:
        prompt (str): The input prompt from which to extract the query.

    Returns:
        str: The extracted query, or an empty string if no query is found.
    """
    # Remove common phrases that indicate a query
    patterns = re.sub(
        r'(search for|find information on|look up|what is|who is|where is)',
        '',
        prompt,
        flags=re.IGNORECASE
    )  # Remove unwanted characters

    return patterns.strip(" ?")  # Return the cleaned query