from adjascency_list_v2 import AdjascencyListV2
from adjascency_list import AdjascencyList

class Dijkstra:
  def __init__(self,graph, root):
    self.graph = graph
    self.s = root
    
  def iterate(self):
    distance = [float('inf')] * self.graph.vertices_quantity
    V = self.graph.vertices()
    #print(V)
    S = set()
    distance[self.s] = 0
    
    while(S != V):
      remain_vertices = V - S
      u = self.find_vertex_with_minimum_cost(remain_vertices, distance)
      S.add(u)
      for v in self.graph.node_neighbors(u):
        if distance[v[0]] > distance[u] + self.weight(v):
          distance[v[0]] = round( distance[u] + self.weight(v), 3)
    
    return distance

  def find_vertex_with_minimum_cost(self, vertices, distance):
    vertex_with_minimum_cost = vertices.pop()
    
    for vertex in vertices:
      if distance[vertex] < distance[vertex_with_minimum_cost]:
        vertex_with_minimum_cost = vertex
    
    return vertex_with_minimum_cost
  
  def weight(self, v):
    return v[1]