"""
--- Day 2: Dive! ---

Now, you need to figure out how to pilot this thing.

It seems like the submarine can take a series of commands like forward 1,
down 2, or up 3:

    - forward X increases the horizontal position by X units.
    - down X increases the depth by X units.
    - up X decreases the depth by X units.

Note that since you're on a submarine, down and up affect your depth, and so
they have the opposite result of what you might expect.

The submarine seems to already have a planned course (your puzzle input). You
should probably figure out where it's going. Your horizontal position and depth
both start at 0.

In addition to horizontal position and depth, you'll also need to track a third
value, aim, which also starts at 0. The commands also mean something entirely
different than you first thought:

    - down X increases your aim by X units.
    - up X decreases your aim by X units.
    - forward X does two things:
        - It increases your horizontal position by X units.
        - It increases your depth by your aim multiplied by X.

Calculate the horizontal position and depth you would have after following the
planned course.

    Part 1: What do you get if you multiply your final horizontal position by
            your final depth?

    Part 2: If you use the third value aim to interpret the instructions. What
            do you get if you multiply your final horizontal position by your
            final depth?

"""


class SubNavigation:

    def __init__(self, instructions_path: str, aim_move=False):

        # Submarine Start Position
        self.x_pos = 0
        self.y_pos = 0

        # Load and parse the instructions
        self.instructs = open(instructions_path, "r").read().splitlines()

        # Modify the instructions with aim
        self.aim_move = aim_move
        self.aim = 0

    def show_instructions(self):
        """
        Print the submarine instructions to standard out.
        """
        [print(x) for x in self.instructs]

    def execute_instr(self, instr: str):
        """
        Run one instruction defined by the string `instr`. Extract the command
        and the direction from the instruction string and change the submarine
        position according to their values.
        """

        # Extract the command and magnitude
        comm, mag = instr.split(" ", 1)

        # Parse the magnitude str to a number
        mag = int(mag)

        # Execute the instructions
        if comm == "forward" and not self.aim_move:
            self.x_pos += mag

        elif comm == "up" and not self.aim_move:
            self.y_pos -= mag

        elif comm == "down" and not self.aim_move:
            self.y_pos += mag

        # Execute the aim instructions
        elif comm == "forward" and self.aim_move:
            self.x_pos += mag
            self.y_pos += mag * self.aim

        elif comm == "up" and self.aim_move:
            self.aim -= mag

        elif comm == "down" and self.aim_move:
            self.aim += mag

        else:
            raise Exception(f"Command '{comm}' not recognised.")

    def execute_all_instructions(self):
        """
        Move the submarine according to the instructions
        """

        # Iterate over all the instructions
        for instr in self.instructs:
            self.execute_instr(instr)

    def show_position(self):
        print(self.x_pos, self.y_pos)


sample_dive = SubNavigation("./data/input.txt")
sample_dive.execute_all_instructions()

print(f"Answer to part 1: {sample_dive.x_pos * sample_dive.y_pos}")

sample_dive = SubNavigation("./data/input.txt", True)
sample_dive.execute_all_instructions()

print(f"Answer to part 2: {sample_dive.x_pos * sample_dive.y_pos}")
