# Python program for the above approach
class AdjascencyListFulkerson:
    def __init__(self, file_name):
        self.adj = {}
        with open(file_name, "r") as f:
            # Given vertices
            self.V = int(f.readline()) + 1
            self.initGraph(f)

    # Function to add edges
    def addEdge(self, u, v):
        if u not in self.adj:
            self.adj[u] = {v[0]: v[1]}
        else:
            self.adj[u].update({v[0]: v[1]})

    # Function to initialize the adjacency list
    # of the given graph
    def initGraph(self, f):
        fist_line = True
        for line in f:
            if fist_line:
                fist_line = False
            else:
                edge = line.strip().split(' ')
                self.addEdge(int(edge[0]), [int(edge[1]), float(edge[2])])
