"""
--- Day 22: Grid Computing ---

You gain access to a massive storage cluster arranged in a grid; each storage
node is only connected to the four nodes directly adjacent to it (three if the
node is on an edge, two if it's in a corner).

You can directly access data only on node /dev/grid/node-x0-y0, but you can
perform some limited actions on the other nodes:

    -   You can get the disk usage of all nodes (via df). The result of doing
        this is in your puzzle input.

    -   You can instruct a node to move (not copy) all of its data to an
        adjacent node (if the destination node has enough space to receive the
        data). The sending node is left empty after this operation.

Nodes are named by their position: the node named node-x10-y10 is adjacent to
nodes node-x9-y10, node-x11-y10, node-x10-y9, and node-x10-y11.

Before you begin, you need to understand the arrangement of data on these nodes.
Even though you can only move data between directly connected nodes, you're
going to need to rearrange a lot of the data to get access to the data you need.
Therefore, you need to work out how you might be able to shift data around.

To do this, you'd like to count the number of viable pairs of nodes. A viable
pair is any two nodes (A,B), regardless of whether they are directly connected,
such that:

    -   Node A is not empty (its Used is not zero).

    -   Nodes A and B are not the same node.

    -   The data on node A (its Used) would fit on node B (its Avail).

PART 1: How many viable pairs of nodes are there?

Now that you have a better understanding of the grid, it's time to get to work.

Your goal is to gain access to the data which begins in the node with y=0 and
the highest x (that is, the node in the top-right corner).

PART 2: What is the fewest number of steps required to move your goal data to
        node-x0-y0?
"""

import sys
import re
import numpy as np
from itertools import permutations


class NodeGrid:
    def __init__(self, datafile: str):
        node_pat = r"x(\d+)\-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%"
        grid_max = (0, 0)
        node_usage = []
        node_size = []
        self.node_loc = []

        # Read the raw data from file
        with open(datafile, "r") as fp:
            for idx, line in enumerate(fp):
                if idx < 2:
                    continue

                # Extract the details of the node
                matches = re.search(node_pat, line)

                if matches is not None:
                    node_size.append(int(matches.group(3)))
                    node_usage.append(int(matches.group(4)))
                    self.node_loc.append((int(matches.group(1)), int(matches.group(2))))

        # Create the 2D node grid as full of partial nodes
        self.nodes = ["." for x in range(len(self.node_loc))]

        # Find the empty node
        for empt_idx in range(len(self.node_loc)):
            if node_usage[empt_idx] == 0:
                self.nodes[empt_idx] = "_"
                break
        else:
            raise Exception("No empty node found!")

        # Catagorise the full nodes
        for idx in range(len(self.node_loc)):
            if node_usage[idx] > node_size[empt_idx]:
                self.nodes[idx] = "#"

        # Find the goal node
        max_x = 0
        max_x_idx = 0

        for idx in range(len(self.node_loc)):
            if self.node_loc[idx][1] == 0 and self.node_loc[idx][0] > max_x:
                max_x = self.node_loc[idx][0]
                max_x_idx = idx

        self.nodes[max_x_idx] = "G"

    def are_nodes_neighbours(self, node_a_idx: int, node_b_idx: int) -> bool:
        """
        Determine if two nodes are next to one another.
        """
        if node_a_idx == node_b_idx:
            return False

        a_x, a_y = self.node_loc[node_a_idx]
        b_x, b_y = self.node_loc[node_b_idx]

        if (a_x == b_x and (a_y - 1 == b_y or a_y + 1 == b_y)) or (
            a_y == b_y and (a_x - 1 == b_x or a_x + 1 == b_x)
        ):
            return True
        else:
            return False

    def viable_pairs(
        self, curr_node_usage: tuple[str], next_door: bool = False
    ) -> list[(int, int)]:
        """
        Determine the viable node pairs in the grid in its current
        state.
        """
        pairs = []

        # Each permuation of node indexes assess viability
        for idx_a, idx_b in permutations([x for x in range(len(self.nodes))], 2):

            # Nodes A and B are not the same node.
            if idx_a == idx_b:
                continue

            # Ensure there is space for a move
            if curr_node_usage[idx_b] != "_":
                continue

            # Ensure there is data to move
            if curr_node_usage[idx_a] not in [".", "G"]:
                continue

            # Test if the nodes are next to each other
            if next_door and self.are_nodes_neighbours(idx_a, idx_b):
                pairs.append((idx_a, idx_b))
            elif not next_door:
                pairs.append((idx_a, idx_b))

        return pairs

    def moves_empty_to_data(self) -> int:
        """
        Find the shortest path to move the empty space to the node with
        the cruical data. Return the minimum moves required to get there.
        """
        unvisted_nodes = set([x for x in range(len(self.nodes))])
        dist_to_nodes = {x: sys.maxsize for x in range(len(self.nodes))}
        dest_node = self.nodes.index("G")

        # Start at the empty node
        dist_to_nodes[self.nodes.index("_")] = 0

        while True:

            # Pick the unvisited node with the smallest distance
            curr_min = sys.maxsize
            curr_min_idx = 0
            for n_idx in unvisted_nodes:
                if dist_to_nodes[n_idx] < curr_min:
                    curr_min = dist_to_nodes[n_idx]
                    curr_min_idx = n_idx

            # Abort the loop if the destination is reached
            if curr_min_idx == dest_node:
                break

            # Find all the neighbours of the current minimum and set their dist
            for n_idx in unvisted_nodes:
                if self.are_nodes_neighbours(n_idx, curr_min_idx):
                    dist_to_nodes[n_idx] = curr_min + 1

            unvisted_nodes.remove(curr_min_idx)

        return dist_to_nodes[dest_node]

    def data_extract_min_moves(self) -> int:
        """
        Calculate the total number of moves to get the target data 'G' to the
        access node at 0,0.
        """
        moves_for_empty = self.moves_empty_to_data()
        return moves_for_empty + 5 * self.node_loc[self.nodes.index("G")][0] + 1


if __name__ == "__main__":
    cluster = NodeGrid("./data/input.txt")
    print(f"Part 1 = {len(cluster.viable_pairs(cluster.nodes))}")
    print(f"Part 2 = {cluster.data_extract_min_moves()}")
