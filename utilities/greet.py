from datetime import datetime


def greet() -> str:
    """
    Generates a greeting message based on the current time.

    Returns:
        str: The greeting message.
    """

    current_hour = datetime.now().hour

    if 5 <= current_hour < 12:
        return "Good morning, and welcome!"
    
    elif 12 <= current_hour < 18:
        return "Good afternoon, and welcome!"
    
    else:
        return "Good evening, and welcome!"