import math
import random

class Graph: 
	def __init__(self, file_name):
		self.file_name = file_name

		self.readed_graph 		= self.read_graph_file()
		self.vertices_quantity 	= self.get_vertices_quantity()
		self.edges_quantity 		= self.get_edges_quantity()

	def read_graph_file(self):
		"""
		Reads a graph file and returns a list of all the lines in the file.
		"""
		with open(self.file_name, 'r') as file:
			return file.read().splitlines()


	def get_vertices_quantity(self): 
		"""
		Returns the vertices of the graph.
		"""
		return int(self.readed_graph[0].rstrip("\n"))

	def get_edges_quantity(self):
		"""
		Returns the edges of the graph.
		"""
		return len(self.readed_graph) - 1	