"""
--- Day 7: Amplification Circuit ---

Based on the navigational maps, you're going to need to send more power to your
ship's thrusters to reach Santa in time. To do this, you'll need to configure a
series of amplifiers already installed on the ship.

There are five amplifiers connected in series; each one receives an input signal
and produces an output signal. They are connected such that the first
amplifier's output leads to the second amplifier's input, the second amplifier's
output leads to the third amplifier's input, and so on. The first amplifier's
input value is 0, and the last amplifier's output leads to your ship's
thrusters.

        O-------O  O-------O  O-------O  O-------O  O-------O
    0 ->| Amp A |->| Amp B |->| Amp C |->| Amp D |->| Amp E |-> (to thrusters)
        O-------O  O-------O  O-------O  O-------O  O-------O

The Elves have sent you some Amplifier Controller Software (your puzzle input),
a program that should run on your existing Intcode computer. Each amplifier will
need to run a copy of the program.

When a copy of the program starts running on an amplifier, it will first use an
input instruction to ask the amplifier for its current phase setting (an integer
from 0 to 4). Each phase setting is used exactly once, but the Elves can't
remember which amplifier needs which phase setting.

The program will then call another input instruction to get the amplifier's
input signal, compute the correct output signal, and supply it back to the
amplifier with an output instruction. (If the amplifier has not yet received an
input signal, it waits until one arrives.)

Your job is to find the largest output signal that can be sent to the thrusters
by trying every possible combination of phase settings on the amplifiers. Make
sure that memory is not shared or reused between copies of the program.

For example, suppose you want to try the phase setting sequence 3,1,2,4,0, which
would mean setting amplifier A to phase setting 3, amplifier B to setting 1, C
to 2, D to 4, and E to 0. Then, you could determine the output signal that gets
sent from amplifier E to the thrusters with the following steps:

        -   Start the copy of the amplifier controller software that will run on
            amplifier A. At its first input instruction, provide it the
            amplifier's phase setting, 3. At its second input instruction,
            provide it the input signal, 0. After some calculations, it will use
            an output instruction to indicate the amplifier's output signal.

        -   Start the software for amplifier B. Provide it the phase setting (1)
            and then whatever output signal was produced from amplifier A. It
            will then produce a new output signal destined for amplifier C.

        -   Start the software for amplifier C, provide the phase setting (2)
            and the value from amplifier B, then collect its output signal.

        -   Run amplifier D's software, provide the phase setting (4) and input
            value, and collect its output signal.

        -   Run amplifier E's software, provide the phase setting (0) and input
            value, and collect its output signal.

The final output signal from amplifier E would be sent to the thrusters.
However, this phase setting sequence may not have been the best one; another
sequence might have sent a higher signal to the thrusters.

Here are some example programs:

        -   Max thruster signal 43210 (from phase setting sequence 4,3,2,1,0):

            3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0

        -   Max thruster signal 54321 (from phase setting sequence 0,1,2,3,4):

            3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,
            99,0,0

        -   Max thruster signal 65210 (from phase setting sequence 1,0,4,3,2):

            3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,
            33,31,31,1,32,31,31,4,31,99,0,0,0

PART 1: Try every combination of phase settings on the amplifiers. What is the
        highest signal that can be sent to the thrusters?
"""

from itertools import permutations


