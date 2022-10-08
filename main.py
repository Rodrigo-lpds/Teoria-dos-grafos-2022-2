from graph import Graph
from adjascency_list import BuildAdjList
from adjascency_matriz import BuildAdjMatriz
from tree_graph_bfs import BuildBFS
from tree_graph_dfs import BuildDFS

def get_graph_diameter(graph):
		diameter = 0
		for node in nodes:
			#print(node)
			tree_graph_bfs = BuildBFS(graph,node+1)
			longest_path = tree_graph_bfs.shortest_longest_path()
			if diameter < longest_path:
				diameter = longest_path
		
		print("diameter: ",diameter)

if __name__ == "__main__":
	graph_file_path = "./graph_example.txt"
	graph = Graph(graph_file_path)
	
	graph_adj_list_rep = BuildAdjList(graph)
	#graph_adj_list_rep.represent_graph()
	nodes = graph_adj_list_rep.graph_nodes()
	#graph_adj_matriz_rep = BuildAdjMatriz(graph)
	#graph_adj_matriz_rep.represent_graph()
	diameter = get_graph_diameter(graph)
	#node_input = 1
	#bfs_input = int(input("BFS root: "))
	#tree_graph_bfs = BuildBFS(graph,node_input)
	#tree_graph_bfs.represent_tree()
	#tree_graph_bfs.distance_between_vertex(5)
	#tree_graph_bfs.shortest_longest_path()
	
	#tree_graph_dfs = BuildDFS(graph,node_input)
	#tree_graph_dfs.represent_tree()
