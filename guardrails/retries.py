import random


DEAD_LETTER_QUEUE = []  # A simple list to act as a dead letter queue for failed retries

def retries(
        max_attempts: int,
        initial_delay: float = 5.0,
        backoff_factor: float = 5.0,
        max_delay: float = 1.0
    ):
    """
    Decorator to retry a function call upon failure.

    Args:
        max_attempts (int): The maximum number of attempts to retry the function.
        initial_delay (float): The initial delay in seconds between retries. Default is 1.0 second.
        backoff_factor (float): The factor by which the delay increases with each retry. Default is 2.0.
        max_delay (float): The maximum delay in seconds between retries. Default is 1.0 second.

    Returns:
        function: The decorated function with retry logic.
    """
    from functools import wraps
    import time
    from datetime import datetime

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            delay = initial_delay

            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                
                except Exception as e:
                    print(f"[{datetime.now()}] Attempt {attempt}/{max_attempts}")
                    print(f"Function: {func.__name__} failed with error: {e}.")
                    
                    if attempt == max_attempts:
                        failed_request = {
                            "timestamp": datetime.now().isoformat(),
                            "function": func.__name__,
                            "args": args,
                            "kwargs": kwargs,
                            "error": str(e),
                            "attempt": attempt
                        }
                        DEAD_LETTER_QUEUE.append(failed_request)

                        print(f"[DQL] Request moved to Dead Letter Queue after {attempt} attempts: {failed_request}")

                        raise
                
                    # Exponential backoff with a cap on the maximum delay
                    jitter = random.uniform(0, 0.5)  # Add a small random jitter to avoid thundering herd problem
                    sleep_time = min(delay, max_delay) + jitter

                    print(f"[{datetime.now()}] Attempt {attempt} failed. Retrying in {sleep_time:.2f} seconds...")
                    time.sleep(sleep_time)

                    delay *= backoff_factor

        return wrapper

    return decorator

def show_dead_letter_queue(query: str = ''):
    """
    Display all failed request
    """
    if not DEAD_LETTER_QUEUE:
        print("Dead Letter Queue is empty")
        return []
    
    print(f"You askd for {query}")
    print("\n===== DEAD LETTER QUEUE ======")

    failed_request = []

    for index, item in enumerate(DEAD_LETTER_QUEUE, start=1):
        print(f"\nRequest {index}")

        request_obj = {"request": index}

        for key, value in item.items():
            print(f"{key}: {value}")
            request_obj[key] = value
        
        failed_request.append(request_obj)

    return failed_request