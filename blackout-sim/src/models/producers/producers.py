from datetime import datetime
from ..producer import Producer
from .producer_registry import *

@register_producer("coal_plant")
class CoalPlant(Producer):
    def __init__(self, id: str = None, created_at: datetime = None) -> None:
        super().__init__(id, created_at)
        self.production_factor = 2

    def get_production(self):
        return super().get_production() * self.production_factor
    
    def __str__(self) -> str:
        return super().__str__() + "Coal Plant"

@register_producer("nuclear_power_plant")
class NuclearPowerPlant(Producer):
    def __init__(self, id: str = None, created_at: datetime = None) -> None:
        super().__init__(id, created_at)
        self.production_factor = 5

    def get_production(self):
        return super().get_production() * self.production_factor
    
    def __str__(self) -> str:
        return super().__str__() + "Coal Plant"
