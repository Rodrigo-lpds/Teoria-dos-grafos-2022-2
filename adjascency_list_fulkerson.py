# Python program for the above approach
class AdjascencyListFulkerson:
    def __init__(self, file_name):
        self.adj = {}
        with open(file_name, "r") as f:
            # Given vertices
            self.V = int(f.readline()) + 1
            self.initGraph(f)

    # Function to add edges
    def addEdge(self, origin, destination, flow):
        if origin not in self.adj:
            self.adj[origin] = {destination: flow}
        else:
            self.adj[origin].update({destination: flow})

    # Function to initialize the adjacency list
    # of the given graph
    def initGraph(self, f):
        fist_line = True
        for line in f:
            if fist_line:
                fist_line = False
            else:
                edge = line.strip().split(' ')
                origin_vertex = int(edge[0])
                destination_vertex = int(edge[1])
                flow = float(edge[2])
                self.addEdge(origin_vertex, destination_vertex, flow)
