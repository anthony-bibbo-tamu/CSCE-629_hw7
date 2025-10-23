from typing import Dict, List, Optional, Tuple

class Vertex:
    def __init__(self, name: str):
        self.name = name
        self.dist: float = float('inf')
        self.prev: Optional['Vertex'] = None

class Edge:
    def __init__(self, u: str, v: str, weight: float):
        self.u = u
        self.v = v
        self.weight = weight

class Graph:
    def __init__(self, vertices: List[str], edges: List[Tuple[str, str, float]]):
        self.vertices: Dict[str, Vertex] = {name: Vertex(name) for name in vertices}
        self.edges: List[Edge] = [Edge(u, v, w) for (u, v, w) in edges]
