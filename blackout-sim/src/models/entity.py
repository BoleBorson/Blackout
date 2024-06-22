from abc import ABC
from datetime import datetime
from uuid import uuid4

class Entity(ABC):
    def __init__(self, id: str = None, created_at: datetime = None) -> None:
        self.id = id if id else str(uuid4())
        self.created_at = created_at if created_at else datetime.now()