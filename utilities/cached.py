def cached(maxsize: int = 128):
    """
    Decorator to cache the results of a function call.

    Args:
        maxsize (int): The maximum number of cached results. Default is 128.

    Returns:
        function: The decorated function with caching.
    """
    from functools import lru_cache

    def decorator(func):
        cached_func = lru_cache(maxsize=maxsize)(func)

        def wrapper(*args, **kwargs):
            return cached_func(*args, **kwargs)

        return wrapper

    return decorator