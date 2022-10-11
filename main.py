import time
from adjascency_matrix import AdjascencyMatrix
from adjascency_list import AdjascencyList
from bfs import BuildBFS
from dfs import BuildDFS
from connected_components import ConnectedComponentes
from graph_info_output import GraphInfoOutput

if __name__ == "__main__":
	graph_file_path = "./graph_files/graph_example.txt"
 	# (1) check memory usage
 	# matrix = AdjascencyMatrix(graph_file_path)
	# list_rep = AdjascencyList(graph_file_path)
	# -------------------------------------------------------

	# (2) 1000 bfs searchs using matrix representation and list representation
	#start_time = time.time()
	#matrix = AdjascencyMatrix(graph_file_path)
	#list_rep = AdjascencyList(graph_file_path)
	#tree = BuildBFS(matrix, 1)
	#print("--- %s seconds ---" % (time.time() - start_time))
	
	#start_time = time.time()
	#tree = BuildBFS(list_rep, 1)
	#print("--- %s seconds ---" % (time.time() - start_time))
	# ----------------------------------------------------

	# (3) 1000 dfs searchs using matrix representation and list representation
	""" start_time = time.time()
		matrix = AdjascencyMatrix(graph_file_path)
		tree = BuildDFS(matrix, 1)
		print("--- %s seconds ---" % (time.time() - start_time)) """
	
	#start_time = time.time()
	#list_rep = AdjascencyList(graph_file_path)
	#tree = BuildDFS(list_rep, 1)
	#print("--- %s seconds ---" % (time.time() - start_time))
	# ----------------------------------------------------

	# (4) Determine the father of the 10,20, and 30 nodes of the graph using vertices 1,2 3 as starting points

	# 4.1 Using BFS search
	""" list_rep = AdjascencyList(graph_file_path)
	for start_node in range(1,4):
		bfs = BuildBFS(list_rep, start_node)
		for i in range(10,31,10):
			if bfs.tree.tree_graph.get(i) is not None:
				print("Node father of", i, "it's node:", bfs.tree.tree_graph.get(i).dad)
			else:
				print("Node", i, "has no father when bfs starts searching from node", start_node)
		print() """

	# 4.2 Using DFS search
	""" list_rep = AdjascencyList(graph_file_path)
	for start_node in range(1,4):
		bfs = BuildDFS(list_rep, start_node)
		for i in range(10,31,10):
			if bfs.tree.tree_graph.get(i) is not None:
				print("Node father of", i, "it's node:", bfs.tree.tree_graph.get(i).dad)
			else:
				print("Node", i, "has no father when dfs starts searching from node", start_node)
		print() """
	# ----------------------------------------------------

	# (5) Determine the distance between nodes (10,20), (10,30), (20,30) (we gonna use BFS search)
	""" list_rep = AdjascencyList(graph_file_path)
	nodes = [[10,20],[10,30], [20,30]]
	for node in nodes:
		bfs = BuildBFS(list_rep, node[0])
		if bfs.tree.tree_graph.get(node[1]) is not None:
			print("Distance between nodes", node[0], "and", node[1], ":", bfs.tree.tree_graph.get(node[1]).nivel)
		else:
			print("There's no path from node", node[0], "to", node[1]) """
		#print(bfs.tree.tree_graph.get(30).nivel)
		
	
	# ----------------------------------------------------

	# (6) Find all connected components of given graph. Return how many connected components,
	#  the length of the largest connected components and the length of the smallest
	list_rep = AdjascencyList(graph_file_path)
	connected_components = ConnectedComponentes(list_rep)
	connected_components.represent_components()
	# ----------------------------------------------------


	# (7) Determine the graph diameter of given graph
	""" list_rep = AdjascencyList(graph_file_path)
	paths_distance = []
	tree = BuildBFS(list_rep, 1)
	paths_distance.append(tree.longest_short_path())
	last_explored_node = tree.last_explored_node()
	tree = BuildBFS(list_rep, last_explored_node)
	paths_distance.append(tree.longest_short_path()) """

	""" for node in list_rep.node_list():
		tree = BuildBFS(list_rep, node)
		#print(tree.last_explored_node())
		paths_distance.append(tree.longest_short_path()) """
	# -------------------------------
	#print(paths_distance)
	#print(max(paths_distance))
	# Build graph output
	""" list_rep = AdjascencyList(graph_file_path)
	output = GraphInfoOutput(list_rep)
	output.build_file("output_grafo_5.txt") """