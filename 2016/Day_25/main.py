"""
--- Day 25: Clock Signal ---

You open the door and find yourself on the roof. The city sprawls away from you
for miles and miles.

There's not much time now - it's already Christmas, but you're nowhere near the
North Pole, much too far to deliver these stars to the sleigh in time.

However, maybe the huge antenna up here can offer a solution. After all, the
sleigh doesn't need the stars, exactly; it needs the timing data they provide,
and you happen to have a massive signal generator right here.

You connect the stars you have to your prototype computer, connect that to the
antenna, and begin the transmission.

Nothing happens.

You call the service number printed on the side of the antenna and quickly
explain the situation. "I'm not sure what kind of equipment you have connected
over there," he says, "but you need a clock signal." You try to explain that
this is a signal for a clock.

"No, no, a clock signal - timing information so the antenna computer knows how
to read the data you're sending it. An endless, alternating pattern of 0, 1, 0,
1, 0, 1, 0, 1, 0, 1...." He trails off.

You ask if the antenna can handle a clock signal at the frequency you would need
to use for the data from the stars. "There's no way it can! The only antenna
we've installed capable of that is on top of a top-secret Easter Bunny
installation, and you're definitely not-" You hang up the phone.

You've extracted the antenna's clock signal generation assembunny code (your
puzzle input); it looks mostly compatible with code you worked on just recently.

This antenna code, being a signal generator, uses one extra instruction:

    -   out x transmits x (either an integer or the value of a register) as the
        next value for the clock signal.

The code takes a value (via register a) that describes the signal to generate,
but you're not sure how it's used. You'll have to find the input to produce the
right signal through experimentation.

PART 1: What is the lowest positive integer that can be used to initialize
        register a and cause the code to output a clock signal of 0, 1, 0, 1...
        repeating forever?
"""

from enum import Enum

Comm = Enum("Comm", [("CPY", 1), ("INC", 2), ("DEC", 3), ("JNZ", 4), ("OUT", 5)])


class SignalGenerator:
    def __init__(self, data_file: str):
        self.commands = []
        self.register = [0, 0, 0, 0]
        self.command_idx = 0
        self.outputs = []

        with open(data_file, "r") as fp:
            for line in fp.readlines():
                parts = []

                # Parse the numbers and convert register accesses to 1000 nums
                for idx, prt in enumerate(line.split()):
                    if idx == 0:
                        parts.append(prt)
                    else:
                        if prt[0].isalpha():
                            parts.append(ord(prt[0]) - ord("a") + 1000)
                        else:
                            parts.append(int(prt))

                # Match the command to the enum
                if parts[0] == "cpy":
                    self.commands.append((Comm.CPY, parts[1], parts[2]))

                elif parts[0] == "inc":
                    self.commands.append((Comm.INC, parts[1]))

                elif parts[0] == "dec":
                    self.commands.append((Comm.DEC, parts[1]))

                elif parts[0] == "jnz":
                    self.commands.append((Comm.JNZ, parts[1], parts[2]))

                elif parts[0] == "out":
                    self.commands.append((Comm.OUT, parts[1]))

                else:
                    raise Exception(f"Unknown instruction '{parts[0]}'!")

    def access_val(self, val: int) -> int:
        """
        Extract a register value or return the original number
        """
        if val < 1000:
            return val
        else:
            return self.register[val - 1000]

    def parse_instruc(self, instruct: tuple):
        """
        Execute an instruction based on the instruction.
        """
        if instruct[0] == Comm.CPY:
            self.register[instruct[2] - 1000] = self.access_val(instruct[1])

        elif instruct[0] == Comm.INC:
            self.register[instruct[1] - 1000] += 1

        elif instruct[0] == Comm.DEC:
            self.register[instruct[1] - 1000] -= 1

        elif instruct[0] == Comm.JNZ:
            if self.access_val(instruct[1]) != 0:
                self.command_idx += self.access_val(instruct[2])
                return

        elif instruct[0] == Comm.OUT:
            self.outputs.append(self.register[instruct[1] - 1000])

        self.command_idx += 1

    def confirm_next_n_outputs(self, n_outs: int) -> bool:
        """
        Determine if the next n outputs match the expected output.
        """
        start_out_cnt = len(self.outputs)
        curr_out_cnt = len(self.outputs)

        # Generate the outputs from the current state
        while len(self.outputs) < start_out_cnt + n_outs:
            self.parse_instruc(self.commands[self.command_idx])

            # If a new output has been added check its the right one
            if len(self.outputs) > curr_out_cnt:

                # All even outputs should be one
                if len(self.outputs) % 2 == 0:
                    if self.outputs[len(self.outputs) - 1] != 1:
                        return False

                # All odd outputs should be zero
                else:
                    if self.outputs[len(self.outputs) - 1] != 0:
                        return False

                # Reset the output count
                curr_out_cnt = len(self.outputs)

        return True

    def lowest_int_for_rep(self) -> int:
        """
        Find the lowest integer that creates an alternating pattern of zeros
        and ones.
        """
        curr_test_value = 0
        max_test_outputs = 100

        while True:
            self.register = [curr_test_value, 0, 0, 0]
            self.command_idx = 0
            self.outputs = []
            curr_out_cnt = len(self.outputs)

            # Generate the outputs from the current state
            while len(self.outputs) < max_test_outputs:

                self.parse_instruc(self.commands[self.command_idx])

                # If a new output has been added check its the right one
                if len(self.outputs) > curr_out_cnt:

                    # All even outputs should be one
                    if len(self.outputs) % 2 == 0:
                        if self.outputs[len(self.outputs) - 1] != 1:
                            break

                    # All odd outputs should be zero
                    else:
                        if self.outputs[len(self.outputs) - 1] != 0:
                            break

                    # Reset the output count
                    curr_out_cnt = len(self.outputs)

            # If the loop is uninterupted then a solution has been found
            else:
                return curr_test_value

            # Otherwise prepare to test the next number
            curr_test_value += 1


if __name__ == "__main__":
    print(f"Part 1 = {SignalGenerator('./data/input.txt').lowest_int_for_rep()}")
