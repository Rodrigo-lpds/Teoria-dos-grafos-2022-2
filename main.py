from graph import Graph
from adjascency_list import BuildAdjList

if __name__ == "__main__":
	graph_file_path = "./graph_example.txt"
	graph = Graph(graph_file_path)
	
	V = int(graph.vertices_quantity)
	graph_adj_list_rep = BuildAdjList(graph)

	graph_adj_list_rep.represent_graph()
	
