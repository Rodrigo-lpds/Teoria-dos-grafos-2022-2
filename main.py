from graph import Graph
from adjascency_list import BuildAdjList
from adjascency_matriz import BuildAdjMatriz
from tree_graph_bfs import BuildBFS

if __name__ == "__main__":
	graph_file_path = "./graph_example.txt"
	graph = Graph(graph_file_path)
	
	graph_adj_list_rep = BuildAdjList(graph)
	graph_adj_list_rep.represent_graph()

	graph_adj_matriz_rep = BuildAdjMatriz(graph)
	graph_adj_matriz_rep.represent_graph()

	bfs_input = 5
	#bfs_input = int(input("BFS root: "))
	tree_graph_bfs = BuildBFS(graph,bfs_input)
	tree_graph_bfs.represent_tree()

