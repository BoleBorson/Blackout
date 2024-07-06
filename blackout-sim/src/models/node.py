from .entity import Entity
from datetime import datetime
from .producer import  Producer
from .consumer import Consumer
from .edge import Edge
from typing import Optional

class Node(Entity):
    """A physical entity in the sim. Must have a producer or consumer. Can have both.

    Args:
        producer (Producer): A concrete Producer ex: CoalPlant()
        consumer (Consumer): A concrete Consmer ex: City()
    """
    def __init__(self, producer: Optional[Producer] = None, consumer: Optional[Consumer] = None, id: str = None, created_at: datetime = None) -> None:
        super().__init__(id, created_at)
        if not producer and not consumer:
            raise ValueError("Either producer or consumer must be provided.")
        self.producer: Producer = producer
        self.consumer = consumer
        self.edges: list[Edge] = []

    def __str__(self) -> str:
        return f"Node {self.id} \n {self.producer.__str__()} \n {self.consumer.__str__()}"