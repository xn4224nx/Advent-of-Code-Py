class Graph(object):
    """
    A symmetrical graph of nodes and edges defined by an input of nodes and the
    edges between them.
    """
    def __init__(self, nodes, init_graph):

        self.nodes = nodes
        self.graph = self.construct_graph(init_graph)

    def construct_graph(self, init_graph) -> dict:
        """Make sure the graph is symmetrical along every edge."""

        # Make sure every node has a key in the dict
        graph = {node: {} for node in self.nodes}

        # Overwrite empty values with ones already known
        graph.update(init_graph)

        # For each node in the graph
        for node, edges in graph.items():

            # For each node the outer node via an edge
            for adjacent_node, distance in edges.items():

                # Check that the edge to the outer node is in the
                # edges for the adjacent_node and if not create it
                if node not in graph[adjacent_node]:
                    graph[adjacent_node][node] = distance

        return graph

    def node_neighbours(self, node) -> list:
        """Returns the neighbors of a node in a list."""
        return list(self.graph[node].keys())

    def nearest_neighbour(self, node) -> str:
        """Returns the nearest neighbour to the node."""
        return min(self.graph[node], key=self.graph[node])

    def dist_between_nodes(self, node1, node2):
        """Returns the distance of an edge between two nodes."""
        return self.graph[node1][node2]
