import time
import random
from adjascency_matrix import AdjascencyMatrix
from adjascency_list import AdjascencyList
from adjascency_list_v2 import AdjascencyListV2
from bfs import BuildBFS
from dfs import BuildDFS
from connected_components import ConnectedComponentes
from graph_info_output import GraphInfoOutput
from old_graph import OldGraph
from dijkstra import Dijkstra
import heapdict

class Prim:
    def __init__(self, graph, root):
        self.graph = graph
        self.root = root
    
    def generate_MST(self):
        cost = [float('inf')] * self.graph.vertices_quantity
        S = {}
        priority_queue = heapdict.heapdict()
        priority_queue[self.root] = 0
        cost[self.root]
        while(S.__len__ < self.graph.vertices_quantity):
            u = self.find_vertex_with_minimum_cost_heap(priority_queue)
            S.add(u[0])
            for v in self.graph.node_neighbors(u[0]):
                if cost[v[0]] > self.weight(v):
                    priority_queue[v[0]] = self.weight(v)
                    cost[v[0]] = self.weight(v)
        
        return S

    def find_vertex_with_minimum_cost_heap(self, queue):
        vertex_with_minimum_cost = queue.popitem()
        return vertex_with_minimum_cost
    def weight(self, v):
        return v[1]

