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


class Route:
    def __init__(self, seed: str):
        self.seed = seed

    def hash_md5(self, msg: str) -> str:
        """
        Calculate the md5 hash of the message appended to the end of the
        internal salt value. Only return the first four characters of the
        hash.
        """
        pass

    def detect_next_steps(self, previous_path: str) -> list[str]:
        """
        Determine the next possible moves that could be made in the current
        route.
        """
        pass

    def find_shortest_path(self) -> str:
        """
        Find and return the path that will get from the start point to the
        vault in the smallest number of steps.
        """
        pass


if __name__ == "__main__":
    pass
