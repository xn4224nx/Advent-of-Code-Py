"""
--- Day 13: Packet Scanners ---

By studying the firewall briefly, you are able to record (in your puzzle input)
the depth of each layer and the range of the scanning area for the scanner
within it, written as depth: range. Each layer has a thickness of exactly 1. A
layer at depth 0 begins immediately inside the firewall; a layer at depth 1
would start immediately after that.

For example, suppose you've recorded the following:

0: 3
1: 2
4: 4
6: 4

This means that there is a layer immediately inside the firewall (with range
3), a second layer immediately after that (with range 2), a third layer which
begins at depth 4 (with range 4), and a fourth layer which begins at depth 6
(also with range 4). Visually, it might look like this:

 0   1   2   3   4   5   6
[ ] [ ] ... ... [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[ ]             [ ]     [ ]
                [ ]     [ ]
Within each layer, a security scanner moves back and forth within its range.
Each security scanner starts at the top and moves down until it reaches the
bottom, then moves up until it reaches the top, and repeats. A security
scanner takes one picosecond to move one step. Drawing scanners as S, the
first few picoseconds look like this:

Picosecond 0:
 0   1   2   3   4   5   6
[S] [S] ... ... [S] ... [S]
[ ] [ ]         [ ]     [ ]
[ ]             [ ]     [ ]
                [ ]     [ ]

Picosecond 1:
 0   1   2   3   4   5   6
[ ] [ ] ... ... [ ] ... [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]

Picosecond 2:
 0   1   2   3   4   5   6
[ ] [S] ... ... [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[S]             [S]     [S]
                [ ]     [ ]

Picosecond 3:
 0   1   2   3   4   5   6
[ ] [ ] ... ... [ ] ... [ ]
[S] [S]         [ ]     [ ]
[ ]             [ ]     [ ]
                [S]     [S]

Your plan is to hitch a ride on a packet about to move through the firewall.
The packet will travel along the top of each layer, and it moves at one layer
per picosecond. Each picosecond, the packet moves one layer forward (its first
move takes it into layer 0), and then the scanners move one step. If there is
a scanner at the top of the layer as your packet enters it, you are caught.
(If a scanner moves into the top of its layer while you are there, you are not
caught: it doesn't have time to notice you before you leave.) If you were to
do this in the configuration above, marking your current position with
parentheses, your passage through the firewall would look like this:

Initial state:
 0   1   2   3   4   5   6
[S] [S] ... ... [S] ... [S]
[ ] [ ]         [ ]     [ ]
[ ]             [ ]     [ ]
                [ ]     [ ]

Picosecond 0:
 0   1   2   3   4   5   6
(S) [S] ... ... [S] ... [S]
[ ] [ ]         [ ]     [ ]
[ ]             [ ]     [ ]
                [ ]     [ ]

 0   1   2   3   4   5   6
( ) [ ] ... ... [ ] ... [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]


Picosecond 1:
 0   1   2   3   4   5   6
[ ] ( ) ... ... [ ] ... [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] (S) ... ... [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[S]             [S]     [S]
                [ ]     [ ]


Picosecond 2:
 0   1   2   3   4   5   6
[ ] [S] (.) ... [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[S]             [S]     [S]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] [ ] (.) ... [ ] ... [ ]
[S] [S]         [ ]     [ ]
[ ]             [ ]     [ ]
                [S]     [S]


Picosecond 3:
 0   1   2   3   4   5   6
[ ] [ ] ... (.) [ ] ... [ ]
[S] [S]         [ ]     [ ]
[ ]             [ ]     [ ]
                [S]     [S]

 0   1   2   3   4   5   6
[S] [S] ... (.) [ ] ... [ ]
[ ] [ ]         [ ]     [ ]
[ ]             [S]     [S]
                [ ]     [ ]


Picosecond 4:
 0   1   2   3   4   5   6
[S] [S] ... ... ( ) ... [ ]
[ ] [ ]         [ ]     [ ]
[ ]             [S]     [S]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] [ ] ... ... ( ) ... [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]


Picosecond 5:
 0   1   2   3   4   5   6
[ ] [ ] ... ... [ ] (.) [ ]
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] [S] ... ... [S] (.) [S]
[ ] [ ]         [ ]     [ ]
[S]             [ ]     [ ]
                [ ]     [ ]


Picosecond 6:
 0   1   2   3   4   5   6
[ ] [S] ... ... [S] ... (S)
[ ] [ ]         [ ]     [ ]
[S]             [ ]     [ ]
                [ ]     [ ]

 0   1   2   3   4   5   6
[ ] [ ] ... ... [ ] ... ( )
[S] [S]         [S]     [S]
[ ]             [ ]     [ ]
                [ ]     [ ]

In this situation, you are caught in layers 0 and 6, because your packet
entered the layer when its scanner was at the top when you entered it. You
are not caught in layer 1, since the scanner moved into the top of the layer
once you were already there.

The severity of getting caught on a layer is equal to its depth multiplied by
its range. (Ignore layers in which you do not get caught.) The severity of
the whole trip is the sum of these values. In the example above, the trip
severity is 0*3 + 6*4 = 24.

PART 1: Given the details of the firewall you've recorded, if you leave
        immediately, what is the severity of your whole trip?
"""


class Firewall:
    def __init__(self, conf_file: str):
        self.sc_info = []  # Scanner Infomation
        self.sc_level = []  # Current Scanner Level
        self.sc_desc = []  # Current Scanner Directions
        self.packet_loc = 0  # Packet location

        with open(conf_file, "r") as fp:
            for line in fp.readlines():
                val_0, val_1 = line.split(": ")
                self.sc_info.append((int(val_0), int(val_1)))
                self.sc_level.append(0)
                self.sc_desc.append(True)

    def increment_scanners(self):
        """
        Move the scanners one step.
        """
        for sc_idx in range(len(self.sc_level)):
            # Move the scanner up or down
            if self.sc_desc[sc_idx]:
                self.sc_level[sc_idx] += 1
            else:
                self.sc_level[sc_idx] -= 1

            # Reverse the movement direction
            if self.sc_level[sc_idx] == 0:
                self.sc_desc[sc_idx] = True

            elif self.sc_level[sc_idx] == self.sc_info[sc_idx][1] - 1:
                self.sc_desc[sc_idx] = False

    def trip_severity(self) -> int:
        """
        With the firewall in its current state calculate the total severity
        of the trip.
        """
        total_severity = 0

        # Move the packet until it reaches the end
        while self.packet_loc <= self.sc_info[-1][0]:

            # Check for packet detection
            for sc_idx in range(len(self.sc_info)):

                # Check to see if the packet is in this scanners column and
                # that the scanner is at the top of the column.
                if (
                    self.sc_info[sc_idx][0] == self.packet_loc
                    and self.sc_level[sc_idx] == 0
                ):
                    total_severity += self.sc_info[sc_idx][0] * self.sc_info[sc_idx][1]

            # Move the scanners
            self.increment_scanners()

            # Move the packet along
            self.packet_loc += 1

        return total_severity

    def traverse(self, start_time: int) -> int:
        """
        Move across the filewall at the specified start time and return
        the total severity of the traversal.
        """
        self.sc_level = [0 for _ in range(len(self.sc_info))]
        self.sc_desc = [True for _ in range(len(self.sc_info))]
        self.packet_loc = 0

        for _ in range(start_time):
            self.increment_scanners()

        return self.trip_severity()


if __name__ == "__main__":
    print(f"Part 1 = {Firewall("./data/input.txt").trip_severity()}")
