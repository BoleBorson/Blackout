from base import Node

class Producer(Node):
    production_factor: int
    type: str

    def production(self, work):
        return self.production_factor * work
    
prod = Producer(name="PPL2", age=10, production_factor=10, type="Power")
print(prod.production(work=10))