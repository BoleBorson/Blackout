from abc import abstractmethod, ABC
from datetime import datetime
from uuid import uuid4

class Entity(ABC):
    def __init__(self, id: str = None, created_at: datetime = None) -> None:
        self.id = id if id else str(uuid4())
        self.created_at = created_at if created_at else datetime.now()

class Node(Entity):
    """Generic Base Class"""
    def __init__(self, producer, consumer, id: str = None, created_at: datetime = None) -> None:
        super().__init__(id, created_at)
        producer = producer if producer else None
        consumer = consumer if consumer else None

class Edge(Entity):
    """Generic Base Class"""
    to_node: str
    from_node: str
