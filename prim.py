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
        self.cost = [float('inf')] * self.graph.vertices_quantity
        self.cost[0] = 0
        self.S = set()
        priority_queue = heapdict.heapdict()
        priority_queue[self.root] = 0
        self.parents = [0] * self.graph.vertices_quantity
        self.parents[self.root] = -1
        self.cost[self.root] = 0
        while(len(self.S) < self.graph.vertices_quantity-1):
            u = self.find_vertex_with_minimum_cost_heap(priority_queue)
            self.S.add(u[0])
            for v in self.graph.node_neighbors(u[0]):
                if self.cost[v[0]] > self.weight(v):
                    self.parents[v[0]] = u[0]
                    priority_queue[v[0]] = self.weight(v)
                    self.cost[v[0]] = self.weight(v)

    def find_vertex_with_minimum_cost_heap(self, queue):
        vertex_with_minimum_cost = queue.popitem()
        return vertex_with_minimum_cost
    def weight(self, v):
        return v[1]

    def write_MST(self, file_name):
        f = open(file_name, "w")
        f.write("Custo total: " + str(self.total_cost_MST()) + "\n")
        f.write("Arvore:" + "\n")
        for vertex in self.S:
            if(self.parents[vertex] == -1):
                f.write("Vertice: "+ str(vertex) + "--- Pai: Raiz" + ", Peso: " + str(self.cost[vertex]) + "\n") 
            else:
                f.write("Vertice: "+ str(vertex) + "--- Pai: " + str(self.parents[vertex]) + ", Peso: " + str(self.cost[vertex]) + "\n") 
        f.close()

    def total_cost_MST(self):
        total = 0.000
        for cost in self.cost:
            total += cost
        print(total)
        return total

