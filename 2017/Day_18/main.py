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

As you congratulate yourself for a job well done, you notice that the
documentation has been on the back of the tablet this entire time. While you
actually got most of the instructions correct, there are a few key differences.
This assembly code isn't about sound at all - it's meant to be run twice at the
same time.

Each running copy of the program has its own set of registers and follows the
code independently - in fact, the programs don't even necessarily run at the
same speed. To coordinate, they use the send (snd) and receive (rcv)
instructions:

        -   snd X sends the value of X to the other program. These values wait
            in a queue until that program is ready to receive them. Each program
            has its own message queue, so a program can never receive a message
            it sent.

        -   rcv X receives the next value and stores it in register X. If no
            values are in the queue, the program waits for a value to be sent to
            it. Programs do not continue to the next instruction until they have
            received a value. Values are received in the order they are sent.

Each program also has its own program ID (one 0 and the other 1); the register p
should begin with this value.

For example:

    snd 1
    snd 2
    snd p
    rcv a
    rcv b
    rcv c
    rcv d

Both programs begin by sending three values to the other. Program 0 sends 1, 2,
0; program 1 sends 1, 2, 1. Then, each program receives a value (both 1) and
stores it in a, receives another value (both 2) and stores it in b, and then
each receives the program ID of the other program (program 0 receives 1; program
1 receives 0) and stores it in c. Each program now sees a different value in its
own copy of register c.

Finally, both programs try to rcv a fourth time, but no data is waiting for
either of them, and they reach a deadlock. When this happens, both programs
terminate.

It should be noted that it would be equally valid for the programs to run at
different speeds; for example, program 0 might have sent all three values and
then stopped at the first rcv before program 1 executed even its first
instruction.

PART 2: Once both of your programs have terminated (regardless of what caused
        them to do so), how many times did program 1 send a value?
"""

import re


class Duo:
    def __init__(self, datafile: str, twin_program: bool = False):
        self.twin_program = twin_program
        self.regs = [{}, {}]
        self.cmds = []
        self.transit = [[], []]
        self.active_prog = 0
        self.idx = [0, 0]
        self.sent_counts = [0, 0]

        # Collect the instructions and the possible registers
        with open(datafile, "r") as fp:
            for line in fp.readlines():
                raw = re.match(r"([a-z]{3}) (-?[0-9]+|[a-z])\s?(-?[0-9]+|[a-z])?", line)

                tmp_cmd = {"cmd": raw[1]}

                # Parse the first variable
                if any(x.isdigit() for x in raw[2]):
                    tmp_cmd["x"] = int(raw[2])
                else:
                    tmp_cmd["x"] = raw[2]
                    self.regs[0][raw[2]] = 0
                    self.regs[1][raw[2]] = 0

                # If the second variable exists add it in
                if raw[3] is not None:
                    if any(x.isdigit() for x in raw[3]):
                        tmp_cmd["y"] = int(raw[3])
                    else:
                        tmp_cmd["y"] = raw[3]
                        self.regs[0][raw[3]] = 0
                        self.regs[1][raw[3]] = 0

                self.cmds.append(tmp_cmd)

        if self.twin_program:
            self.regs[0]["p"] = 0
            self.regs[1]["p"] = 1

    def parse_value(self, val: int | str) -> int:
        """
        Detect if it as reference to a register or a value. Either way return
        a value. The register's value or the original value.
        """
        if isinstance(val, str):
            return self.regs[self.active_prog][val]
        else:
            return val

    def non_active_prog(self) -> int:
        """
        Determine the currently non-active program.
        """
        return (self.active_prog + 1) % len(self.regs)

    def snd(self, x_val: int | str):
        """
        Plays a sound with a frequency equal to the value of x_val if this is
        not a twin_program.

        If this is a twin program send a value to the non-active programs
        transit list.
        """
        if not self.twin_program:
            self.transit[0].append(self.parse_value(x_val))
        else:
            self.transit[self.non_active_prog()].append(self.parse_value(x_val))
            self.sent_counts[self.active_prog] += 1

        self.idx[self.active_prog] += 1

    def set_val(self, x_reg: str, y_val: int | str):
        """
        Sets register x_val to the value of y_val.
        """
        self.regs[self.active_prog][x_reg] = self.parse_value(y_val)
        self.idx[self.active_prog] += 1

    def add(self, x_reg: str, y_val: int | str):
        """
        Increases register x_val by the value of y_val.
        """
        self.regs[self.active_prog][x_reg] += self.parse_value(y_val)
        self.idx[self.active_prog] += 1

    def mul(self, x_reg: str, y_val: int | str):
        """
        Sets register x_reg to the result of multiplying the value contained
        in register x_reg by the value of y_val.
        """
        self.regs[self.active_prog][x_reg] *= self.parse_value(y_val)
        self.idx[self.active_prog] += 1

    def mod(self, x_reg: str, y_val: int | str):
        """
        Sets register x_reg to the remainder of dividing the value contained
        in register x_reg by the value of Y (that is, it sets x_reg to the
        result of x_reg modulo Y).
        """
        self.regs[self.active_prog][x_reg] %= self.parse_value(y_val)
        self.idx[self.active_prog] += 1

    def rcv(self, x_val: int | str):
        """
        Recovers the frequency of the last sound played, but only when the
        value of x_val is not zero. (If it is zero, the command does nothing.)
        if this is not a twin_program.

        Otherwise if this is a twin-program wait for a value to be sent to this
        program.
        """
        if not self.twin_program:
            if self.parse_value(x_val) != 0:
                self.transit[1].append(self.transit[0][-1])
            self.idx[self.active_prog] += 1

        # Extract the last value from the programs transit and set a register
        elif len(self.transit[self.active_prog]) > 0:
            self.regs[self.active_prog][x_val] = self.transit[self.active_prog].pop(0)
            self.idx[self.active_prog] += 1

    def jgz(self, x_val: int | str, y_val: int | str):
        """
        Jumps with an offset of the value of y_val, but only if the value of
        x_val is greater than zero. (An offset of 2 skips the next
        instruction, an offset of -1 jumps to the previous instruction, and so
        on.)
        """
        if self.parse_value(x_val) > 0:
            self.idx[self.active_prog] += self.parse_value(y_val)
        else:
            self.idx[self.active_prog] += 1

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
        while len(self.transit[1]) < 1:
            self.execute_cmd(self.cmds[self.idx[self.active_prog]])

        return self.transit[1][-1]

    def sent_values(self, prog_id: int) -> int:
        """
        After both programs have terminated count the number of times the
        specified program sent a value.
        """
        assert self.twin_program
        while True:

            # Run the current command for both programs
            for prog_id in [0, 1]:
                self.active_prog = prog_id
                self.execute_cmd(self.cmds[self.idx[self.active_prog]])

            # If both programs are waiting for a recieve with nothing coming
            if (
                self.cmds[self.idx[0]]["cmd"] == "rcv"
                and self.cmds[self.idx[1]]["cmd"] == "rcv"
                and len(self.transit[0]) == 0
                and len(self.transit[0]) == 0
            ):
                return self.sent_counts[prog_id]


if __name__ == "__main__":
    print(f"Part 1 = {Duo("./data/input.txt").first_rcv_execution()}")
    print(f"Part 2 = {Duo("./data/input.txt", True).sent_values(1)}")
