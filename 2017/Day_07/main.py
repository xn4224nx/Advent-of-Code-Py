r"""
--- Day 7: Recursive Circus ---

Wandering further through the circuits of the computer, you come upon a tower
of programs that have gotten themselves into a bit of trouble. A recursive
algorithm has gotten out of hand, and now they're balanced precariously in a
large tower.

One program at the bottom supports the entire tower. It's holding a large disc,
and on the disc are balanced several more sub-towers. At the bottom of these
sub-towers, standing on the bottom disc, are other programs, each holding their
own disc, and so on. At the very tops of these sub-sub-sub-...-towers, many
programs stand simply keeping the disc below them balanced but with no disc of
their own.

You offer to help, but first you need to understand the structure of these
towers. You ask each program to yell out their name, their weight, and (if
they're holding a disc) the names of the programs immediately above them
balancing on that disc. You write this information down (your puzzle input).
Unfortunately, in their panic, they don't do this in an orderly fashion; by the
time you're done, you're not sure which program gave which information.

For example, if your list is the following:

    pbga (66)
    xhth (57)
    ebii (61)
    havc (66)
    ktlj (57)
    fwft (72) -> ktlj, cntj, xhth
    qoyq (66)
    padx (45) -> pbga, havc, qoyq
    tknk (41) -> ugml, padx, fwft
    jptl (61)
    ugml (68) -> gyxo, ebii, jptl
    gyxo (61)
    cntj (57)

...then you would be able to recreate the structure of the towers that looks
like this:
                    gyxo
                /
            ugml - ebii
        /      \
        |         jptl
        |
        |         pbga
        /        /
    tknk --- padx - havc
        \        \
        |         qoyq
        |
        |         ktlj
        \      /
            fwft - cntj
                \
                    xhth

In this example, tknk is at the bottom of the tower (the bottom program), and
is holding up ugml, padx, and fwft. Those programs are, in turn, holding up
other programs; in this example, none of those programs are holding up any
other programs, and are all the tops of their own towers. (The actual tower
balancing in front of you is much larger.)

PART 1: Before you're ready to help them, you need to make sure your
        information is correct. What is the name of the bottom program?

The programs explain the situation: they can't get down. Rather, they could get
down, if they weren't expending all of their energy trying to keep the tower
balanced. Apparently, one program has the wrong weight, and until it's fixed,
they're stuck here.

For any program holding a disc, each program standing on that disc forms a sub-
tower. Each of those sub-towers are supposed to be the same weight, or the disc
itself isn't balanced. The weight of a tower is the sum of the weights of the
programs in that tower.

In the example above, this means that for ugml's disc to be balanced, gyxo,
ebii, and jptl must all have the same weight, and they do: 61.

However, for tknk to be balanced, each of the programs standing on its disc and
all programs above it must each match. This means that the following sums must
all be the same:

    -   ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251

    -   padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243

    -   fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243

As you can see, tknk's disc is unbalanced: ugml's stack is heavier than the
other two. Even though the nodes above ugml are balanced, ugml itself is too
heavy: it needs to be 8 units lighter for its stack to weigh 243 and keep the
towers balanced. If this change were made, its weight would be 60.

PART 2: Given that exactly one program is the wrong weight, what would its
        weight need to be to balance the entire tower?
"""

import re
import collections


