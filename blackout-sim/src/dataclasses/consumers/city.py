from datetime import datetime
from ..consumer import Consumer

class City(Consumer):
    def __init__(self, id: str = None, created_at: datetime = None) -> None:
        super().__init__(id, created_at)
        self.city_consumption = 100

    def get_consumption(self):
        return super().get_consumption() + self.city_consumption