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


class Computer:
    def __init__(self, datafile: str):
        pass

    def copy(self, value: str | int, dest: str):
        pass

    def incr(self, dest: str):
        pass

    def decr(self, dest: str):
        pass

    def zero_jump(self, dest: str, move: str):
        pass

    def execute_command(self, raw_cmd: str):
        pass

    def exe_all_commands(self):
        pass


if __name__ == "__main__":
    pass
