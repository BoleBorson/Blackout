PRODUCERS = {}

def register_producer(producer_type: str):
    """Decorates concrete Producer class. Adds class to PRODUCERS constant for factory usage

    Args:
        producer_type (str): The key value the factory will return this producer with.
    """
    def decorator(fn):
        PRODUCERS[producer_type] = fn
        return fn
    return decorator
