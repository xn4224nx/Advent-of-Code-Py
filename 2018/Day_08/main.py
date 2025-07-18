"""
--- Day 8: Memory Maneuver ---

The sleigh is much easier to pull than you'd expect for something its weight.
Unfortunately, neither you nor the Elves know which way the North Pole is from
here.

You check your wrist device for anything that might help. It seems to have some
kind of navigation system! Activating the navigation system produces more bad
news: "Failed to start navigation system. Could not read software license
file."

The navigation system's license file consists of a list of numbers (your puzzle
input). The numbers define a data structure which, when processed, produces
some kind of tree that can be used to calculate the license number.

The tree is made up of nodes; a single, outermost node forms the tree's root,
and it contains all other nodes in the tree (or contains nodes that contain
nodes, and so on).

Specifically, a node consists of:

        -   A header, which is always exactly two numbers:

            -   The quantity of child nodes.

            -   The quantity of metadata entries.

        -   Zero or more child nodes (as specified in the header).

        -   One or more metadata entries (as specified in the header).

Each child node is itself a node that has its own header, child nodes, and
metadata. For example:

    2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
    A----------------------------------
        B----------- C-----------
                        D-----

In this example, each node of the tree is also marked with an underline
starting with a letter for easier identification. In it, there are four nodes:

    -   A, which has 2 child nodes (B, C) and 3 metadata entries (1, 1, 2).

    -   B, which has 0 child nodes and 3 metadata entries (10, 11, 12).

    -   C, which has 1 child node (D) and 1 metadata entry (2).

    -   D, which has 0 child nodes and 1 metadata entry (99).

The first check done on the license file is to simply add up all of the
metadata entries. In this example, that sum is 1+1+2+10+11+12+2+99=138.

PART 1: What is the sum of all metadata entries?
"""


class Tree:
    def __init__(self, node_file: str):
        with open(node_file, "r") as fp:
            self.raw_info = list(map(int, fp.read().strip().split()))

    def node_metadata_sum(self) -> int:
        """
        For all the nodes in the tree sum their constituant metadata.
        """
        children = [self.raw_info[0]]
        meta_cnt = [self.raw_info[1]]
        node_data = []

        # Extract the node meta data
        tree_idx = 2
        while tree_idx < len(self.raw_info):

            # If the current node has nodes below it save it and move on
            if children[-1] > 0:
                children[-1] -= 1
                children.append(self.raw_info[tree_idx])
                meta_cnt.append(self.raw_info[tree_idx + 1])
                tree_idx += 2

            # Otherwise save the node data and then move along
            else:
                node_data += self.raw_info[tree_idx : tree_idx + meta_cnt[-1]]
                tree_idx += meta_cnt[-1]
                children.pop()
                meta_cnt.pop()

        return sum(node_data)


if __name__ == "__main__":
    pass
