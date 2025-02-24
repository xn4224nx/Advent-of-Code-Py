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
"""

import re


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


if __name__ == "__main__":
    print(
        f"Part 1 = {ProgramTower('./data/input.txt').bottom_disk()}",
    )
