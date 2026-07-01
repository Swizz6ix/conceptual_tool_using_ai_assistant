import sys
import time
import threading
from functools import wraps


class TimeoutError(Exception):
    """Custom exception to indicate a timeout."""
    pass

def timeout(seconds: int):
    """
    Cross-platform decorator to add a timeout to a function.
    - Uses signal module on Unix-like systems.
    - Uses threading on Windows.

    Args:
        seconds (int): The number of seconds before the function times out.

    Returns:
        function: The decorated function with a timeout.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # UNIX Implementation using signal
            if sys.platform != "win32":
                import signal

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

            # Windows Implementation using threading
            else:
                result_container = {}

                def target():
                    try:
                        result_container['result'] = func(*args, **kwargs)
                    except Exception as e:
                        result_container['exception'] = e

                thread = threading.Thread(target=target)
                thread.start()
                thread.join(seconds)

                if thread.is_alive():
                    raise TimeoutError(f"Function '{func.__name__}' timed out after {seconds} seconds.")
                if 'exception' in result_container:
                    raise result_container['exception']
                result = result_container.get('result')

            return result

        return wrapper

    return decorator