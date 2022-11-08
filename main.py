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

if __name__ == "__main__":
	graph_file_path = "./graph_files/rede_colaboracao.txt"
 	# (1) check memory usage
	#matrix = AdjascencyMatrix(graph_file_path)
	#start_time = time.time()
	#list_rep = AdjascencyList(graph_file_path)
	#print("--- %s seconds ---" % (time.time() - start_time))
	#f = open("./graph_files/grafo_2.txt", "r")
	#print(f.readline())
	list_rep = AdjascencyListV2(graph_file_path, weighted = True)
	#print(list_rep.list[2].vertex)
	node = 2722
	#nodes = [2,12,234,876,1832,28,58,100,16,1229]
	#start_time = time.time()
	#for node in nodes:
	dijkstra = Dijkstra(list_rep, node)
	#dijkstra.iterate()
	dijkstra_distance = dijkstra.iterate_heap()
	#print("The distance between node", node, "and node 20 is ", dijkstra_distance[20])
	#print("The distance between node", node, "and node 30 is ", dijkstra_distance[30])
	#print("The distance between node", node, "and node 40 is ", dijkstra_distance[40])
	#print("The distance between node", node, "and node 50 is ", dijkstra_distance[50])
	#print("The distance between node", node, "and node 60 is ", dijkstra_distance[60])
	#print("--- %s seconds ---" % (time.time() - start_time))
	print("The distance between node", node, "and node 11365 is ", dijkstra_distance[11365])
	print("The distance between node", node, "and node 471365 is ", dijkstra_distance[471365])
	print("The distance between node", node, "and node 5709 is ", dijkstra_distance[5709])
	print("The distance between node", node, "and node 11386 is ", dijkstra_distance[11386])
	print("The distance between node", node, "and node 343930 is ", dijkstra_distance[343930])
	# -------------------------------------------------------

	# (2) 1000 bfs searchs using matrix representation and list representation
	#start_time = time.time()
	
	#matrix = AdjascencyMatrix(graph_file_path)
	#start_time = time.time()
	#for node in selected_nodes_graph_3:
	#	tree = BuildDFS(matrix, node)
	#print("--- %s seconds ---" % (time.time() - start_time))
	#list_rep = AdjascencyList(graph_file_path)
	
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
	#connected_components = ConnectedComponentes(OldGraph(graph_file_path))
	#connected_components.represent_components()
	# ----------------------------------------------------
	#nodes = []
	""" for node in connected_components.components:
		nodes.append(node[0].get_name())  """
	# (7) Determine the graph diameter of given graph
	""" list_rep = AdjascencyList(graph_file_path)
	paths_distance = []
	for node in nodes:
		tree = BuildBFS(list_rep, node)
		last_explored_node = tree.explored_node(-1)
		tree = BuildBFS(list_rep, last_explored_node)
		paths_distance.append(tree.longest_short_path())
	print(paths_distance) """
	
	""" for node in list_rep.node_list():
		tree = BuildBFS(list_rep, node)
		#print(tree.last_explored_node())
		paths_distance.append(tree.longest_short_path()) """
	#print(max(paths_distance))
	# -------------------------------
	#print(paths_distance)
	#print(max(paths_distance))
	# Build graph output
	""" list_rep = AdjascencyList(graph_file_path)
	output = GraphInfoOutput(list_rep)
	output.build_file("output_grafo_5.txt") """