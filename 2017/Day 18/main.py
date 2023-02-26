"""
--- Day 18: Duet ---

You discover a tablet containing some strange assembly code labeled simply
"Duet". Rather than bother the sound card with it, you decide to run the code
yourself. Unfortunately, you don't see any documentation, so you're left to
figure out what the instructions mean on your own.

It seems like the assembly is meant to operate on a set of registers that are
each named with a single letter and that can each hold a single integer. You
suppose each register should start with a value of 0.


# Part 1
What is the value of the recovered frequency (the value of the most recently
played sound) the first time a rcv instruction is executed with a non-zero
value?

"""


class SoundRegister:

    def __init__(self):

        self.values = {}
        self.instructions = []
        self.curr_instruction_idx = 0
        self.played_sounds = []

    def load_instructions(self, file_path: str):

        self.instructions = open(file_path, "r").read().splitlines()

        # Determine how many registers are there?
        register_names = set()

        for instruction in self.instructions:
            register_names.update(instruction.split()[1])

        # Initialise the register
        self.values = {key: 0 for key in register_names}

    def execute_instruction(self, instruction: str):

        # Extract the instruction parts
        instr_parts = instruction.split()

        # Play a sound
        if instruction.startswith("snd"):

            if instr_parts[1].isalpha():
                self.played_sounds.append(self.values[instr_parts[1]])
            else:
                self.played_sounds.append(int(instr_parts[1]))

        # Set a register value
        elif instruction.startswith("set"):

            if instr_parts[2].isalpha():
                self.values[instr_parts[1]] = self.values[instr_parts[2]]
            else:
                self.values[instr_parts[1]] = int(instr_parts[2])

        # Add to a register value
        elif instruction.startswith("add"):

            if instr_parts[2].isalpha():
                self.values[instr_parts[1]] += self.values[instr_parts[2]]
            else:
                self.values[instr_parts[1]] += int(instr_parts[2])

        # Multiply a register value
        elif instruction.startswith("mul"):

            if instr_parts[2].isalpha():
                self.values[instr_parts[1]] *= self.values[instr_parts[2]]
            else:
                self.values[instr_parts[1]] *= int(instr_parts[2])

        # Get the modulus of a register value
        elif instruction.startswith("mod"):

            if instr_parts[2].isalpha():
                self.values[instr_parts[1]] %= self.values[instr_parts[2]]
            else:
                self.values[instr_parts[1]] %= int(instr_parts[2])

        # Recover the last sound played
        elif instruction.startswith("rcv"):

            if self.played_sounds and self.played_sounds[-1] != 0:
                print(f"Recovered sound: {self.played_sounds[-1]}")

        # Skip instructions
        elif instruction.startswith("jgz"):

            if instr_parts[1].isalpha():
                test_val = self.values[instr_parts[1]]
            else:
                test_val = int(instr_parts[1])

            if test_val <= 0:
                return
            elif instr_parts[2].isalpha():
                self.curr_instruction_idx += self.values[instr_parts[2]]-1
            else:
                self.curr_instruction_idx += int(instr_parts[2])-1

    def run_all_instructions(self):

        while self.curr_instruction_idx < len(self.instructions):
            self.execute_instruction(
                self.instructions[self.curr_instruction_idx])
            self.curr_instruction_idx += 1


sample = SoundRegister()
sample.load_instructions("data/input.txt")
sample.run_all_instructions()

print()
