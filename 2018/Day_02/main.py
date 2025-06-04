"""
--- Day 2: Inventory Management System ---

You stop falling through time, catch your breath, and check the screen on the
device. "Destination reached. Current Year: 1518. Current Location: North Pole
Utility Closet 83N10." You made it! Now, to find those anomalies.

Outside the utility closet, you hear footsteps and a voice. "...I'm not sure
either. But now that so many people have chimneys, maybe he could sneak in that
way?" Another voice responds, "Actually, we've been working on a new kind of
suit that would let him fit through tight spaces like that. But, I heard that a
few days ago, they lost the prototype fabric, the design plans, everything!
Nobody on the team can even seem to remember important details of the project!"

"Wouldn't they have had enough fabric to fill several boxes in the warehouse?
They'd be stored together, so the box IDs should be similar. Too bad it would
take forever to search the warehouse for two similar box IDs..." They walk too
far away to hear any more.

Late at night, you sneak to the warehouse - who knows what kinds of paradoxes
you could cause if you were discovered - and use your fancy wrist device to
quickly scan every box and produce a list of the likely candidates (your puzzle
input).

To make sure you didn't miss any, you scan the likely candidate boxes again,
counting the number that have an ID containing exactly two of any letter and
then separately counting those with exactly three of any letter. You can
multiply those two counts together to get a rudimentary checksum and compare it
to what your device predicts.

For example, if you see the following box IDs:

        -   abcdef contains no letters that appear exactly two or three times.
        -   bababc contains two a and three b, so it counts for both.
        -   abbcde contains two b, but no letter appears exactly three times.
        -   abcccd contains three c, but no letter appears exactly two times.
        -   aabcdd contains two a and two d, but it only counts once.
        -   abcdee contains two e.
        -   ababab contains three a and three b, but it only counts once.

Of these box IDs, four of them contain a letter which appears exactly twice,
and three of them contain a letter which appears exactly three times.
Multiplying these together produces a checksum of 4 * 3 = 12.

PART 1: What is the checksum for your list of box IDs?
"""


class Warehouse:
    def __init__(self, box_ids_file: str):
        self.boxes = [x.strip() for x in open(box_ids_file, "r").readlines()]

    def box_check(self, box: str) -> (bool, bool):
        """
        Does the box contain exactly 2 number of the same letter and does it
        contain exactly 3 for the same letter.
        """
        letter_cnts = {}

        # Count the occurance of each character
        for char in box:
            if char in letter_cnts:
                letter_cnts[char] += 1
            else:
                letter_cnts[char] = 1

        # Determine if there are any letters that occur twice or three times
        counts = [x for x in letter_cnts.values()]
        return 2 in counts, 3 in counts

    def checksum(self) -> int:
        """
        Count the number of boxes with 2 and 3 of the same letter. Multiply the
        numbers together to calculate the checksum.
        """
        check_2, check_3 = 0, 0

        # Count the total number of boxes that pass both checks
        for box in self.boxes:
            cnt_2, cnt_3 = self.box_check(box)
            check_2 += cnt_2
            check_3 += cnt_3

        # Return the product of both checks
        return check_2 * check_3


if __name__ == "__main__":
    pass
