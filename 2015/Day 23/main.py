"""
--- Day 23: Opening the Turing Lock ---

The computer supports two registers and six instructions. The registers are
named a and b, can hold any non-negative integer, and begin with a value of 0.
The instructions are as follows:

    hlf r sets register r to half its current value, then continues with the
    next instruction.

    tpl r sets register r to triple its current value, then continues with the
    next instruction.

    inc r increments register r, adding 1 to it, then continues with the next
    instruction.

    jmp offset is a jump; it continues with the instruction offset away
    relative to itself.

    jie r, offset is like jmp, but only jumps if register r is even ("jump if
    even").

    jio r, offset is like jmp, but only jumps if register r is 1 ("jump if
    one", not odd).

What is the value in register b when the program in your puzzle input is
finished executing?
"""

import re


class TuringLock:
    """Class to simulate the Turing Lock Computer."""

    def __init__(self, file_path, a=0, b=0):
        self.register = {
            "a": a,
            "b": b
        }

        # Pattern to detect the register instructions
        re_pat = r"(hlf|tpl|inc|jmp|jie|jio) (a|b|-?\+?[0-9]+)(, ){0," \
                 r"1}(-?\+?[0-9]+){0,1}"

        # Load the instructions from file
        data = open(file_path).read().splitlines()

        # Parse the instructions
        self.instructions = [re.findall(re_pat, x) for x in data]

    def run_instruct(self):
        """Run the instructions on the registers."""

        i = 0
        while i < len(self.instructions):

            inst_0 = self.instructions[i][0][0]
            inst_1 = self.instructions[i][0][1]
            inst_2 = self.instructions[i][0][3]

            match inst_0:

                case "hlf":
                    # Set the register to half its value
                    self.register[inst_1] //= 2

                case "tpl":
                    # Set the register to triple its current value
                    self.register[inst_1] *= 3

                case "inc":
                    # Increments the register by one
                    self.register[inst_1] += 1

                case "jmp":
                    # Move to a different instructions
                    i += int(inst_1)
                    continue

                case "jie":
                    # only jumps if register r is even
                    if self.register[inst_1] % 2 == 0:
                        i += int(inst_2)
                        continue

                case "jio":
                    # only jumps if register r is one
                    if self.register[inst_1] == 1:
                        i += int(inst_2)
                        continue

            i += 1


if __name__ == "__main__":

    samp_com = TuringLock("data/sample.txt")
    samp_com.run_instruct()
    print(samp_com.register["a"])

    # Part 1
    main_com = TuringLock("data/input.txt")
    main_com.run_instruct()
    print(main_com.register["b"])

    # Part 2
    main_com = TuringLock("data/input.txt", 1)
    main_com.run_instruct()
    print(main_com.register["b"])
