from dataclasses.producers import *
from dataclasses.consumers import *
from dataclasses.node import Node

coal_node = Node(producer=CoalPlant())

city_node = Node(consumer=City())

print(coal_node.producer.get_production())