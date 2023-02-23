"""
--- Day 12: Digital Plumber ---

Programs in this village communicate using a fixed system of pipes. Messages
are passed between programs using these pipes, but most programs aren't
connected to each other directly. Instead, programs pass messages between each
other until the message reaches the intended recipient.

Each program has one or more programs with which it can communicate, and these
pipes are bidirectional; if 8 says it can communicate with 11, then 11 will say
it can communicate with 8.

# Part 1
You need to figure out how many programs are in the group that contains program
ID 0.

# Part 2
Find how many non-connected groups there are.
"""

import random


class ProgramVillage:

    def __init__(self, node_record_fp: str):

        self.node_record = {}

        # Load the communication record from file
        with open(node_record_fp, "r") as file:
            for line in file:

                raw = line.strip().split(" <-> ")
                self.node_record[int(raw[0])] = [int(x.strip())
                                            for x in raw[1].split(",")]

    def connected_nodes(self, node_2_be_investigated: int) -> list[int]:
        """Find all the other nodes connected to this node."""

        found_nodes = 1
        connected_nodes = [node_2_be_investigated]

        while found_nodes > 0:
            found_nodes = 0

            for node in self.node_record:

                # Don't look into node already identified as connected
                if node in connected_nodes:
                    continue

                # Determine if this node is linked to any in `connected_nodes`
                for conn_node in connected_nodes:
                    if conn_node in self.node_record[node]:
                        found_nodes += 1
                        connected_nodes.append(node)
                        break

        return connected_nodes

    def count_groups(self):
        """Find out how many non-connected groups are in the village."""

        found_groups = []
        ungrouped_nodes = list(self.node_record.keys())

        while ungrouped_nodes:

            # Pick random node to start the search
            curr_node = random.choice(ungrouped_nodes)

            # Find all the nodes in its group
            curr_group = self.connected_nodes(curr_node)
            found_groups.append(curr_group)

            # Remove those nodes from the list of nodes to visit
            ungrouped_nodes = [x for x in ungrouped_nodes
                               if x not in curr_group]

        return len(found_groups)


sample = ProgramVillage("data/input.txt")

# Part 1
print(len(sample.connected_nodes(0)))

# Part 2
print(sample.count_groups())