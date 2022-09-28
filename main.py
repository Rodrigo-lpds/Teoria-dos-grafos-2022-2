from graph import Graph
from adjascency_list import AdjList

if __name__ == "__main__":
	graph_file_path = "./graph_example.txt"
	graph = Graph(graph_file_path)
	print(graph.readed_graph)
	V = int(graph.vertices_quantity)
	graph_adj_list_rep = AdjList(V)
	for line in graph.readed_graph[1:]:
		line = line.split(' ')
		graph_adj_list_rep.add_edge(int(line[0]), int(line[1]))

	graph_adj_list_rep.print_agraph()
	
