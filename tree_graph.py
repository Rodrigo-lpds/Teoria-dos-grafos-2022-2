
class TreeGraph:
    def __init__(self, root):
        self.tree_graph = {}
        self.insert_vertex_node(root, 0, 0)

    def add_vertex_node(self, vertex, dad):
        """
		Try to add a Vertex to the tree and calculate his nivel, return true if vertex doesn't exist in the tree
		"""
        if(self.tree_graph.get(vertex) is None):
            nivel = self.tree_graph[dad].nivel + 1
            self.insert_vertex_node(vertex, dad, nivel)
            return True
        else:
            return False

    def insert_vertex_node(self, vertex, dad, nivel):
        """
		Insert a Vertex in the tree
		"""
        node = TreeNode(vertex, dad, nivel, True)
        self.tree_graph.update({vertex: node})
    
    def print_tree(self):
        for value in self.tree_graph.values():
            value.print_node()
        print()


class TreeNode:
    def __init__(self, vertex, dad, nivel, is_explored):
        self.vertex = vertex
        self.explored = is_explored
        self.dad = dad
        self.nivel = nivel

    def print_node(self):
        print("vertex:", self.vertex, "dad:", self.dad, "nivel:", self.nivel)
    
    def set_uncovered(self, is_explored):
        self.explored = is_explored
    
    