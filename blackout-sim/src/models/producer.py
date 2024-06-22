from datetime import datetime
from .entity import Entity
from abc import abstractmethod

class Producer(Entity):
    def __init__(self, id: str = None, created_at: datetime = None) -> None:
        super().__init__(id, created_at)
        self.base_production = 100

    @abstractmethod
    def get_production(self):
        """Returns the production value of a producer"""
        return self.base_production