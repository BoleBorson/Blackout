from datetime import datetime
from .entity import Entity

class Edge(Entity):
    """Generic Base Class"""
    def __init__(self, id: str = None, created_at: datetime = None) -> None:
        super().__init__(id, created_at)
        to_node: str
        from_node: str