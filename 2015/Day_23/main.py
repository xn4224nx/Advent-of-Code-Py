"""
--- Day 23: Opening the Turing Lock ---

Little Jane Marie just got her very first computer for Christmas from some
unknown benefactor. It comes with instructions and an example program, but the
computer itself seems to be malfunctioning. She's curious what the program
does, and would like you to help her run it

The manual explains that the computer supports two registers and six
instructions (truly, it goes on to remind the reader, a state-of-the-art
technology). The registers are named a and b, can hold any non-negative
integer, and begin with a value of 0. The instructions are as follows:

    -   hlf r sets register r to half its current value, then continues with
        the next instruction.

    -   tpl r sets register r to triple its current value, then continues with
        the next instruction.

    -   inc r increments register r, adding 1 to it, then continues with the
        next instruction.

    -   jmp offset is a jump; it continues with the instruction offset away
        relative to itself.

    -   jie r, offset is like jmp, but only jumps if register r is even ("jump
        if even").

    -   jio r, offset is like jmp, but only jumps if register r is 1 ("jump if
        one", not odd).

All three jump instructions work with an offset relative to that instruction.
The offset is always written with a prefix + or - to indicate the direction of
the jump (forward or backward, respectively). For example, jmp +1 would simply
continue with the next instruction, while jmp +0 would continuously jump back
to itself forever.

The program exits when it tries to run an instruction beyond the ones defined.

PART 1: What is the value in register b when the program in your puzzle input
        is finished executing?
"""


class Register:
    """
    Simulate the register of a basic computer being changing the values of its
    two values `a` and `b`. The `instr_idx` is the index of the next
    instruction to be executed.
    """

    def __init__(self):
        self.values = {"a": 0, "b": 0}
        self.instr_idx = 0

    def read_instr(self, file_path: str):
        """
        Read the raw instructions from disk and keep them in a list of strings
        each element representing a single instruction.
        """
        with open(file_path, "r") as fp:
            self.all_instr = [x.strip() for x in fp.readlines()]

    def execute_instr(self, instr: str):
        """
        Modify the register based on a single raw instruction.
        """
        com, dets = instr.split(maxsplit=1)

        if com == "hlf":
            self.values[dets] //= 2
            self.instr_idx += 1

        elif com == "tpl":
            self.values[dets] *= 3
            self.instr_idx += 1

        elif com == "inc":
            self.values[dets] += 1
            self.instr_idx += 1

        elif com == "jmp":
            self.instr_idx += int(dets)

        elif com == "jie":
            reg, inc = dets.split(", ", maxsplit=1)
            if self.values[reg] % 2 == 0:
                self.instr_idx += int(inc)
            else:
                self.instr_idx += 1

        elif com == "jio":
            reg, inc = dets.split(", ", maxsplit=1)
            if self.values[reg] == 1:
                self.instr_idx += int(inc)
            else:
                self.instr_idx += 1

        else:
            raise Exception(f"Unrecognised instruction '{instr}'")

    def run_all_instr(self, reg: str) -> int:
        """
        Execute all the instructions stored in the instance of the class. Then
        calculate the value of the register specified by `reg`.
        """
        # Keep executing instructions until the index goes outside the range
        while self.instr_idx >= 0 and self.instr_idx < len(self.all_instr):
            self.execute_instr(self.all_instr[self.instr_idx])

        return self.values[reg]


if __name__ == "__main__":
    ljm = Register()
    ljm.read_instr("./data/input.txt")
    print(f"Part 1 = {ljm.run_all_instr('b')}")
