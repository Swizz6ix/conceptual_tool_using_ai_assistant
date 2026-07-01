STOP_WORDS = ["exit", "quit", "stop", "bye", "goodbye", "break"]  # Words to stop the application

def stop(user_input: str) -> bool:
    """
    Check if the user input contains any of the stop words.

    Args:
        user_input (str): The input string from the user.
        stop_words (list[str]): A list of words that indicate the application should stop.

    Returns:
        bool: True if any stop word is found in the user input, False otherwise.
    """
    return any(stop_word in user_input.lower().strip() for stop_word in STOP_WORDS)