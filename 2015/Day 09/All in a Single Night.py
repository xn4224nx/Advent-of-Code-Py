# -*- coding: utf-8 -*-
"""

--- Day 9: All in a Single Night ---

What is the distance of the shortest route?

Created on Fri Dec 30 22:02:17 2022

@author: FAKENAME

https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html
"""

import sys


class Graph(object):

    def __init__(self, nodes, init_graph):

        self._nodes = nodes
        self._graph = self.construct_graph(nodes, init_graph)

    @property
    def nodes(self):
        """The nodes of the graph as a list."""
        return list(self._nodes)

    def construct_graph(self, nodes, init_graph) -> dict:
        """Make sure the graph is symetrical along every edge."""

        # Make sure every node has a key in the dict
        graph = {node: {} for node in nodes}

        # Overwite empty values with ones already known
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

        connections = []

        for outer_node in self._nodes:

            if outer_node in self._graph[node]:
                connections.append(outer_node)

        return connections

    def dist_between_nodes(self, node1, node2):
        """Returns the distance of an edge between two nodes."""
        return self._graph[node1][node2]


def dijkstra_algo(graph, start_node) -> (dict, dict):
    """Find the shortest path to each node from start_node"""

    # Get a list of the unvisited nodes in the graph
    unvisited_nodes = {node: None for node in graph.nodes}

    # Define dicts to store the best paths and previous nodes
    # Initialise the shortest path to the lragest value we can
    short_paths = {node: sys.maxsize for node in unvisited_nodes}
    prev_nodes = {}

    # Initialise the starting node to zero
    short_paths[start_node] = 0

    # Run the loop as long as there are nodes to visit
    while unvisited_nodes:

        # Find the node with the lowest value
        # (default to the first in the list)
        min_node = None

        # Iterate over all the nodes
        for node in unvisited_nodes:

            # If the node is undefined, set the min as the current node
            if not min_node:
                min_node = node

            # If the node path is smaller than current min,
            # set the new min to node
            elif short_paths[node] < short_paths[min_node]:
                min_node = node

        # get the min_node's neighbours
        neighbours = graph.node_neighbours(min_node)

        # Updates the min_node neighbours distance
        for node in neighbours:

            # Work out the current edge distance between the min_node and node
            tentative_dist = short_paths[min_node] \
                + graph.dist_between_nodes(min_node, node)

            if tentative_dist < short_paths[node]:

                # If this is shorter than the one in short_paths, replace it
                short_paths[node] = tentative_dist

                # Update the path to the previous node
                prev_nodes[node] = min_node

        else:
            # After all the neighbours have been reviewed, remove the
            # min_node from unvisited_nodes.

            del unvisited_nodes[min_node]

    return (prev_nodes, short_paths)


def dijkstra_analy(algo_tuple, target_node) -> None:

    # Find the start node
    start_node = [k for k, v in algo_tuple[1].items() if v == 0][0]

    # The path to the start node from the target node
    path = []

    node = target_node

    while node != start_node:

        path.append(node)
        node = algo_tuple[0][node]

    # Add the start node in manually
    path.append(start_node)

    print(f"Best path found - Distance {algo_tuple[1][target_node]}.")
    print(" -> ".join(reversed(path)))


nodes = ["Reykjavik", "Oslo", "Moscow", "London",
         "Rome", "Berlin", "Belgrade", "Athens"]

init_graph = {}
for node in nodes:
    init_graph[node] = {}

init_graph["Reykjavik"]["Oslo"] = 5
init_graph["Reykjavik"]["London"] = 4
init_graph["Oslo"]["Berlin"] = 1
init_graph["Oslo"]["Moscow"] = 3
init_graph["Moscow"]["Belgrade"] = 5
init_graph["Moscow"]["Athens"] = 4
init_graph["Athens"]["Belgrade"] = 1
init_graph["Rome"]["Berlin"] = 2
init_graph["Rome"]["Athens"] = 2

graph = Graph(nodes, init_graph)

ret_tuple = dijkstra_algo(graph, start_node="Reykjavik")

dijkstra_analy(ret_tuple, "Belgrade")
