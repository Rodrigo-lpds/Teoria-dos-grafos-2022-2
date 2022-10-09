from tree_graph import TreeGraph

class BuildBFS:
    def __init__(self, graph, root):
        self.graph = graph
        self.root = root
        self.tree = TreeGraph(self.root)
        self.build_tree()

    def build_tree(self):
        nodes_graph = self.graph.get_nodes_graph() # use graph representation instead
        queue = [self.root]
        while(len(queue) > 0):
            print(queue)
            currentVertex = queue.pop(0)
            
            currentNode = nodes_graph.get(currentVertex) # use graph representation instead
            for neighbor in currentNode.get_neighbors_names():
                if(self.tree.add_vertex_node(neighbor, currentVertex)):
                    queue.append(neighbor)



    def represent_tree(self):
        self.tree.print_tree()

    def distance_between_vertex(self, vertex):
        self.tree.distance_between_vertex(vertex)
    
    def shortest_longest_path(self):
        return self.tree.shortest_longest_path()