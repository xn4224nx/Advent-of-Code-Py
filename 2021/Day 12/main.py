"""
--- Day 12: Passage Pathing ---

With your submarine's subterranean subsystems subsisting suboptimally, the only
way you're getting out of this cave anytime soon is by finding a path yourself.
Not just a path - the only way to know if you've found the best path is to find
all of them.

You start in the cave named start, and your destination is the cave named end.
An entry like b-d means that cave b is connected to cave d - that is, you can
move between them.

Your goal is to find the number of distinct paths that start at start, end at
end, and don't visit small caves more than once. There are two types of caves:
big caves (written in uppercase, like A) and small caves (written in lowercase,
like b). It would be a waste of time to visit any small cave more than once, but
big caves are large enough that it might be worth visiting them multiple times.
So, all paths you find should visit small caves at most once, and can visit big
caves any number of times.

Part 1:
    How many paths through this cave system are there that visit small caves at
    most once?
"""

import random


class CaveGraph:

    def __init__(self, datafile: str):

        # Define the start and end nodes
        self.start_node = "start"
        self.end_node = "end"

        # Dict of cave connecting nodes
        self.atlas = {}

        # Possible Access Routes through the cave
        self.routes = []

        # Read the text in and split by new lines into a list
        raw = open(datafile, "r").read().splitlines()

        # Split into source node and destination node
        for line in raw:

            # Extract the source and destination from the line
            source, destination = line.split("-")

            # Add both nodes to the cave atlas
            if source not in self.atlas:
                self.atlas[source] = [destination]
            else:
                self.atlas[source].append(destination)

            if destination not in self.atlas:
                self.atlas[destination] = [source]
            else:
                self.atlas[destination].append(source)

    def find_path(self) -> list[str]:
        """
        Find a paths between `start` and `end` that only goes through small
        caves once.
        """

        # Initialise a temporary path through the cave
        temp_path = [self.start_node]

        # Iterate over the possible paths through the cave system
        while temp_path[-1] != self.end_node:

            # Filter to  the viable next moves
            moves = [x for x in self.atlas[temp_path[-1]]
                     if x.lower() not in temp_path]

            # If there are no viable moves return nothing
            if not moves:
                return []

            # Out of the connected cave select the next move
            temp_path.append(random.choice(moves))

        return temp_path

    def find_all_paths(self, limit: int = 1000):
        """
        Find all possible paths through a cave that only goes through small
        caves once.

        The algorithm times out after the limit.
        """

        found_paths = set()

        while limit > 0:

            # Generate a path
            tmp_path = tuple(self.find_path())

            # Check if it has been seen before
            if tmp_path in found_paths:
                limit -= 1
            else:
                found_paths.add(tmp_path)

        # Convert to a list
        self.routes = list(found_paths)

        # Remove the empty path
        self.routes = [x for x in self.routes if len(x) > 0]


sample = CaveGraph("./data/sample.txt")
sample.find_all_paths()

print(f"Part 1: {len(sample.routes)}")
