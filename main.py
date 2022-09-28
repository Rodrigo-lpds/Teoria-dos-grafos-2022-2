from graph import Graph

if __name__ == "__main__":
	graph_file_path = "./graph_example.txt"
	graph = Graph(graph_file_path)
	print(graph.vertices_quantity)
	print(graph.edges_quantity)