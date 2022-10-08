from tree_graph import TreeGraph

class BuildBFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.root = root
        self.tree = TreeGraph(self.root, int(self.graph.vertices_quantity))
        self.build_tree()
    
    """
    def build_tree(self):
        edges = self.graph.get_edges_array()
        queue = [self.root]
        while(len(queue)>0):
            currentVertex = queue.pop(0)
            for edge in edges:
                if(edge[0] == currentVertex):
                    if(self.tree.add_vertex_node(edge[1], currentVertex)):
                        queue.append(edge[1])
                if(edge[1] == currentVertex):
                    if(self.tree.add_vertex_node(edge[0], currentVertex)):
                        queue.append(edge[0])
    """

    def build_tree(self):
        nodes_graph = self.graph.get_nodes_graph()
        queue = [self.root]
        while(len(queue)>0):
            currentVertex = queue.pop(0)
            currentNode = nodes_graph.get(currentVertex)
            for neighbor in currentNode.get_neighbors_names():
                if(self.tree.add_vertex_node(neighbor, currentVertex)):
                    queue.append(neighbor)



    def represent_tree(self):
        self.tree.print_tree()

    def distance_between_vertex(self, vertex):
        self.tree.distance_between_vertex(vertex)
    
    def shortest_longest_path(self):
        self.tree.shortest_longest_path()