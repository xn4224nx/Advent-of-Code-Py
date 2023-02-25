"""
--- Day 16: Permutation Promenade ---

There are sixteen programs in total, named a through p. They start by standing
in a line: a stands in position 0, b stands in position 1, and so on until p,
which stands in position 15.

    Spin, written sX, makes X programs move from the end to the front, but
    maintain their order otherwise. (For example, s3 on abcde produces cdeab).

    Exchange, written xA/B, makes the programs at positions A and B swap places.

    Partner, written pA/B, makes the programs named A and B swap places.

Part 1
In what order are the programs standing after their dance?
"""

import re

class Promenade:

    def __init__(self, num_progs: int):

        self.order = {chr(x + ord('a')): x for x in range(num_progs)}
        self.instructions = []

    def __str__(self):

        return_value = ""

        for w in sorted(self.order, key=self.order.get, reverse=False):
            return_value += w

        return return_value

    def load_instructions(self, file_path):
        self.instructions = open(file_path, "r").read().split(",")

    def spin(self, offset: int):
        """
        Makes the programs move from the end to the front by offset steps,
        but maintain their order otherwise.
        """
        for program in self.order:
            self.order[program] = (self.order[program] + offset) \
                                   % len(self.order)

    def exchange(self, idx1: int, idx2: int):
        """Makes the programs at positions idx1 and idx2 swap places."""

        names = list(self.order.keys())
        positions = list(self.order.values())

        prog1 = names[positions.index(idx1)]
        prog2 = names[positions.index(idx2)]

        self.partner(prog1, prog2)

    def partner(self, prog1: str, prog2: str):
        self.order.update({prog1: self.order[prog2], prog2: self.order[prog1]})

    def execute_instruction(self, instruction: str):

        if instruction.startswith("s"):
            self.spin(int(instruction[1:]))

        elif instruction.startswith("x"):
            progs = instruction[1:].split("/")
            self.exchange(int(progs[0]), int(progs[1]))

        elif instruction.startswith("p"):
            progs = instruction[1:].split("/")
            self.partner(progs[0], progs[1])

        else:
            raise Exception(f"{instruction} is not a recognised instruction.")

    def execute_all_instructions(self):

        for instruction in self.instructions:
            self.execute_instruction(instruction)


# Part 1
part1 = Promenade(16)
part1.load_instructions("data/input.txt")
part1.execute_all_instructions()
print(part1)


# Part 2
part2 = Promenade(16)
part2.load_instructions("data/input.txt")

# Determine how long the pattern takes to repeat
dance_iterations = []
for i in range(100):

    part2.execute_all_instructions()

    if str(part2) in dance_iterations:
        repeat_len = i
        break
    else:
        dance_iterations.append(str(part2))

# Work out the value at one billion
part2 = Promenade(16)
part2.load_instructions("data/input.txt")

for _ in range(1000000000 % repeat_len):
    part2.execute_all_instructions()

print(part2)