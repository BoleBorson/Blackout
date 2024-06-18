from pydantic import BaseModel
from uuid import uuid4

class Edge(BaseModel):
    """
    Generic Base Class \n
    Represent a connection between two entites (nodes)
    """
    id: int = str(uuid4())