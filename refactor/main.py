from adjascency_matrix import AdjascencyMatrix

if __name__ == "__main__":
	graph_file_path = "../graph_files/graph_example.txt"
	matrix = AdjascencyMatrix(graph_file_path)
	print(matrix.node_degree(1))
	print(matrix.node_neighbors(1))