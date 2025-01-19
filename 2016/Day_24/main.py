"""
--- Day 24: Air Duct Spelunking ---

You've finally met your match; the doors that provide access to the roof are
locked tight, and all of the controls and related electronics are inaccessible.
You simply can't reach them.

The robot that cleans the air ducts, however, can.

It's not a very fast little robot, but you reconfigure it to be able to
interface with some of the exposed wires that have been routed through the HVAC
system. If you can direct it to each of those locations, you should be able to
bypass the security controls.

You extract the duct layout for this area from some blueprints you acquired and
create a map with the relevant locations marked (your puzzle input). 0 is your
current location, from which the cleaning robot embarks; the other numbers are
(in no particular order) the locations the robot needs to visit at least once
each. Walls are marked as #, and open passages are marked as .. Numbers behave
like open passages.

Since the robot isn't very fast, you need to find it the shortest route. This
path is the fewest steps required to start at 0 and then visit every other
location at least once.

PART 1: Given your actual map, and starting from location 0, what is the fewest
        number of steps required to visit every non-0 number marked on the map
        at least once?

Of course, if you leave the cleaning robot somewhere weird, someone is bound to
notice.

PART 2: What is the fewest number of steps required to start at 0, visit every
        non-0 number marked on the map at least once, and then return to 0?
"""

from itertools import combinations, permutations


class HVAC:
    def __init__(self, maze_file: str):
        self.nodes = {}
        self.free = set()

        with open(maze_file, "r") as fp:
            for y_idx, line in enumerate(fp):
                for x_idx, char in enumerate(line):

                    # Catch a node
                    if char.isdigit():
                        self.nodes[int(char)] = (x_idx, y_idx)
                        self.free.add((x_idx, y_idx))

                    # Catch empty space
                    elif char == ".":
                        self.free.add((x_idx, y_idx))

    def next_steps(self, pnt: tuple[int, int]) -> set[tuple[int, int]]:
        """
        Determine the next possible steps for a point in the HVAC system.
        """
        return {
            x
            for x in [
                (pnt[0] - 1, pnt[1]),
                (pnt[0] + 1, pnt[1]),
                (pnt[0], pnt[1] - 1),
                (pnt[0], pnt[1] + 1),
            ]
            if x in self.free
        }

    def fewest_steps_from_nodes(
        self, s_node: int, e_node: int, revisit_allowed: bool = False
    ) -> int:
        """
        What is the shortest possible steps between two named nodes in the HVAC
        map?
        """
        mv_idx = 0
        epnt = self.nodes[e_node]
        curr_pnts = {self.nodes[s_node]}
        seen_pnts = {self.nodes[s_node]}

        # Move out from the start point in all directions
        while True:
            mv_idx += 1
            nxt_pnts = set()

            # Determine all the next possible steps
            for pnt in curr_pnts:
                if revisit_allowed:
                    nxt_pnts |= self.next_steps(pnt)
                else:
                    for n_pnt in self.next_steps(pnt):
                        if n_pnt not in seen_pnts:
                            nxt_pnts.add(n_pnt)
                            seen_pnts.add(n_pnt)

            # Check for a solution
            if epnt in nxt_pnts:
                break

            curr_pnts = nxt_pnts

        return mv_idx

    def fewest_steps(self, return_bot: bool = False) -> int:
        """
        Find the smallest number steps required to reach all of the  nodes.
        """
        route_lens = []
        other_nodes = [x for x in self.nodes.keys() if x != 0]

        # Calculate the minimum number of steps between each node
        min_lens = {
            tuple(sorted([s_pnt, e_pnt])): self.fewest_steps_from_nodes(s_pnt, e_pnt)
            for s_pnt, e_pnt in combinations(self.nodes.keys(), 2)
        }

        # Find all possible permutions of how the nodes could be visited.
        for node_route in permutations(other_nodes):
            nroute = [0] + list(node_route)

            if return_bot:
                nroute.append(0)

            # Calculate the distance this route would take by linking the nodes
            route_lens.append(
                sum(
                    [
                        min_lens[tuple(sorted([nroute[idx], nroute[idx + 1]]))]
                        for idx in range(len(nroute) - 1)
                    ]
                )
            )
        return min(route_lens)


if __name__ == "__main__":
    print(f"Part 1 = {HVAC('./data/input.txt').fewest_steps()}")
    print(f"Part 2 = {HVAC('./data/input.txt').fewest_steps(True)}")
