from graph import Graph
from adjascency_matriz import BuildAdjMatriz
from adjascency_list import BuildAdjList
from tree_graph_bfs import BuildBFS
from tree_graph_dfs import BuildDFS
from connected_components import ConnectedComponentes

class CaseStudy: 
	def __init__(self, file_name):
	    self.graph = Graph(graph_file_path)
    
    def adjascency_list_representation(self):
        list_rep = BuildAdjList(self.graph)
        list_rep.represent_graph()
    
    def adjascency_matrix_representation(self):
        matrix_rep = BuildAdjMatriz(self.graph)
	    matrix_rep.represent_graph()
    
    def graph_diameter(self):
        nodes = BuildAdjList(self.graph).graph_nodes()
		diameter = 0
		for node in nodes:
			tree_graph_bfs = BuildBFS(self.graph,node+1)
			longest_path = tree_graph_bfs.shortest_longest_path()
			if diameter < longest_path:
				diameter = longest_path
		
		return diameter
    
    def bfs_search(self, node_input):
        tree = BuildBFS(graph,self.node_input)
	    tree.represent_tree()
    
    def dfs_search(self, node_input):
        tree = BuildDFS(graph,node_input)
	    tree.represent_tree()
    
    def connected_components(self):
        connected_components = ConnectedComponentes(self.graph)
	    connected_components.represent_components()