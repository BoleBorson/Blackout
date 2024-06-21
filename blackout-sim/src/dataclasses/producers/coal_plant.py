from datetime import datetime
from ..producer import Producer

class CoalPlant(Producer):
    def __init__(self, id: str = None, created_at: datetime = None) -> None:
        super().__init__(id, created_at)

    def get_production(self):
        pass
