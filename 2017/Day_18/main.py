"""

--- Day 18: Duet ---

You discover a tablet containing some strange assembly code labeled simply
"Duet". Rather than bother the sound card with it, you decide to run the code
yourself. Unfortunately, you don't see any documentation, so you're left to
figure out what the instructions mean on your own.

It seems like the assembly is meant to operate on a set of registers that are
each named with a single letter and that can each hold a single integer. You
suppose each register should start with a value of 0.

There aren't that many instructions, so it shouldn't be hard to figure out what
they do. Here's what you determine:

        -   snd X plays a sound with a frequency equal to the value of X.

        -   set X Y sets register X to the value of Y.

        -   add X Y increases register X by the value of Y.

        -   mul X Y sets register X to the result of multiplying the value
            contained in register X by the value of Y.

        -   mod X Y sets register X to the remainder of dividing the value
            contained in register X by the value of Y (that is, it sets X to
            the result of X modulo Y).

        -   rcv X recovers the frequency of the last sound played, but only
            when the value of X is not zero. (If it is zero, the command does
            nothing.)

        -   jgz X Y jumps with an offset of the value of Y, but only if the
            value of X is greater than zero. (An offset of 2 skips the next
            instruction, an offset of -1 jumps to the previous instruction, and
            so on.)

Many of the instructions can take either a register (a single letter) or a
number. The value of a register is the integer it contains; the value of a
number is that number.

After each jump instruction, the program continues with the instruction to
which the jump jumped. After any other instruction, the program continues with
the next instruction. Continuing (or jumping) off either end of the program
terminates it.

For example:

    set a 1
    add a 2
    mul a a
    mod a 5
    snd a
    set a 0
    rcv a
    jgz a -1
    set a 1
    jgz a -2

        -   The first four instructions set a to 1, add 2 to it, square it, and
            then set it to itself modulo 5, resulting in a value of 4.

        -   Then, a sound with frequency 4 (the value of a) is played.

        -   After that, a is set to 0, causing the subsequent rcv and jgz
            instructions to both be skipped (rcv because a is 0, and jgz
            because a is not greater than 0).

        -   Finally, a is set to 1, causing the next jgz instruction to
            activate, jumping back two instructions to another jump, which
            jumps again to the rcv, which ultimately triggers the recover
            operation.

At the time the recover operation is executed, the frequency of the last sound
played is 4.

PART 1: What is the value of the recovered frequency (the value of the most
        recently played sound) the first time a rcv instruction is executed
        with a non-zero value?
"""

import re


class Duo:
    def __init__(self, datafile: str):
        cmd_re = r"([a-z]{3}) (-?[0-9]+|[a-z])\s?(-?[0-9]+|[a-z])?"

        self.idx = 0
        self.played = []
        self.received = []
        self.cmds = []
        self.reg = {}

        with open(datafile, "r") as fp:
            for line in fp.readlines():
                raw = re.match(cmd_re, line)

                tmp_cmd = {"cmd": raw[1]}

                # Parse the first variable
                if any(x.isdigit() for x in raw[2]):
                    tmp_cmd["x"] = int(raw[2])
                else:
                    tmp_cmd["x"] = raw[2]
                    self.reg[raw[2]] = 0

                # If the second variable exists add it in
                if raw[3] is not None:
                    if any(x.isdigit() for x in raw[3]):
                        tmp_cmd["y"] = int(raw[3])
                    else:
                        tmp_cmd["y"] = raw[3]
                        self.reg[raw[3]] = 0

                self.cmds.append(tmp_cmd)

    def parse_value(self, val: int | str) -> int:
        """
        Detect if it as reference to a register or a value. Either way return
        a value. The register's value or the original value.
        """
        if isinstance(val, str):
            return self.reg[val]
        else:
            return val

    def snd(self, x_val: int | str):
        """
        Plays a sound with a frequency equal to the value of x_val.
        """
        self.played.append(self.parse_value(x_val))
        self.idx += 1

    def set_val(self, x_reg: str, y_val: int | str):
        """
        Sets register x_val to the value of y_val.
        """
        self.reg[x_reg] = self.parse_value(y_val)
        self.idx += 1

    def add(self, x_reg: str, y_val: int | str):
        """
        Increases register x_val by the value of y_val.
        """
        self.reg[x_reg] += self.parse_value(y_val)
        self.idx += 1

    def mul(self, x_reg: str, y_val: int | str):
        """
        Sets register x_reg to the result of multiplying the value contained
        in register x_reg by the value of y_val.
        """
        self.reg[x_reg] *= self.parse_value(y_val)
        self.idx += 1

    def mod(self, x_reg: str, y_val: int | str):
        """
        Sets register x_reg to the remainder of dividing the value contained
        in register x_reg by the value of Y (that is, it sets x_reg to the
        result of x_reg modulo Y).
        """
        self.reg[x_reg] %= self.parse_value(y_val)
        self.idx += 1

    def rcv(self, x_val: int | str):
        """
        Recovers the frequency of the last sound played, but only when the
        value of x_val is not zero. (If it is zero, the command does nothing.)
        """
        if self.parse_value(x_val) != 0:
            self.received.append(self.played[-1])
        self.idx += 1

    def jgz(self, x_val: int | str, y_val: int | str):
        """
        Jumps with an offset of the value of y_val, but only if the value of
        x_val is greater than zero. (An offset of 2 skips the next
        instruction, an offset of -1 jumps to the previous instruction, and so
        on.)
        """
        if self.parse_value(x_val) > 0:
            self.idx += self.parse_value(y_val)
        else:
            self.idx += 1

    def execute_cmd(self, cmd_info: dict[str:str]):
        """
        Take a command dictionary and execute one of the above methods based
        on its details.
        """
        match cmd_info["cmd"]:
            case "snd":
                self.snd(cmd_info["x"])

            case "set":
                self.set_val(cmd_info["x"], cmd_info["y"])

            case "add":
                self.add(cmd_info["x"], cmd_info["y"])

            case "mul":
                self.mul(cmd_info["x"], cmd_info["y"])

            case "mod":
                self.mod(cmd_info["x"], cmd_info["y"])

            case "rcv":
                self.rcv(cmd_info["x"])

            case "jgz":
                self.jgz(cmd_info["x"], cmd_info["y"])

            case _:
                raise Exception(f"Unknown command {cmd_info["cmd"]}")

    def first_rcv_execution(self) -> int:
        """
        Find the first recovered frequency when a non-zero rcv command is
        executed.
        """
        while len(self.received) < 1:
            self.execute_cmd(self.cmds[self.idx])

        return self.received[-1]


if __name__ == "__main__":
    pass
