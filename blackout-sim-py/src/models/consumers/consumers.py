from datetime import datetime
from ..consumer import Consumer
from .consumer_registry import *

@register_consumer("default")
class DefaultConsumer(Consumer):
    """Has no consumption value. Used when a node should not consume"""
    def __init__(self, id: str = None, created_at: datetime = None) -> None:
        super().__init__(id, created_at)
        self.consumption = 0

    def get_consumption(self):
        return self.consumption
    
    def __str__(self) -> str:
        return super().__str__() + "Default: No Consumption Value"

@register_consumer("city")
class City(Consumer):
    def __init__(self, id: str = None, created_at: datetime = None) -> None:
        super().__init__(id, created_at)
        self.consumption = 100

    def get_consumption(self):
        return super().get_consumption() + self.consumption

    def __str__(self) -> str:
        return super().__str__() + "City"