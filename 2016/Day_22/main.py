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
"""

import re
from itertools import permutations


class NodeGrid:
    def __init__(self, datafile: str):
        node_pat = r"(\S+)\s+([0-9]+)T\s+([0-9]+)T\s+([0-9]+)T\s+([0-9]+)%"

        self.nodes = []

        with open(datafile, "r") as fp:
            for idx, line in enumerate(fp):
                if idx < 2:
                    continue

                # Extract the details of the node
                matches = re.search(node_pat, line)

                if matches is not None:
                    self.nodes.append(
                        {
                            "Addr": matches.group(1),
                            "Size": int(matches.group(2)),
                            "Used": int(matches.group(3)),
                            "Avail": int(matches.group(4)),
                        }
                    )

    def viable_pairs(self) -> list[(int, int)]:
        """
        Determine the viable node pairs in the grid in its current
        state.
        """
        node_idxs = [x for x in range(len(self.nodes))]
        pairs = []

        # Each permuation of node indexes assess viability
        for idx_a, idx_b in permutations(node_idxs, 2):

            # Node A is not empty (its Used is not zero).
            if self.nodes[idx_a]["Used"] == 0:
                continue

            # Nodes A and B are not the same node.
            if idx_a == idx_b:
                continue

            # The data on node A (its Used) would fit on node B (its Avail).
            if self.nodes[idx_a]["Used"] > self.nodes[idx_b]["Avail"]:
                continue

            pairs.append((idx_a, idx_b))

        return pairs


if __name__ == "__main__":
    pass
