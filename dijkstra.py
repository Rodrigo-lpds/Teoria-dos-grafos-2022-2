from adjascency_list_v2 import AdjascencyListV2
from adjascency_list import AdjascencyList

class Dijkstra:
  def __init__(self,graph):
    self.graph = graph
    
  def iterate(self):
    distance = [float('inf')] * self.graph.vertices.count
    V = self.graph.vertices ## needs to be a set type
    S = set()
    distance[s] = 0
    
    while(S != V):
      remain_vertices = V - S
      u = find_vertex_with_minimum_cost(remain_vertices)
      S.add(u)
      for v in self.graph.neighbors(u):
        if distance[v] > distance[u] + weight(u,v):
          distance[v] = distance[u] + weight(u,v)
    
    return distance
  
  def read_graph