from pydantic import BaseModel
from uuid import uuid4

class Node(BaseModel):
    """
    Generic Base Class \n
    Represent an entity
    """
    id: str = str(uuid4())

    def production():
        pass