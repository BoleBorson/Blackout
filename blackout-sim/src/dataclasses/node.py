from .entity import Entity
from datetime import datetime
from .producer import  Producer

class Node(Entity):
    """Generic Base Class"""
    def __init__(self, producer: Producer = None, consumer = None, id: str = None, created_at: datetime = None) -> None:
        super().__init__(id, created_at)
        self.producer: Producer = producer
        self.consumer = consumer