import time
from case_study import CaseStudy

if __name__ == "__main__":
	graph_file_path = "./graph_files/graph_example.txt"
	graph = CaseStudy(graph_file_path)
	
	# (1) check memory usage
	""" start_time = time.time()
	graph.adjascency_list_representation()
	print("--- %s seconds ---" % (time.time() - start_time))
	start_time = time.time()
	graph.adjascency_matrix_representation()
	print("--- %s seconds ---" % (time.time() - start_time)) """
	# -------------------------------------------------------

	# (2) 1000 bfs searchs using matrix representation and list representation
	start_time = time.time()
	graph.bfs_search(1)
	print("--- %s seconds ---" % (time.time() - start_time))
	# ----------------------------------------------------

	# (3) 1000 dfs searchs using matrix representation and list representation

	# ----------------------------------------------------

	# (4) Determine the father of the 10,20, and 30 nodes of the graph using vertices 1,2 3 as starting points

	# 4.1 Using BFS search

	# 4.2 Using DFS search
	
	# ----------------------------------------------------

	# (5) Determine the distance between nodes (10,20), (10,30), (20,30) (we gonna use BFS search)

	# ----------------------------------------------------

	# (6) Find all connected components of given graph. Return how many connected components,
	#  the length of the largest connected components and the length of the smallest

	# ----------------------------------------------------


	# (7) Determine the graph diameter of given graph