import re


def extract_dlq(query: str) -> str:
    """
    Extract dlq from the given query

    Args:
        query (str): The input query from which to extract dlq

    Returns:
        str: The extracted dlq
    """
    patterns = re.sub(
        r'show dlq'
    )