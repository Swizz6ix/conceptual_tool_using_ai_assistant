def retries(max_attempts: int, delay: float = 1.0):
    """
    Decorator to retry a function call upon failure.

    Args:
        max_attempts (int): The maximum number of attempts to retry the function.
        delay (float): The delay in seconds between retries. Default is 1.0 second.

    Returns:
        function: The decorated function with retry logic.
    """
    from functools import wraps
    import time

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise e
                    time.sleep(delay)

        return wrapper

    return decorator