# to do: minimum graph degree, maximum graph degree, mean graph degree and median graph degree
from tabnanny import verbose

class AdjNode:
	def __init__(self, value):
		self.vertex = value
		self.cost = 0
		self.next = None
  
class AdjascencyListV2:
	def __init__(self, file_name, weighted=False):
		self.file_name = file_name
		self.weighted = weighted

		f = open(self.file_name, "r")
		self.vertices_quantity = int(f.readline()) + 1

		self.list = [None] * self.vertices_quantity
		self.build_representation()


	def build_representation(self):
		fist_line = True
		with open(self.file_name) as f:
			for line in f:
				if fist_line != True:
					edge = line.strip().split(' ')
					if self.weighted == True:
						self.add_edge([int(edge[0]), float(edge[2])], [int(edge[1]), float(edge[2])])
					else:
						self.add_edge(int(edge[0]), int(edge[1]))

				else:
					fist_line = False

    # Add edges
	def add_edge(self, s, d):
		node = AdjNode(d)
		node.next = self.list[s[0]]
		node.cost = d[1]
		self.list[s[0]] = node

		node = AdjNode(s)
		node.next = self.list[d[0]]
		node.cost = d[1]
		self.list[d[0]] = node

	def vertices(self):
		nodes = set()
		for node in self.list:
			if node is not None:
				nodes.add(self.list.index(node))
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
	
	#def node_cost(self, node):