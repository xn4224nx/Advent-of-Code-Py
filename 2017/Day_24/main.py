"""
--- Day 24: Electromagnetic Moat ---

The CPU itself is a large, black building surrounded by a bottomless pit.
Enormous metal tubes extend outward from the side of the building at regular
intervals and descend down into the void. There's no way to cross, but you need
to get inside.

No way, of course, other than building a bridge out of the magnetic components
strewn about nearby.

Each component has two ports, one on each end. The ports come in all different
types, and only matching types can be connected. You take an inventory of the
components by their port types (your puzzle input). Each port is identified by
the number of pins it uses; more pins mean a stronger connection for your
bridge. A 3/7 component, for example, has a type-3 port on one side, and a
type-7 port on the other.

Your side of the pit is metallic; a perfect surface to connect a magnetic,
zero-pin port. Because of this, the first port you use must be of type 0. It
doesn't matter what type of port you end with; your goal is just to make the
bridge as strong as possible.

The strength of a bridge is the sum of the port types in each component. For
example, if your bridge is made of components 0/3, 3/7, and 7/4, your bridge
has a strength of 0+3 + 3+7 + 7+4 = 24.

For example, suppose you had the following components:

    0/2
    2/2
    2/3
    3/4
    3/5
    0/1
    10/1
    9/10

With them, you could make the following valid bridges:

    0/1
    0/1--10/1
    0/1--10/1--9/10
    0/2
    0/2--2/3
    0/2--2/3--3/4
    0/2--2/3--3/5
    0/2--2/2
    0/2--2/2--2/3
    0/2--2/2--2/3--3/4
    0/2--2/2--2/3--3/5

(Note how, as shown by 10/1, order of ports within a component doesn't matter.
However, you may only use each port on a component once.)

Of these bridges, the strongest one is 0/1--10/1--9/10; it has a strength of
0+1 + 1+10 + 10+9 = 31.

PART 1: What is the strength of the strongest bridge you can make with the
        components you have available?
"""

from itertools import permutations


class BridgeFinder:
    def __init__(self, component_file: str):
        with open(component_file, "r") as fp:
            self.comps = [
                tuple(map(int, x.split("/", maxsplit=1))) for x in fp.readlines()
            ]

    def bridge_strength(self, component_idxs: tuple[int]) -> int:
        """
        Calculate the total strength of a combination of bridge components.
        """
        return sum([self.comps[x][0] + self.comps[x][1] for x in component_idxs])

    def is_component_comb_valid(self, component_idxs: tuple[int]) -> bool:
        """
        Determine if a combination of components is a valid bridge.
        """

        # The bridge must start with zero
        if 0 not in self.comps[component_idxs[0]]:
            return False

        # Construct the bridge as a list of the components
        bridge = [0, max(self.comps[component_idxs[0]])]
        for idx in component_idxs[1:]:

            # Check there is a matching component in this segment
            if bridge[-1] not in self.comps[idx]:
                return False

            bridge.append(bridge[-1])

            # Determine the non matching component and add it to the end
            if self.comps[idx][0] == bridge[-1]:
                bridge.append(self.comps[idx][1])
            else:
                bridge.append(self.comps[idx][0])

        return True

    def find_strongest_bridge(self) -> int:
        """
        Check all valid ways to build a bridge with the supplied components and
        return the strength of the strongest possible bridge.
        """

        # Keep a record of all seen bridges starting with single component ones
        bridge_strengths = {}
        curr_bridges = {(x,) for x in range(len(self.comps)) if 0 in self.comps[x]}

        # Keep exploring possible bridges till no more can be made
        while curr_bridges:
            new_bridges = set()

            # For each previous bridge see if it can be extended
            for prev_bridge in curr_bridges:

                # Check if any component can be added
                for comp_idx in range(len(self.comps)):

                    # No duplicate components allowed
                    if comp_idx in prev_bridge:
                        continue

                    tmp_bridge = prev_bridge + (comp_idx,)

                    # See if this addition would make a valid bridge
                    if self.is_component_comb_valid(tmp_bridge):
                        new_bridges.add(tmp_bridge)

            # Save the strenghts of the older bridges
            bridge_strengths.update({x: self.bridge_strength(x) for x in curr_bridges})

            # Prepare for the next loop iteration
            curr_bridges = new_bridges

        # return the biggest strenght found
        return max(bridge_strengths.values())


if __name__ == "__main__":
    print(f"Part 1 = {BridgeFinder("./data/input.txt").find_strongest_bridge()}")
