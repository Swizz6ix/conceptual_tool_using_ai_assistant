import re


def extract_text_from_prompt(prompt: str) -> str:
    """
    Extracts text from the given prompt.

    Args:
        prompt (str): The input prompt from which to extract the text.

    Returns:
        str: The extracted text, or an empty string if no text is found.
    """
    # Remove common phrases that indicate a request for text
    patterns = re.sub(
        r'(write|generate|create|compose|draft|produce|summarize|paraphrase|rephrase|summary|tl;dr)',
        '',
        prompt,
        flags=re.IGNORECASE
    )  # Remove unwanted characters

    return patterns.strip(" :\"")  # Return the cleaned text