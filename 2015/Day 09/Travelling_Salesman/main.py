"""
Travelling Salesman Solver

A code base to solve travelling salesman problems in python.
"""

import re
import random
from graph import Graph

graph_re = r"([a-zA-Z]+) to ([a-zA-Z]+) = (\d+)"

# Load the data
data = open("data/input.txt").read().splitlines()

graph_data_dict = {}

# Create a dict of graph links
for line in data:

    # Split the line
    node1, node2, dist = re.findall(graph_re, line)[0]

    # Check the locations is in the dict
    if node1 not in graph_data_dict:
        graph_data_dict[node1] = {}

    if node2 not in graph_data_dict:
        graph_data_dict[node2] = {}

    # Add the line data into the dict
    graph_data_dict[node1][node2] = dist
    graph_data_dict[node2][node1] = dist

# Create the graph object from the data from disk
graph = Graph(list(graph_data_dict.keys()), graph_data_dict)


def ts_rnd_solver(ts_graph, neigh_pick="random") -> (int, list):
    """Nearest Neighbour Algorithm"""

    # Pick a random node to start on
    start_node = random.choice(ts_graph.nodes)

    # Define a dict of the unvisited nodes
    unvisited_nodes = {node: None for node in ts_graph.nodes}

    # Setup the node for the loop
    cur_node = start_node

    # Keep a record of how good this loop was and what is consisted of
    loop_route = []
    loop_len = 0

    # While there are nodes still to visit
    while unvisited_nodes:

        # Pick a neighbour to the node
        neighbours = graph.graph[cur_node]

        next_node = None

        if neigh_pick == "closest":

            # For each neighbour check if it has been
            # visited and pick the closest one
            for node, val in neighbours.items():

                # Don't pick nodes that have been seen before
                if node not in unvisited_nodes:
                    continue

                # If no node has been picked use this one
                if not next_node:
                    next_node = node

                # If this node is closer than the current one, replace it
                elif val < neighbours[next_node]:
                    next_node = node

        elif neigh_pick == "random":

            # Remove nodes if they are not unvisited
            pos_nodes = [node for node in neighbours
                         if node in unvisited_nodes]

            # Pick a random node
            if pos_nodes:
                next_node = random.choice(pos_nodes)

        # Remove the current node from visited nodes
        del unvisited_nodes[cur_node]

        # Add to the route details
        loop_route.append(cur_node)

        # Check that a node has been found
        if not next_node:

            # Check to see if one of the neighbours
            # of this node is the start_node
            # and there are no more Nodes to visit
            if start_node in neighbours and not unvisited_nodes:
                break
            else:
                raise Exception(f"Loop could not be closed on "
                                f"the node {cur_node}")

        # Save what the route was
        loop_len += int(graph.graph[cur_node][next_node])

        # Setup for the next loop iteration
        cur_node = next_node

    # If you want to show loop results
    if False:
        print(loop_route)
        print(loop_len)

    return loop_len, loop_route


possible_loops = {}

for i in range(1000000):

    loop_length, loop_path = ts_rnd_solver(graph)

    possible_loops[loop_length] = loop_path

print(f"Shortest route is {min(possible_loops)} with route "
      f"{possible_loops[min(possible_loops)]}.")

print(f"Longest route is {max(possible_loops)} with route "
      f"{possible_loops[max(possible_loops)]}.")
