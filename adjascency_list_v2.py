# to do: minimum graph degree, maximum graph degree, mean graph degree and median graph degree
from tabnanny import verbose

class AdjNode:
	def __init__(self, value):
		self.vertex = value
		self.next = None
  
class AdjascencyListV2:
	def __init__(self, file_name):
		self.file_name = file_name

		f = open(self.file_name, "r")
		vertices_quantity = int(f.readline()) + 1

		self.list = [None] * vertices_quantity
		self.build_representation()


	def build_representation(self):
		fist_line = True
		with open(self.file_name) as f:
			for line in f:
				if fist_line != True:
					edge = line.strip().split(' ')
					self.add_edge(int(edge[0]), int(edge[1]))
				else:
					fist_line = False

    # Add edges
	def add_edge(self, s, d):
		node = AdjNode(d)
		node.next = self.list[s]
		self.list[s] = node

		node = AdjNode(s)
		node.next = self.list[d]
		self.list[d] = node

	def node_list(self):
		nodes = []
		for node in self.list:
			if node is not None:
				nodes.append(self.list.index(node))
		return nodes

	def node_neighbors(self, node):
		neighbors = []
		#self.list[node]
		node = self.list[node]
		node_value = node.vertex
		next_node = node.next
		end_of_list = False
		while(not(end_of_list)):
			neighbors.append(node_value)
			if next_node is None:
				end_of_list = True
			else:
				node_value = next_node.vertex
				next_node = next_node.next
		
		return neighbors

	def node_degree(self, node):
		""" 
			 	It's the same as the quantity of node's edges
		"""
		return len(self.node_neighbors(node))