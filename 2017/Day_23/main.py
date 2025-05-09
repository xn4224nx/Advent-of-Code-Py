"""
--- Day 23: Coprocessor Conflagration ---

You decide to head directly to the CPU and fix the printer from there. As you
get close, you find an experimental coprocessor doing so much work that the
local programs are afraid it will halt and catch fire. This would cause serious
issues for the rest of the computer, so you head in and see what you can do.

The code it's running seems to be a variant of the kind you saw recently on
that tablet. The general functionality seems very similar, but some of the
instructions are different:

        -   set X Y sets register X to the value of Y.

        -   sub X Y decreases register X by the value of Y.

        -   mul X Y sets register X to the result of multiplying the value
            contained in register X by the value of Y.

        -   jnz X Y jumps with an offset of the value of Y, but only if the
            value of X is not zero. (An offset of 2 skips the next instruction,
            an offset of -1 jumps to the previous instruction, and so on.)

Only the instructions listed above are used. The eight registers here, named a
through h, all start at 0.

The coprocessor is currently set to some kind of debug mode, which allows for
testing, but prevents it from doing any meaningful work.

PART 1: If you run the program (your puzzle input), how many times is the mul
        instruction invoked?

Now, it's time to fix the problem.

The debug mode switch is wired directly to register a. You flip the switch,
which makes register a now start at 1 when the program is executed.

Immediately, the coprocessor begins to overheat. Whoever wrote this program
obviously didn't choose a very efficient implementation. You'll need to optimize
the program if it has any hope of completing before Santa needs that printer
working.

The coprocessor's ultimate goal is to determine the final value left in register
h once the program completes. Technically, if it had that... it wouldn't even
need to run the program.

PART 2: After setting register a to 1, if the program were to run to completion,
        what value would be left in register h?
"""

from sympy.ntheory import isprime


class CPU:
    def __init__(self, command_file: str):
        self.cmd_idx = 0
        self.register = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0,
        }
        self.cmds = []

        # Read the commands and parse the numbers
        with open(command_file, "r") as fp:
            for line in fp.readlines():
                self.cmds.append(
                    [
                        int(x) if x[1:].isdigit() or x.isdigit() else x
                        for x in line.split()
                    ]
                )

    def lookup_val(self, val: int | str) -> int:
        """
        Lookup a value in the register and return its value or just return the
        original value.
        """
        if isinstance(val, int):
            return val
        else:
            return self.register[val]

    def exe_command(self, com_idx: int):
        """
        Modify the CPU with the supplied command.
        """
        com_name = self.cmds[com_idx][0]

        if com_name == "set":
            self.register[self.cmds[com_idx][1]] = self.lookup_val(
                self.cmds[com_idx][2]
            )

        elif com_name == "sub":
            self.register[self.cmds[com_idx][1]] -= self.lookup_val(
                self.cmds[com_idx][2]
            )

        elif com_name == "mul":
            self.register[self.cmds[com_idx][1]] *= self.lookup_val(
                self.cmds[com_idx][2]
            )

        elif com_name == "jnz":
            if self.lookup_val(self.cmds[com_idx][1]) != 0:
                self.cmd_idx += self.lookup_val(self.cmds[com_idx][2]) - 1

        else:
            raise Exception(f"Unrecognised command {com_name}")

        self.cmd_idx += 1

    def command_count(self, com_name: str) -> int:
        """
        Execute all the commands in order until the command index points to
        a command that doesn't exist. While doing this count the number of
        times the specified command is executed.
        """
        cmd_counts = {self.cmds[x][0]: 0 for x in range(len(self.cmds))}
        assert com_name in cmd_counts

        while self.cmd_idx >= 0 and self.cmd_idx < len(self.cmds):

            # Record the command about to be executed
            cmd_counts[self.cmds[self.cmd_idx][0]] += 1

            # Execute current command
            self.exe_command(self.cmd_idx)

        return cmd_counts[com_name]

    def final_reg_val(self, reg_name: str) -> int:
        """
        Find the final value that a register has after executing all commands.
        """
        assert reg_name in self.register

        while self.cmd_idx >= 0 and self.cmd_idx < len(self.cmds):
            self.exe_command(self.cmd_idx)

        return self.register[reg_name]

    def part_02_fast(self) -> int:
        """
        Optimised version of part 2. Find the number of non-primes between
        two specified values.
        """
        counter = 0
        first_val = self.cmds[0][2] * self.cmds[4][2] - self.cmds[5][2]
        last_val = first_val - self.cmds[7][2]

        for val in range(first_val, last_val + 1, -self.cmds[-2][2]):
            if not isprime(val):
                counter += 1

        return counter


if __name__ == "__main__":
    print(
        f"Part 1 = {CPU("./data/input.txt").command_count('mul')}\n"
        f"Part 2 = {CPU("./data/input.txt").part_02_fast()}\n"
    )