class Amplifier:
    def __init__(self, program_file: str):
        self.ptr = 0
        self.phase_setting = None
        self.input_signal = None
        self.outputs = []

        # Read the initial state of the program memory
        with open(program_file, "r") as fp:
            self.orginal_mem = [int(x) for x in fp.read().split(",")]

        self.mem = self.orginal_mem[:]

    def curr_params(self) -> (int, int, int, int):
        """
        For the current instruction value deconstruct the opcode and the three
        parameters.
        """
        return (
            self.mem[self.ptr] % 100,
            self.mem[self.ptr] % 1000 // 100,
            self.mem[self.ptr] % 10000 // 1000,
            self.mem[self.ptr] % 100000 // 10000,
        )

    def curr_cmd(self) -> int:
        """
        Execute the command pointed to by the current pointer and return the
        commands opcode.
        """
        opcode, pram1, pram2, pram3 = self.curr_params()

        # Opcode 99 - Exit
        if opcode == 99:
            return opcode

        # Resolve the parameters
        if (
            pram1 == 0
            and self.ptr + 1 < len(self.mem)
            and self.mem[self.ptr + 1] < len(self.mem)
        ):
            pram1 = self.mem[self.mem[self.ptr + 1]]
        elif self.ptr + 1 < len(self.mem):
            pram1 = self.mem[self.ptr + 1]

        if (
            pram2 == 0
            and self.ptr + 2 < len(self.mem)
            and self.mem[self.ptr + 2] < len(self.mem)
        ):
            pram2 = self.mem[self.mem[self.ptr + 2]]
        elif self.ptr + 2 < len(self.mem):
            pram2 = self.mem[self.ptr + 2]

        # Opcode 1 - Addition - three parameters
        if opcode == 1:
            self.mem[self.mem[self.ptr + 3]] = pram1 + pram2
            self.ptr += 4

        # Opcode 2 - Multiplication - three parameters
        elif opcode == 2:
            self.mem[self.mem[self.ptr + 3]] = pram1 * pram2
            self.ptr += 4

        # Opcode 3 - Set a value in memory to what the input is - one parameter
        elif opcode == 3:

            # At the first input instruction provide the phase setting
            if self.phase_setting is not None:
                self.mem[self.mem[self.ptr + 1]] = self.phase_setting
                self.phase_setting = None

            # Otherwise provide the input code
            else:
                self.mem[self.mem[self.ptr + 1]] = self.input_signal

            self.ptr += 2

        # Opcode 4 - Output a value - one parameter
        elif opcode == 4:
            self.outputs.append(pram1)
            self.ptr += 2

        # Opcode 5 - jump-if-true - two parameters
        elif opcode == 5:
            if pram1 != 0:
                self.ptr = pram2
            else:
                self.ptr += 3

        # Opcode 6 - jump-if-false - two parameters
        elif opcode == 6:
            if pram1 == 0:
                self.ptr = pram2
            else:
                self.ptr += 3

        # Opcode 7 - less than - three parameters
        elif opcode == 7:
            if pram1 < pram2:
                self.mem[self.mem[self.ptr + 3]] = 1
            else:
                self.mem[self.mem[self.ptr + 3]] = 0
            self.ptr += 4

        # Opcode 8 - equals
        elif opcode == 8:
            if pram1 == pram2:
                self.mem[self.mem[self.ptr + 3]] = 1
            else:
                self.mem[self.mem[self.ptr + 3]] = 0
            self.ptr += 4

        else:
            raise Exception(f"Unknown Opcode: '{opcode}'")

        return opcode

    def final_output(self, input_signal: int, phase_setting: int) -> int:
        """
        For a program input a specific value and return the value the program
        outputs.
        """
        self.phase_setting = phase_setting
        self.input_signal = input_signal

        # Set the program to its intial state
        self.ptr = 0
        self.outputs = []
        self.mem = self.orginal_mem[:]

        # Generate diagnostic codes until the stop code is reached.
        while self.curr_cmd() != 99:
            pass

        return self.outputs[-1]

    def run_phase_setting(self, settings: list[int]) -> int:
        """
        What is the final thruster signal value from a specific phase setting?
        """
        input_value = 0

        for p_setting in settings:
            input_value = self.final_output(input_value, p_setting)

        return input_value

    def max_thruster_signal(self) -> (int, list[int]):
        """
        What is the combination of phase settings that will produce the largest
        thruster value from this Amplifier controller software?
        """
        max_comb = None
        max_thrust = 0

        for phase_comb in permutations(range(5)):
            curr_thrust = self.run_phase_setting(list(phase_comb))

            if curr_thrust > max_thrust:
                max_thrust = curr_thrust
                max_comb = list(phase_comb)

        return max_thrust, max_comb


if __name__ == "__main__":
    print(f"Part 1 = {Amplifier('./data/input_0.txt').max_thruster_signal()[0]}")
