from datetime import datetime
from ..producer import Producer

class CoalPlant(Producer):
    def __init__(self, id: str = None, created_at: datetime = None) -> None:
        super().__init__(id, created_at)
        self.production_factor = 2

    def get_production(self):
        return super().get_production() * self.production_factor
