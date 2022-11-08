import heapdict
from adjascency_list_v2 import AdjascencyListV2
from adjascency_list import AdjascencyList

class Dijkstra:
  def __init__(self,graph, root):
    self.graph = graph
    self.s = root
    
  def iterate(self):
    distance = [float('inf')] * self.graph.vertices_quantity
    V = self.graph.vertices()
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
  
  def iterate_heap(self):
    distance = heapdict.heapdict()
    for vertex in range(self.graph.vertices_quantity):
      distance[vertex] = float('inf')
    
    distance[self.s] = 0

    priority_queue = heapdict.heapdict()
    priority_queue[self.s] = 0

    V = self.graph.vertices()
    S = set()

    while(S != V):
      u = self.find_vertex_with_minimum_cost_heap(priority_queue)
      S.add(u[0])

      for v in self.graph.node_neighbors(u[0]):
        if distance[v[0]] > distance[u[0]] + self.weight(v):
          priority_queue[v[0]] = round(distance[u[0]] + self.weight(v), 3)
          distance[v[0]] = round(distance[u[0]] + self.weight(v), 3)
    
    return distance

  def find_vertex_with_minimum_cost_heap(self, queue):
    vertex_with_minimum_cost = queue.popitem()
    
    return vertex_with_minimum_cost

  def weight(self, v):
    return v[1]