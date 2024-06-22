from models.producers import *
from models.consumers import *
from models.node import Node

coal_node = Node(producer=CoalPlant())

city_node = Node(consumer=City())

print(coal_node.producer.get_production())