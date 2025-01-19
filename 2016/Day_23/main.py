"""
--- Day 23: Safe Cracking ---

This is one of the top floors of the nicest tower in EBHQ. The Easter Bunny's
private office is here, complete with a safe hidden behind a painting, and who
wouldn't hide a star in a safe behind a painting?

The safe has a digital screen and keypad for code entry. A sticky note attached
to the safe has a password hint on it: "eggs". The painting is of a large
rabbit coloring some eggs. You see 7.

When you go to type the code, though, nothing appears on the display; instead,
the keypad comes apart in your hands, apparently having been smashed. Behind it
is some kind of socket - one that matches a connector in your prototype
computer! You pull apart the smashed keypad and extract the logic circuit, plug
it into your computer, and plug your computer into the safe.

Now, you just need to figure out what output the keypad would have sent to the
safe. You extract the assembunny code from the logic chip (your puzzle input).

The code looks like it uses almost the same architecture and instruction set
that the monorail computer used! You should be able to use the same assembunny
interpreter for this as you did there, but with one new instruction:

    -   For one-argument instructions, inc becomes dec, and all other one-
        argument instructions become inc.

    -   For two-argument instructions, jnz becomes cpy, and all other two-
        instructions become jnz.

    -   The arguments of a toggled instruction are not affected.

    -   If an attempt is made to toggle an instruction outside the program,
        nothing happens.

    -   If toggling produces an invalid instruction (like cpy 1 2) and an
        attempt is later made to execute that instruction, skip it instead.

    -   If tgl toggles itself (for example, if a is 0, tgl a would target
        itself and become inc a), the resulting instruction is not executed
        until the next time it is reached.

The rest of the electronics seem to place the keypad entry (the number of eggs,
7) in register a, run the code, and then send the value left in register a to
the safe.

PART 1: What value should be sent to the safe?
"""

import re


class Computer:
    def __init__(self, datafile: str, a_start: int):
        self.register = {"a": a_start, "b": 0, "c": 0, "d": 0}
        self.curr_cmd = 0

        with open(datafile) as fp:
            self.insruc = fp.read().splitlines()

        # Each instruction defaults to not being inverted
        self.inverted = [False] * len(self.insruc)

    def extract_var(self, raw_var: str) -> int:
        """
        Test if the variable or a registry reference. Then either parse it or
        extract the current registary value.
        """
        if raw_var[0].isdigit() or raw_var[0] == "-":
            return int(raw_var)
        else:
            return self.register[raw_var]

    def cpy(self, x_value: str, y_reg: str, invert: bool = False):
        """
        Copies x (either an integer or the value of a register) into register y.
        """
        if invert:
            self.jnz(x_value, y_reg)

        else:
            # Ensure that the command can be executed
            if y_reg in self.register:
                self.register[y_reg] = self.extract_var(x_value)
            self.curr_cmd += 1

    def inc(self, x_reg: str, invert: bool = False):
        """
        Increases the value of register x by one.
        """
        if invert:
            self.register[x_reg] -= 1
        else:
            self.register[x_reg] += 1
        self.curr_cmd += 1

    def dec(self, x_reg: str, invert: bool = False):
        """
        Decreases the value of register x by one.
        """
        if invert:
            self.register[x_reg] += 1
        else:
            self.register[x_reg] -= 1
        self.curr_cmd += 1

    def jnz(self, x_test: str, y_jump: str, invert: bool = False):
        """
        Jumps to an instruction y away (positive means forward; negative means
        backward), but only if x is not zero.
        """
        if invert:
            self.cpy(x_test, y_jump)
        else:
            if self.extract_var(x_test) != 0:
                self.curr_cmd += self.extract_var(y_jump)
            else:
                self.curr_cmd += 1

    def tgl(self, x_dist: str, invert: bool = False):
        """
        Toggles the instruction x away (pointing at instructions like jnz does:
        positive means forward; negative means backward).
        """
        if invert:
            if x_dist in self.register:
                self.register[x_dist] += 1

        else:
            idx_invert = self.extract_var(x_dist) + self.curr_cmd

            print(idx_invert)

            if 0 <= idx_invert < len(self.inverted):
                self.inverted[idx_invert] = not self.inverted[idx_invert]

        self.curr_cmd += 1

    def parse_instruc(self, instruc_idx: int):
        """
        Execute the instruction in the particular index.
        """
        cmd = self.insruc[instruc_idx].split()

        if cmd[0] == "cpy":
            self.cpy(cmd[1], cmd[2], self.inverted[instruc_idx])
        elif cmd[0] == "inc":
            self.inc(cmd[1], self.inverted[instruc_idx])
        elif cmd[0] == "dec":
            self.dec(cmd[1], self.inverted[instruc_idx])
        elif cmd[0] == "jnz":
            self.jnz(cmd[1], cmd[2], self.inverted[instruc_idx])
        elif cmd[0] == "tgl":
            self.tgl(cmd[1], self.inverted[instruc_idx])
        else:
            raise Exception(f"Unknown command: '{self.insruc[instruc_idx]}'")

    def final_register_val(self, register: str):
        """
        Calculate the final value of the register after all instructions have
        been run.
        """
        while 0 <= self.curr_cmd < len(self.insruc):
            self.parse_instruc(self.curr_cmd)

        return self.register[register]


if __name__ == "__main__":
    pass
