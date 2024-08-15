from models.producers import *
from models.consumers import *
from models.node import Node
from models.edge import Edge
from factories.consumer_factory import consumer_factory
from factories.producer_factory import producer_factory


class Graph:
    def __init__(self) -> None:
        self.nodes = []
        self.edges = []

    def add_node_to_graph(
        self, producer_type: str = "default", consumer_type: str = "default"
    ) -> Node:
        node = Node(
            producer=producer_factory(producer_type),
            consumer=consumer_factory(consumer_type),
        )
        self.nodes.append(node)
        return node
    
    def create_edge(source_node: Node, destination_node: Node) -> Edge:
        edge = Edge(
            source_node=source_node,
            destination_node=destination_node
        )

    def __str__(self) -> str:
        output = "Nodes in Graph: \n \n"
        for node in self.nodes:
            output += node.__str__() + "\n\n"
        output += "\nEdges in Graph \n \n"
        for edge in self.edges:
            output += edge.__str__()
        return output


graph = Graph()
graph.add_node_to_graph(producer_type="coal_plant")
graph.add_node_to_graph(producer_type="nuclear_power_plant")
graph.add_node_to_graph(consumer_type="city")
print(graph)
