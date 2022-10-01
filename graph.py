# to do: minimum graph degree, maximum graph degree, mean graph degree and median graph degree
class Graph: 
	def __init__(self, file_name):
		self.file_name = file_name

		self.readed_graph 			= self.read_graph_file()
		self.vertices_quantity 	= self.get_vertices_quantity()
		self.edges_quantity 		= self.get_edges_quantity()
		self.nodes_graph = {}

	def read_graph_file(self):
		"""
		Reads a graph file and returns a list of all the lines in the file.
		"""
		with open(self.file_name, 'r') as file:
			return file.read().splitlines()
	
	def get_edges_array(self):
		"""
		Returns a matriz with all edges of the graph. Example of output: [[1,2], [1,3], [3,2]]
		"""
		edges = []
		for line in self.readed_graph[1:]:
			line = line.split(' ')
			edges.append([int(line[0]), int(line[1])])
		return edges

	def get_nodes_graph(self):
		"""
		Returns a dictionary of Nodes from the graph 
		"""
		if(len(self.nodes_graph)>0): 
			return self.nodes_graph 
		self.build_nodes_graph()
		return self.nodes_graph 

	def build_nodes_graph(self):
		"""
		Build a dictionary of Nodes from the graph 
		"""
		edges = self.get_edges_array()
		self.nodes_graph = {}
		vertices_in_graph = [False] * self.vertices_quantity
		node0 = Node(None)
		node1 = Node(None)
		for edge in edges:
			index = edge[0]-1
			if(not vertices_in_graph[index]):
				vertices_in_graph[index] = True
				node0 = Node(edge[0])
				self.nodes_graph.update({edge[0]: node0})
			else:
				node0 = self.nodes_graph.get(edge[0])

			index = edge[1]-1
			if(not vertices_in_graph[index]):
				vertices_in_graph[index] = True
				node1 = Node(edge[1])
				self.nodes_graph.update({edge[1]: node1})
			else:
				node1 = self.nodes_graph.get(edge[1])

			node0.add_neighbor(node1)
			node1.add_neighbor(node0)
	
	"""
	def debug_nodes_graph(self):
		for vertex in self.nodes_graph.values():
			print('vertex:',vertex.name)
			print(vertex.get_neighbors_names())
	"""

			

	def get_vertices_quantity(self): 
		"""
		Returns the vertices quantity of the graph.
		"""
		return int(self.readed_graph[0].rstrip("\n"))

	def get_edges_quantity(self):
		"""
		Returns the edges quantity of the graph.
		"""
		return len(self.readed_graph) - 1	

class Node:
	def __init__(self, name):
		self.name = name
		self.neighbors_node = []
		self.neighbors_name = []

	def add_neighbor(self, vertex):
		self.neighbors_node.append(vertex)
		self.neighbors_name.append(vertex.name)
	
	def get_neighbors_nodes(self):
		return self.neighbors_node

	def get_neighbors_names(self):
		return self.neighbors_name
