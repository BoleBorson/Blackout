from datetime import datetime
from .entity import Entity
from abc import abstractmethod

class Consumer(Entity):
    def __init__(self, id: str = None, created_at: datetime = None) -> None:
        super().__init__(id, created_at)
        self.base_consumption = 10

    @abstractmethod
    def get_consumption(self):
        """Returns the consumption value of a consumer"""
        return self.base_consumption  