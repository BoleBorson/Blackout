from pydantic import BaseModel
from uuid import uuid4

class Node(BaseModel):
    id: str = str(uuid4())
    name: str
    age: int

    def production():
        pass