class ProgramTower:
    def __init__(self, tower_status: str):
        self.disks = {}
        re_grp = re.compile(r"([a-z]+) \(([0-9]+)\)( -> )?([a-z, ]+)?")

        # Iterate over lines in the file
        with open(tower_status, "r") as fp:
            for line in fp.readlines():
                parts = re_grp.match(line)

                # Extract the name and weight
                self.disks[parts.group(1)] = {}
                self.disks[parts.group(1)]["weight"] = int(parts.group(2))

                # Detect disks above this one
                if parts.group(3) is not None:
                    tmp_above = [x.strip() for x in parts.group(4).split(",")]
                else:
                    tmp_above = []

                self.disks[parts.group(1)]["above"] = tmp_above

    def bottom_disk(self) -> str:
        """
        Determine the name of the disk at the bottom of the program tower. Do
        this by finding a key that doesn't appear in any other disks above
        list while still having disks above itself.
        """
        disks_with_above = [
            disk for disk, disk_dets in self.disks.items() if disk_dets["above"]
        ]

        # Check each disk to make sure no other disk is above it
        for disk_bot in disks_with_above:
            for disk_ch in disks_with_above:
                if disk_bot == disk_ch:
                    continue

                # If the potential bottom disk appears in any other it is not
                if disk_bot in self.disks[disk_ch]["above"]:
                    break

            # If the loop completes then this disk is at the bottom
            else:
                return disk_bot
        else:
            raise Exception("No viable disk found to be at the bottom!")

    def calc_above_weights(self):
        """
        For each disk calculate the weights of the disks above it as a variable
        called `ab_weight`.
        """
        disks_to_do = [x for x in self.disks.keys()]

        # Create for every disk the sum of data above it
        while disks_to_do:
            rm_disks = []

            # For each disk check if the above weight can be calculated
            for dk_nm in disks_to_do:

                # Catch top level disks
                if not self.disks[dk_nm]["above"]:
                    self.disks[dk_nm]["ab_weight"] = 0
                    self.disks[dk_nm]["total_weight"] = self.disks[dk_nm]["weight"]
                    rm_disks.append(dk_nm)

                # Calculate midlevel disks with every disk above calculated
                else:
                    tmp_above_sum = 0

                    # Check that they all have been calculated
                    for above_dk_nm in self.disks[dk_nm]["above"]:
                        if above_dk_nm in disks_to_do:
                            break

                        # Keep a running total of the above weights
                        else:
                            tmp_above_sum += self.disks[above_dk_nm]["ab_weight"]
                            tmp_above_sum += self.disks[above_dk_nm]["weight"]

                    # If all have been calculated save the sum
                    else:
                        self.disks[dk_nm]["ab_weight"] = tmp_above_sum
                        self.disks[dk_nm]["total_weight"] = (
                            self.disks[dk_nm]["weight"] + tmp_above_sum
                        )
                        rm_disks.append(dk_nm)

            # After each run through remove the disks that have been calculated
            [disks_to_do.remove(x) for x in rm_disks]

    def rebalanced_weight(self) -> int:
        """
        Find the new value of the weight that needs to be changed to balance the
        ProgramTower.
        """
        self.calc_above_weights()
        curr_disks = [self.bottom_disk()]

        # Loop until a solution is found
        while True:
            next_disks = []

            # Check each current disk to find imbalances
            for c_disk in curr_disks:
                above_weights = [
                    self.disks[x]["total_weight"] for x in self.disks[c_disk]["above"]
                ]

                # All equal means no disk above it is a solution
                if len(set(above_weights)) == 1:
                    continue

                weight_cnts = collections.Counter(above_weights).most_common()

                # Count the instances of weights and find the unbalanced disk
                least_common_weight = weight_cnts[-1][0]
                unbalanced_disk = self.disks[c_disk]["above"][
                    above_weights.index(least_common_weight)
                ]
                unbal_abv_weights = [
                    self.disks[x]["total_weight"]
                    for x in self.disks[unbalanced_disk]["above"]
                ]

                # If the disks above the unbalanced one are the same it needs changing
                if len(set(unbal_abv_weights)) == 1:
                    return (
                        self.disks[unbalanced_disk]["weight"]
                        - least_common_weight
                        + weight_cnts[0][0]
                    )

                # Otherwise keep looking further up the stem
                else:
                    next_disks.append(unbalanced_disk)

            # Prepare for the next iteration of the loop
            if not next_disks:
                raise Exception("No viable next disks found")
            else:
                curr_disks = next_disks


if __name__ == "__main__":
    print(
        f"Part 1 = {ProgramTower('./data/input.txt').bottom_disk()}\n"
        f"Part 2 = {ProgramTower('./data/input.txt').rebalanced_weight()}\n"
    )
