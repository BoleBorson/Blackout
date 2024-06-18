from pydantic import BaseModel
from uuid import uuid4

class Node(BaseModel):
    """Generic Base Class"""
    id: str = str(uuid4())
    created_at: str

class Edge(BaseModel):
    """Generic Base Class"""
    id: int = str(uuid4())
    created_at: str
    to_node: str
    from_node: str
