from datetime import datetime
from .entity import Entity
from typing import Optional


class Edge(Entity):
    """Generic Base Class"""

    def __init__(
        self,
        source_node,
        destination_node,
        id: Optional[str] = None,
        created_at: Optional[datetime] = None,
    ) -> None:
        if not source_node or not destination_node:
            raise ValueError("Both a souce Node and destination Node must be provided")
        super().__init__(id, created_at)
        self.source_node = source_node
        self.destination_node = destination_node
