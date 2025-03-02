"""
--- Day 8: I Heard You Like Registers ---

You receive a signal directly from the CPU. Because of your recent assistance
with jump instructions, it would like you to compute the result of a series of
unusual register instructions.

Each instruction consists of several parts: the register to modify, whether to
increase or decrease that register's value, the amount by which to increase or
decrease it, and a condition. If the condition fails, skip the instruction
without modifying the register. The registers all start at 0. The instructions
look like this:

    b inc 5 if a > 1
    a inc 1 if b < 5
    c dec -10 if a >= 1
    c inc -20 if c == 10

These instructions would be processed as follows:

    -   Because a starts at 0, it is not greater than 1, and so b is not
        modified.

    -   a is increased by 1 (to 1) because b is less than 5 (it is 0).

    -   c is decreased by -10 (to 10) because a is now greater than or equal to
        1 (it is 1).

    -   c is increased by -20 (to -10) because c is equal to 10.

After this process, the largest value in any register is 1.

You might also encounter <= (less than or equal to) or != (not equal to).
However, the CPU doesn't have the bandwidth to tell you what all the registers
are named, and leaves that to you to determine.

PART 1: What is the largest value in any register after completing the
        instructions in your puzzle input?

PART 2: To be safe, the CPU also needs to know the highest value held in any
        register during this process so that it can decide how much memory to
        allocate to these operations. For example, in the above instructions,
        the highest value ever held was 10 (in register c after the third
        instruction was evaluated).
"""

import re


class CPU:
    def __init__(self, datafile: str):
        instruc_re = re.compile(
            r"([a-z]+) (inc|dec) (\-?[0-9]+) if ([a-z]+) (>=|<=|==|<|>|!=) (\-?[0-9]+)"
        )
        self.register = {}
        self.cmds = []

        with open(datafile, "r") as fp:
            for line in fp.readlines():

                # Check this line for a match
                result = instruc_re.match(line)

                if result is None:
                    raise Exception(f"Line not parsed: '{line}'")

                # Save the named registers
                self.register[result.group(1)] = 0
                self.register[result.group(4)] = 0

                # Determine the register change
                if result.group(2) == "inc":
                    change = int(result.group(3))
                else:
                    change = -1 * int(result.group(3))

                # Save the command
                self.cmds.append(
                    [
                        result.group(1),
                        change,
                        result.group(4),
                        result.group(5),
                        int(result.group(6)),
                    ]
                )

    def execute_command(self, cmd_idx: int):
        """
        Execute an instruction specified by the index, only modify the register
        if the condition is met.
        """
        if eval(
            f"{self.register[self.cmds[cmd_idx][2]]} "
            f"{self.cmds[cmd_idx][3]} "
            f"{self.cmds[cmd_idx][4]}"
        ):
            self.register[self.cmds[cmd_idx][0]] += self.cmds[cmd_idx][1]

    def final_largest_value(self) -> int:
        """
        Execute all instructions and find the largest value in the register.
        Return the final max value and the overall max value through out the
        process.
        """
        overall_max = 0

        for cmd_idx in range(len(self.cmds)):
            self.execute_command(cmd_idx)
            curr_max = max(self.register.values())

            # Check for a new highest maximum
            if curr_max > overall_max:
                overall_max = curr_max

        return (overall_max, curr_max)


if __name__ == "__main__":
    overall_max, curr_max = CPU("./data/input.txt").final_largest_value()
    print(f"Part 1 = {curr_max}\nPart 2 = {overall_max}")
