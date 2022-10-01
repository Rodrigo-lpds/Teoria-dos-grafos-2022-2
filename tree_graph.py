
class TreeGraph:
    def __init__(self, root, vertex_qty):
        self.tree_graph = {}
        self.vertices_in_tree = [False] * vertex_qty
        self.insert_vertex_node(root, 0, 0)

    def add_vertex_node(self, vertex, dad):
        """
		Try to add a Vertex to the tree and calculate his nivel, return true if vertex doesn't exist in the tree
		"""
        if(not (self.vertices_in_tree[vertex-1])):
            nivel = self.tree_graph[dad].nivel + 1
            self.insert_vertex_node(vertex, dad, nivel)
            return True
        else:
            return False

    def insert_vertex_node(self, vertex, dad, nivel):
        """
		Insert a Vertex in the tree
		"""
        node = VertexNode(vertex, dad, nivel)
        self.vertices_in_tree[vertex-1] = True
        self.tree_graph.update({vertex: node})
    
    def print_tree(self):
        for value in self.tree_graph.values():
            value.print_node()


class VertexNode:
    def __init__(self, vertex, dad, nivel):
        self.vertex = vertex
        self.dad = dad
        self.nivel = nivel

    def print_node(self):
        print("vertex:", self.vertex, "dad:", self.dad, "nivel:", self.nivel)
    
    