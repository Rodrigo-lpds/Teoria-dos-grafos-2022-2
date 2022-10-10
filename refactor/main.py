from adjascency_matrix import AdjascencyMatrix
from adjascency_list import AdjascencyList
from bfs import BuildBFS

if __name__ == "__main__":
	graph_file_path = "../graph_files/graph_example.txt"
	matrix = AdjascencyMatrix(graph_file_path)
	#print(matrix.node_degree(1))
	#print(matrix.node_neighbors(1))
	list_rep = AdjascencyList(graph_file_path)
	#print(list_rep.node_degree(1))
	#print(list_rep.node_neighbors(1))
 
	tree = BuildBFS(list_rep, 1)
	tree.represent_tree()
  