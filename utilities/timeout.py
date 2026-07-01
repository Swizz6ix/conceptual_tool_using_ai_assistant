def timeout(seconds):
    """
    Decorator to add a timeout to a function.

    Args:
        seconds (int): The number of seconds before the function times out.

    Returns:
        function: The decorated function with a timeout.
    """
    import signal
    from functools import wraps

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            def handler(signum, frame):
                raise TimeoutError(f"Function '{func.__name__}' timed out after {seconds} seconds.")

            # Set the signal handler and a timer
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)

            try:
                result = func(*args, **kwargs)
            finally:
                # Cancel the timer if the function completes in time
                signal.alarm(0)

            return result

        return wrapper

    return decorator