"""
--- Day 9: All in a Single Night ---

Every year, Santa manages to deliver all of his presents in a
single night.

This year, however, he has some new locations to visit; his
elves have provided him the distances between every pair of
locations. He can start and end at any two (different)
locations he wants, but he must visit each location exactly
once. What is the shortest distance he can travel to achieve
this?

PART 1: What is the distance of the shortest route?
"""

import itertools


class DeliveryNetwork:

    def __init__(self, data_file: str):
        """
        The locations and routes that Santa visits when
        delivering presents in a single night.
        """
        self.data = {}

        # Create the graph from the data file
        with open(data_file) as fp:
            for line in fp:

                # Extract the data
                route, dist = line.split(" = ")
                loc_a, loc_b = route.split(" to ")

                # Ensure an entry for each nodes
                if loc_a not in self.data:
                    self.data[loc_a] = {}

                if loc_b not in self.data:
                    self.data[loc_b] = {}

                # Add in the edge data
                self.data[loc_b][loc_a] = int(dist)
                self.data[loc_a][loc_b] = int(dist)

    def path_len(self, path) -> int:
        """
        Determine the raw distance of a path
        """

        path_dist = 0

        for idx in range(len(path)):
            if idx == 0:
                continue

            curr_node = path[idx]
            prev_node = path[idx - 1]

            if curr_node not in self.data[prev_node]:
                return None

            path_dist += self.data[curr_node][prev_node]

        return path_dist

    def bf_shortest_path(self):
        """
        Find every possible path that goes through every node once and find the
        one with the shortest route.
        """
        path_dists = []

        for node_path in itertools.permutations(list(self.data.keys())):

            curr_path_dist = self.path_len(node_path)
            if curr_path_dist is not None:
                path_dists.append(curr_path_dist)

        return min(path_dists)


if __name__ == "__main__":
    xroute = DeliveryNetwork("./data/input.txt")
    print(f"Part 1 = {xroute.bf_shortest_path()}")
