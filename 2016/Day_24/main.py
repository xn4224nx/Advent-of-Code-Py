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
"""


class HVAC:
    def __init__(self, maze_file: str):
        pass

    def next_steps(self, pnt: tuple[int, int]) -> set[tuple[int, int]]:
        """
        Determine the next possible steps for a point in the HVAC system.
        """
        pass

    def fewest_steps_from_nodes(self, s_node: int, e_node: int) -> int:
        """
        What is the shortest possible steps between two named nodes in the HVAC
        map?
        """
        pass

    def fewest_steps(self) -> int:
        """
        Find the smallest number steps required to reach all of the  nodes.
        """
        pass


if __name__ == "__main__":
    pass
