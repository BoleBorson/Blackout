from datetime import datetime
from .entity import Entity
from abc import abstractmethod, ABC

class Producer(Entity):
    def __init__(self, id: str = None, created_at: datetime = None) -> None:
        super().__init__(id, created_at)

    @abstractmethod
    def get_production(self):
        """Returns the production value of a producer"""
        return