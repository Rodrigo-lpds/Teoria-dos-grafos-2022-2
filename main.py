import time
import random
from adjascency_matrix import AdjascencyMatrix
from adjascency_list import AdjascencyList
from adjascency_list_v2 import AdjascencyListV2
from adjascency_list_fulkerson import AdjascencyListFulkerson
from bfs import BuildBFS
from dfs import BuildDFS
from connected_components import ConnectedComponentes
from graph_info_output import GraphInfoOutput
from old_graph import OldGraph
from dijkstra import Dijkstra
from ford_fulkerson import FordFulkerson

if __name__ == "__main__":
	graph_file_path = "./graph_files/grafo_rf_2.txt"
	#	grafo rf 8 levou 2726.827 segundos e o resultado deu 5377510.0
	# 	grafo rf 7 levou 53.343 segundos e o resultado deu 611
	start_time = time.time()
	list_rep_new = AdjascencyListFulkerson(graph_file_path)
	ff = FordFulkerson(list_rep_new.adj,1,2)
	print("--- %s seconds ---" % (time.time() - start_time))
	print(ff.max_flow)