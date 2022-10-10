from tree_graph import TreeGraph

class BuildDFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.root = root
        self.tree = TreeGraph(self.root)
        self.build_tree()

    def build_tree(self):
        queue = [self.root]
        explored_vertices = []
        while(len(queue) > 0):
            currentVertex = queue.pop(0)
            if currentVertex not in explored_vertices:
                explored_vertices.append(currentVertex)
                for neighbor in self.graph.node_neighbors(currentVertex):
                    self.tree.add_vertex_node(neighbor, currentVertex)
                    queue.append(neighbor)


    def represent_tree(self):
        self.tree.print_tree()


