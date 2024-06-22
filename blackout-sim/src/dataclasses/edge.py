from .entity import Entity

class Edge(Entity):
    """Generic Base Class"""
    to_node: str
    from_node: str