import re


def extract_expression_from_prompt(prompt: str) -> str:
    """
    Extracts a mathematical expression from the given prompt.

    Args:
        prompt (str): The input prompt from which to extract the expression.

    Returns:
        str: The extracted mathematical expression, or an empty string if no expression is found.
    """
    patterns = re.sub(
        r'(calculate|compute|evaluate|solve|what is|find|result of|math)',
        '',
        prompt,
        flags=re.IGNORECASE
    )  # Remove unwanted characters

    return patterns.strip(" ?=")  # Return the cleaned expression  

MATH_PATTERN = re.compile(r'[-+*/^()]|\d+(\.\d+)?')  # Matches numbers and basic math operators

def math_confidence_check(expression: str) -> bool:
    """
    Checks if the given expression is a valid mathematical expression.

    Args:
        expression (str): The mathematical expression to check.

    Returns:
        bool: True if the expression is valid, False otherwise.
    """
    score = 0

    if any(keyword in expression.lower() for keyword in [
        "calculate", "compute", "evaluate", "solve", "what is", "find", "result of", "math"]
    ):
        score += 2
    
    if MATH_PATTERN.search(expression):
        score += 3
    
    if len(re.findall(r"\d", expression)) > 2:
        score += 1

    return score