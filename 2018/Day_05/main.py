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

Time to improve the polymer.

One of the unit types is causing problems; it's preventing the polymer from
collapsing as much as it should. Your goal is to figure out which unit type is
causing the most problems, remove all instances of it (regardless of
polarity), fully react the remaining polymer, and measure its length.

For example, again using the polymer dabAcCaCBAcCcaDA from above:

        -   Removing all A/a units produces dbcCCBcCcD. Fully reacting this
            polymer produces dbCBcD, which has length 6.

        -   Removing all B/b units produces daAcCaCAcCcaDA. Fully reacting
            this polymer produces daCAcaDA, which has length 8.

        -   Removing all C/c units produces dabAaBAaDA. Fully reacting this
            polymer produces daDA, which has length 4.

        -   Removing all D/d units produces abAcCaCBAcCcaA. Fully reacting
            this polymer produces abCBAc, which has length 6.

In this example, removing all C/c units was best, producing the answer 4.

PART 2: What is the length of the shortest polymer you can produce by
        removing all units of exactly one type and fully reacting the result?
"""

from string import ascii_lowercase, ascii_uppercase


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

    def len_after_rm(self) -> int:
        """
        Test the removal of each letter type and find the one that gives the
        shortest length. Then return the smallest length.
        """
        orig_poly = self.units[:]
        min_poly_size = len(orig_poly)

        for l_idx in range(len(ascii_lowercase)):
            self.units = orig_poly[:]
            self.units = self.units.replace(ascii_lowercase[l_idx], "")
            self.units = self.units.replace(ascii_uppercase[l_idx], "")
            l_min = self.final_len()

            if l_min < min_poly_size:
                min_poly_size = l_min

        return min_poly_size


if __name__ == "__main__":
    with open("./data/input_0.txt", "r") as fp:
        long_poly = fp.read().strip()

    print(
        f"Part 1 = {Polymer(long_poly).final_len()}\n"
        f"Part 2 = {Polymer(long_poly).len_after_rm()}\n"
    )
