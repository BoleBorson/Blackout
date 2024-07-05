from models.producers import *
from models.consumers import *
from models.node import Node

coal_node = Node(producer=CoalPlant())

city_node = Node(consumer=City())

print(coal_node.producer.get_production())

class Graph():
    def __init__(self) -> None:
        self.nodes = {}
        self.edges = {}

    def add_node_to_graph(producer_type: str = None, consumer_type: str = None) -> None:
        pass