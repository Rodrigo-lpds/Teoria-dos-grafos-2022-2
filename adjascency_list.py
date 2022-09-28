# Adjascency List representation in Python
class AdjNode:
	def __init__(self, value):
		self.vertex = value
		self.next = None


class AdjList:
	def __init__(self, num):
		self.V = num + 1
		self.graph = [None] * self.V

	# Add edges
	def add_edge(self, s, d):
		node = AdjNode(d)
		node.next = self.graph[s]
		self.graph[s] = node

		node = AdjNode(s)
		node.next = self.graph[d]
		self.graph[d] = node

	# Print the graph
	def print_agraph(self):
		for i in range(self.V):
			temp = self.graph[i]
			if temp is not None:
				print("Vertex " + str(i) + ":", end="")
				while temp:
					print(" -> {}".format(temp.vertex), end="")
					temp = temp.next
				print(" \n")

class BuildAdjList:
	def __init__(self, graph):
		self.graph = graph
		self.V = int(self.graph.vertices_quantity)
		self.graph_adj_list_rep = AdjList(self.V)

	def represent_graph(self):    
		for line in self.graph.readed_graph[1:]:
			line = line.split(' ')
			self.graph_adj_list_rep.add_edge(int(line[0]), int(line[1]))
			
		self.graph_adj_list_rep.print_agraph()