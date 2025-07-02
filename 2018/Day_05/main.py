"""
--- Day 5: Alchemical Reduction ---

You've managed to sneak in to the prototype suit manufacturing lab. The Elves
are making decent progress, but are still struggling with the suit's size
reduction capabilities.

While the very latest in 1518 alchemical technology might have solved their
problem eventually, you can do better. You scan the chemical composition of
the suit's material and discover that it is formed by extremely long polymers
(one of which is available as your puzzle input).

The polymer is formed by smaller units which, when triggered, react with each
other such that two adjacent units of the same type and opposite polarity are
destroyed. Units' types are represented by letters; units' polarity is
represented by capitalization. For instance, r and R are units with the same
type but opposite polarity, whereas r and s are entirely different types and
do not react.

For example:

    -   In aA, a and A react, leaving nothing behind.

    -   In abBA, bB destroys itself, leaving aA. As above, this then destroys
        itself, leaving nothing.

    -   In abAB, no two adjacent units are of the same type, and so nothing
        happens.

    -   In aabAAB, even though aa and AA are of the same type, their
        polarities match, and so nothing happens.

Now, consider a larger example, dabAcCaCBAcCcaDA:

    dabAcCaCBAcCcaDA    The first 'cC' is removed.

    dabAaCBAcCcaDA      This creates 'Aa', which is removed.

    dabCBAcCcaDA        Either 'cC' or 'Cc' are removed (the result is the
                        same).

    dabCBAcaDA          No further actions can be taken.

After all possible reactions, the resulting polymer contains 10 units.

PART 1: How many units remain after fully reacting the polymer you scanned?
"""


class Polymer:
    def __init__(self, s_units: str):
        self.units = s_units

    def collapse(self):
        """
        Iterate over the polymer and if an upper and lower letter of the same
        type are next to each other remove them.
        """
        rm_indexs = []

        # Find the indexs of pairs to remove
        idx = 0
        while idx < len(self.units) - 1:
            if abs(ord(self.units[idx]) - ord(self.units[idx + 1])) == 32:
                rm_indexs.append(idx)
                idx += 2
            else:
                idx += 1

        # Prune the polymer
        for idx in reversed(rm_indexs):
            self.units = self.units[:idx] + self.units[idx + 2 :]

    def final_len(self) -> int:
        """
        After collapsing the polymer as much as possible find its final length.
        """
        while True:
            old_len = len(self.units)
            self.collapse()

            if old_len == len(self.units):
                return old_len


if __name__ == "__main__":
    with open("./data/input_0.txt", "r") as fp:
        long_poly = fp.read().strip()

    print(f"Part 1 = {Polymer(long_poly).final_len() }")
