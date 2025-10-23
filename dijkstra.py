import heapq
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
        # Build adjacency list
        self.adj: Dict[str, List[Tuple[str, float]]] = {name: [] for name in vertices}
        for e in self.edges:
            self.adj[e.u].append((e.v, e.weight))

def Initialize_Single_Source(G: Graph, s: str) -> None:
    for v in G.vertices.values():
        v.dist = float('inf')
        v.prev = None
    G.vertices[s].dist = 0

def Relax(u: Vertex, v: Vertex, w: float) -> None:
    if v.dist > u.dist + w:
        v.dist = u.dist + w
        v.prev = u

def Dijkstra(G: Graph, s: str) -> None:
    Initialize_Single_Source(G, s)

    S: set[str] = set() #initialized set of processed vertices to empty
    Q: List[Tuple[float, str]] = [] #initialized set of unprocessed vertices to empty
    
    for v in G.vertices.values():
        heapq.heappush(Q, (v.dist, v.name)) #add all vertices to Q with their distances
    
    while Q:
        # Extract-Min operation
        u_dist, u_name = heapq.heappop(Q)

        # S = S ∪ {u} 
        # Skip if u is already processed or if the distance is outdated
        if u_name in S:
            continue
        if u_dist != G.vertices[u_name].dist:
            continue
        S.add(u_name)

        # For each vertex in G.Adj[u]





