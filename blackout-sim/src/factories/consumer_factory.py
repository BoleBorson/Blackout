from models.consumers.consumer_registry import CONSUMERS
from models.consumer import Consumer

def consumer_factory(consumer_type: str = "default"):
    """Returns a constructed Producer Object

    Args:
        consumer_type (str): The consumer_type set in the consumer_registry

    Returns:
        Consumer: Valid Consumer type ex: City
    """
    class_obj: Consumer = CONSUMERS.get(consumer_type)
    return class_obj()