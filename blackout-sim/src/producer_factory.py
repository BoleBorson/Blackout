from models.producers.producer_registry import PRODUCERS
from models.producer import Producer

def producer_factory(producer_type: str):
    """Returns a constructed Producer Object

    Args:
        producer_type (str): The producer_type set in the producer_registry

    Returns:
        Producer: Valid Producer type ex: CoalPlant
    """
    class_obj: Producer = PRODUCERS.get(producer_type)
    return class_obj()