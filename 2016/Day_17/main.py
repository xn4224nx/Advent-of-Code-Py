"""
--- Day 17: Two Steps Forward ---

You're trying to access a secure vault protected by a 4x4 grid of small rooms
connected by doors. You start in the top-left room (marked S), and you can
access the vault (marked V) once you reach the bottom-right room:

    #########
    #S| | | #
    #-#-#-#-#
    # | | | #
    #-#-#-#-#
    # | | | #
    #-#-#-#-#
    # | | |
    ####### V

Fixed walls are marked with #, and doors are marked with - or |.

The doors in your current room are either open or closed (and locked) based on
the hexadecimal MD5 hash of a passcode (your puzzle input) followed by a
sequence of uppercase characters representing the path you have taken so far (U
for up, D for down, L for left, and R for right).

Only the first four characters of the hash are used; they represent,
respectively, the doors up, down, left, and right from your current position.
Any b, c, d, e, or f means that the corresponding door is open; any other
character (any number or a) means that the corresponding door is closed and
locked.

To access the vault, all you need to do is reach the bottom-right room;
reaching this room opens the vault and all doors in the maze.

For example, suppose the passcode is hijkl. Initially, you have taken no steps,
and so your path is empty: you simply find the MD5 hash of hijkl alone. The
first four characters of this hash are ced9, which indicate that up is open
(c), down is open (e), left is open (d), and right is closed and locked (9).
Because you start in the top-left corner, there are no "up" or "left" doors to
be open, so your only choice is down.

Next, having gone only one step (down, or D), you find the hash of hijklD. This
produces f2bc, which indicates that you can go back up, left (but that's a
wall), or right. Going right means hashing hijklDR to get 5745 - all doors
closed and locked. However, going up instead is worthwhile: even though it
returns you to the room you started in, your path would then be DU, opening a
different set of doors.

After going DU (and then hashing hijklDU to get 528e), only the right door is
open; after going DUR, all doors lock. (Fortunately, your actual passcode is
not hijkl).

PART 1: Given your vault's passcode, what is the shortest path (the actual
        path, not just the length) to reach the vault?
"""

import hashlib


class Route:
    def __init__(self, seed: str):
        self.seed = seed
        self.start = (0, 0)
        self.vault = (3, 3)
        self.limit = (3, 3)

    def hash_md5(self, msg: str) -> str:
        """
        Calculate the md5 hash of the message appended to the end of the
        internal salt value. Only return the first four characters of the
        hash.
        """
        return hashlib.md5((self.seed + msg).encode()).hexdigest()[:4]

    def detect_next_steps(self, previous_path: str) -> list[str]:
        """
        Determine the next possible moves that could be made in the current
        route.
        """
        valid_chars = ["b", "c", "d", "e", "f"]
        next_steps = []

        hash_guide = self.hash_md5(previous_path)

        if hash_guide[0] in valid_chars:
            next_steps.append("U")

        if hash_guide[1] in valid_chars:
            next_steps.append("D")

        if hash_guide[2] in valid_chars:
            next_steps.append("L")

        if hash_guide[3] in valid_chars:
            next_steps.append("R")

        return next_steps

    def path_2_coords(self, path: str) -> (int, int):
        """
        Determine the end coordinates of a specific path.
        """
        curr_pnt = (self.start[0], self.start[1])

        for move in path:
            if move == "U":
                curr_pnt = (curr_pnt[0], curr_pnt[1] - 1)
            elif move == "D":
                curr_pnt = (curr_pnt[0], curr_pnt[1] + 1)
            elif move == "L":
                curr_pnt = (curr_pnt[0] - 1, curr_pnt[1])
            elif move == "R":
                curr_pnt = (curr_pnt[0] + 1, curr_pnt[1])
            else:
                raise Exception(f"Unknown move '{move}'!")

        return curr_pnt

    def find_shortest_path(self) -> str:
        """
        Find and return the path that will get from the start point to the
        vault in the smallest number of steps.
        """
        viable_paths = {""}

        # Make steps in the maze until the end point is found
        while True:
            new_paths = set()

            # Create & validate new paths
            for path in viable_paths:

                # Work out the next possible steps
                for step in self.detect_next_steps(path):
                    n_path = path + step
                    pnt = self.path_2_coords(n_path)

                    # Check that the path is possible
                    if (
                        pnt[0] < 0
                        or pnt[1] < 0
                        or pnt[0] > self.limit[0]
                        or pnt[1] > self.limit[0]
                    ):
                        continue

                    # Check for a solution
                    if pnt == self.vault:
                        return n_path

                    # Otherwise save it for the next iteration
                    new_paths.add(n_path)

            # Prepare for the next iteration
            if not new_paths:
                raise Exception("No viable path found!")
            else:
                viable_paths = new_paths


if __name__ == "__main__":
    print(f"Part 1 = {Route('vkjiggvb').find_shortest_path()}")
