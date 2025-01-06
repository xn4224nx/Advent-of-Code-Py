"""
--- Day 21: Scrambled Letters and Hash ---

The computer system you're breaking into uses a weird scrambling function to
store its passwords. It shouldn't be much trouble to create your own scrambled
password so you can add it to the system; you just have to implement the
scrambler.

The scrambling function is a series of operations (the exact list is provided in
your puzzle input). Starting with the password to be scrambled, apply each
operation in succession to the string. The individual operations behave as
follows:

    -   swap position X with position Y means that the letters at indexes X and
        Y (counting from 0) should be swapped.

    -   swap letter X with letter Y means that the letters X and Y should be
        swapped (regardless of where they appear in the string).

    -   rotate left/right X steps means that the whole string should be rotated;
        for example, one right rotation would turn abcd into dabc.

    -   rotate based on position of letter X means that the whole string should
        be rotated to the right based on the index of letter X (counting from 0)
        as determined before this instruction does any rotations. Once the index
        is determined, rotate the string to the right one time, plus a number of
        times equal to that index, plus one additional time if the index was at
        least 4.

    -   reverse positions X through Y means that the span of letters at indexes
        X through Y (including the letters at X and Y) should be reversed in
        order.

    -   move position X to position Y means that the letter which is at index X
        should be removed from the string, then inserted such that it ends up at
        index Y.

PART 1: Now, you just need to generate a new scrambled password and you can
        access the system. Given the list of scrambling operations in your
        puzzle input, what is the result of scrambling abcdefgh?
"""

from collections import deque
import re


class Scambler:
    def __init__(self, data_file: str, seed: str):
        self.seed = deque(seed)

        with open(data_file) as fp:
            self.instructs = fp.read().splitlines()

    def swap_by_letters(self, char0: str, char1: str):
        """
        Swap the two mentioned characters in the seed.
        """
        idx0 = self.seed.index(char0)
        idx1 = self.seed.index(char1)
        self.seed[idx0], self.seed[idx1] = self.seed[idx1], self.seed[idx0]

    def swap_by_index(self, idx0: int, idx1: int):
        """
        Swap the two mentioned characters in the seed by their index.
        """
        self.seed[idx0], self.seed[idx1] = self.seed[idx1], self.seed[idx0]

    def rotate_left(self, steps: int):
        """
        Rotate the seed left.
        """
        self.seed.rotate(-1 * steps)

    def rotate_right(self, steps: int):
        """
        Rotate the seed right.
        """
        self.seed.rotate(steps)

    def rotate_by_letter_pos(self, char: str):
        """
        The whole string should be rotated to the right based on the index of
        letter char (counting from 0) as determined before this instruction does
        any rotations. Once the index is determined, rotate the string to the
        right one time, plus a number of times equal to that index, plus one
        additional time if the index was at least 4.
        """
        char_idx = self.seed.index(char)

        if char_idx >= 4:
            char_idx += 1

        self.seed.rotate(char_idx + 1)

    def reverse_positions(self, idx0: int, idx1: int):
        """
        The span of letters at indexes idx0 through idx1 (including the letters
        at idx0 and idx1) should be reversed in order.
        """
        tmp = list(self.seed)
        extract = tmp[idx0 : idx1 + 1]
        self.seed = deque(tmp[:idx0] + extract[::-1] + tmp[idx1 + 1 :])

    def move_positions(self, idx0: int, idx1: int):
        """
        The letter which is at index idx0 should be removed from the string,
        then inserted such that it ends up at index idx1.
        """
        val = self.seed[idx0]
        del self.seed[idx0]
        self.seed.insert(idx1, val)

    def execute_insruct(self, command: str):
        """
        Execute a method based on a supplied string command.
        """
        matches = re.search(r"swap position (\d+) with position (\d+)", command)
        if matches is not None:
            self.swap_by_index(int(matches.group(1)), int(matches.group(2)))
            return

        matches = re.search(r"swap letter ([a-z]) with letter ([a-z])", command)
        if matches is not None:
            self.swap_by_letters(matches.group(1), matches.group(2))
            return

        matches = re.search(r"rotate (left|right) (\d+) steps?", command)
        if matches is not None:
            if matches.group(1) == "left":

                self.rotate_left(int(matches.group(2)))
            else:
                self.rotate_right(int(matches.group(2)))
            return

        matches = re.search(r"rotate based on position of letter ([a-z])", command)
        if matches is not None:
            self.rotate_by_letter_pos(matches.group(1))
            return

        matches = re.search(r"reverse positions (\d+) through (\d+)", command)
        if matches is not None:
            self.reverse_positions(int(matches.group(1)), int(matches.group(2)))
            return

        matches = re.search(r"move position (\d+) to position (\d+)", command)
        if matches is not None:
            self.move_positions(int(matches.group(1)), int(matches.group(2)))
            return

    def execute_all_commands(self) -> str:
        """
        Run through all the commands and return the final value of the seed.
        """
        for comm in self.instructs:
            self.execute_insruct(comm)

        return "".join(self.seed)


if __name__ == "__main__":
    print(f"Part 1 = {Scambler('./data/input.txt', 'abcdefgh').execute_all_commands()}")
