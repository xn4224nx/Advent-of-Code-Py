"""
--- Day 12: Leonardo's Monorail ---

You finally reach the top floor of this building: a garden with a slanted glass
ceiling. Looks like there are no more stars to be had.

While sitting on a nearby bench amidst some tiger lilies, you manage to decrypt
some of the files you extracted from the servers downstairs.

According to these documents, Easter Bunny HQ isn't just this building - it's a
collection of buildings in the nearby area. They're all connected by a local
monorail, and there's another building not far from here! Unfortunately, being
night, the monorail is currently not operating.

You remotely connect to the monorail control systems and discover that the boot
sequence expects a password. The password-checking logic (your puzzle input) is
easy to extract, but the code it uses is strange: it's assembunny code designed
for the new computer you just assembled. You'll have to execute the code and
get the password.

The assembunny code you've extracted operates on four registers (a, b, c, and
d) that start at 0 and can hold any integer. However, it seems to make use of
only a few instructions:

    -   cpy x y copies x (either an integer or the value of a register) into
        register y.

    -   inc x increases the value of register x by one.

    -   dec x decreases the value of register x by one.

    -   jnz x y jumps to an instruction y away (positive means forward;
        negative means backward), but only if x is not zero.

The jnz instruction moves relative to itself: an offset of -1 would continue at
the previous instruction, while an offset of 2 would skip over the next
instruction.

PART 1: After executing the assembunny code in your puzzle input, what value is
        left in register a?
"""

import re


class Computer:
    def __init__(self, datafile: str):
        self.register = {"a": 0, "b": 0, "c": 0, "d": 0}
        self.curr_instruc = 0
        self.datafile = datafile

        with open(datafile, "r") as fp:
            self.instruc = fp.read().splitlines()

    def copy(self, value: str, dest: str):
        """
        Set a value of a register to an integer or the value of another
        register.
        """
        try:
            self.register[dest] = int(value)
        except:
            self.register[dest] = self.register[value]

    def incr(self, dest: str):
        """
        Increase a register by one.
        """
        self.register[dest] += 1

    def decr(self, dest: str):
        """
        Decrease a register by one.
        """
        self.register[dest] -= 1

    def zero_jump(self, dest: str, move: str):
        """
        Move to a different instruction if the specified register is not equal
        to zero.
        """
        if self.register[dest] != 0:
            self.curr_instruc += move

    def execute_command(self, raw_cmd: str):
        """
        Parse a raw string command and execute a command.
        """

        # Detect copy command
        cp_match = re.search(r"cpy (-?\d+|a|b|c|d) (a|b|c|d)", raw_cmd)
        if cp_match is not None:
            self.copy(cp_match.group(1), cp_match.group(2))
            return

        # Detect increment command
        inc_match = re.search(r"inc (a|b|c|d)", raw_cmd)
        if inc_match is not None:
            self.incr(inc_match.group(1))
            return

        # Detect decrease command
        dec_match = re.search(r"dec (a|b|c|d)", raw_cmd)
        if dec_match is not None:
            self.decr(dec_match.group(1))
            return

        # Detect a jump command
        jmp_match = re.search(r"jnz (a|b|c|d) (-?\d+)", raw_cmd)
        if jmp_match is not None:
            self.zero_jump(jmp_match.group(1), int(jmp_match.group(2)))
            return

        raise Exception('Command "{raw_cmd}" not recognised!!')

    def exe_all_commands(self):
        """
        Iterate over all the commands from the datafile.
        """
        while self.curr_instruc < len(self.instruc):
            self.execute_command(self.instruc[self.curr_instruc])
            self.curr_instruc += 1


if __name__ == "__main__":
    pass
