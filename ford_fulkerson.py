import copy

class FordFulkerson:
    def __init__(self, graph, source, sink):
        self.max_flow = self.ford_fulkerson(graph, source, sink)

    def ford_fulkerson(self, graph, source, sink):
        # Initialize the flow network with 0 flow on each edge
        flow = copy.deepcopy(graph)
        for u in graph:
            for v in graph[u]:
                flow.setdefault(v, {})[u] = 0
                flow.setdefault(u, {})[v] = 0

        while True:
            # Find a path from the source to the sink with residual capacity
            path = self.find_augmenting_path(graph, flow, source, sink)
            if not path:
                break

            # Determine the flow along the path
            flow_on_path = min(graph[u][v] - flow[u][v] for u, v in path)

            # Update the flow network
            for u, v in path:
                flow[u][v] += flow_on_path
                flow[v][u] -= flow_on_path

        # The maximum flow is the sum of all flow into the sink
        return sum(flow[source][v] for v in graph[source])

    def find_augmenting_path(self, graph, flow, source, sink):
        # Initialize the search queue with the source node
        queue = [source]
        visited = set()
        path = []

        while queue:
            # Pop the first node from the queue
            u = queue.pop(0)
            visited.add(u)

            # For each neighbor of the node
            for v in graph[u]:
                # If the neighbor has not been visited and there is residual capacity on the edge
                if v not in visited and graph[u][v] - flow[u][v] > 0:
                    # Add the neighbor to the queue and update the path
                    queue.append(v)
                    path.append((u, v))
                    if v == sink:
                        return path

        # If no path was found, return None
        return None
