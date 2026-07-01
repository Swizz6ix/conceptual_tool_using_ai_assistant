from guardrails.cached import cached


@cached(maxsize=128)
def text_summarizer(text, max_length=100):
    """
    Summarizes the input text to a specified maximum length.

    Parameters:
    text (str): The input text to be summarized.
    max_length (int): The maximum length of the summary.

    Returns:
    str: The summarized text.
    """
    # Placeholder for actual summarization logic
    # In a real implementation, you would use an AI model or algorithm here
    if len(text) <= max_length:
        return text
    else:
        return text[:max_length] + '...'