from datetime import datetime
from ..producer import Producer
from .producer_registry import *

@register_producer("default")
class DefaultProducer(Producer):
    """Has no production value. Used when a node should not produce"""
    def __init__(self, id: str = None, created_at: datetime = None) -> None:
        super().__init__(id, created_at)
        self.production = 0

    def get_production(self):
        return super().get_production() * self.production
    
    def __str__(self) -> str:
        return super().__str__() + "Default: No Production Value"

@register_producer("coal_plant")
class CoalPlant(Producer):
    def __init__(self, id: str = None, created_at: datetime = None) -> None:
        super().__init__(id, created_at)
        self.production = 2

    def get_production(self):
        return super().get_production() * self.production
    
    def __str__(self) -> str:
        return super().__str__() + "Coal Plant"

@register_producer("nuclear_power_plant")
class NuclearPowerPlant(Producer):
    def __init__(self, id: str = None, created_at: datetime = None) -> None:
        super().__init__(id, created_at)
        self.production = 5

    def get_production(self):
        return super().get_production() * self.production
    
    def __str__(self) -> str:
        return super().__str__() + "Nuclear Power Plant"
