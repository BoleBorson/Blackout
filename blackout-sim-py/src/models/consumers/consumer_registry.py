CONSUMERS = {}

def register_consumer(consumer_type: str):
    """Decorates concrete Consumer class. Adds class to CONSUMERS constant for factory usage

    Args:
        consumer_type (str): The key value the factory will return this consumer with.
    """
    def decorator(fn):
        CONSUMERS[consumer_type] = fn
        return fn
    return decorator