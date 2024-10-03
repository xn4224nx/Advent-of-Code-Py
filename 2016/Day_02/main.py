"""
--- Day 2: Bathroom Security ---

You arrive at Easter Bunny Headquarters under cover of darkness. However, you
left in such a rush that you forgot to use the bathroom! Fancy office buildings
like this one usually have keypad locks on their bathrooms, so you search the
front desk for the code.

"In order to improve security," the document you find says, "bathroom codes will
no longer be written down. Instead, please memorize and follow the procedure
below to access the bathrooms."

The document goes on to explain that each button to be pressed can be found by
starting on the previous button and moving to adjacent buttons on the keypad: U
moves up, D moves down, L moves left, and R moves right. Each line of
instructions corresponds to one button, starting at the previous button (or, for
the first line, the "5" button); press whatever button you're on at the end of
each line. If a move doesn't lead to a button, ignore it.

PART 1: Your puzzle input is the instructions from the document you found at the
        front desk. What is the bathroom code?

You finally arrive at the bathroom (it's a several minute walk from the lobby so
visitors can behold the many fancy conference rooms and water coolers on this
floor) and go to punch in the code. Much to your bladder's dismay, the keypad is
not at all like you imagined it. Instead, you are confronted with the result of
hundreds of man-hours of bathroom-keypad-design meetings:

    1
  2 3 4
5 6 7 8 9
  A B C
    D

You still start at "5" and stop when you're at an edge.

PART 2: Using the same instructions in your puzzle input, what is the correct
        bathroom code?
"""


class SecSystem:
    """
    Model the Easter Bunnies security system.
    """

    def __init__(self, keypad, start_pnt):
        self.keypad = keypad
        self.start_pnt = start_pnt
        self.pressed_buttons = ""
        self.curr_loc = start_pnt

    def read_bathrm_codes(self, file_path: str):
        """
        Open the file that has the bathroom instructions and store it within the
        class instance.
        """
        with open(file_path) as fp:
            self.codes = [x for x in fp.read().splitlines()]

    def execute_instr(self, instr: str):
        """
        Move the current cursor according to the instruction.
        """
        new_loc = None

        if instr == "U" and self.curr_loc[0] > 0:
            new_loc = (self.curr_loc[0] - 1, self.curr_loc[1])

        elif instr == "D" and self.curr_loc[0] < len(self.keypad) - 1:
            new_loc = (self.curr_loc[0] + 1, self.curr_loc[1])

        elif instr == "L" and self.curr_loc[1] > 0:
            new_loc = (self.curr_loc[0], self.curr_loc[1] - 1)

        elif instr == "R" and self.curr_loc[1] < len(self.keypad[0]) - 1:
            new_loc = (self.curr_loc[0], self.curr_loc[1] + 1)

        # If the new instruction would take the key pad out of bounds revert it
        if new_loc is not None:
            if self.keypad[new_loc[0]][new_loc[1]] is None:
                return
            else:
                self.curr_loc = new_loc

    def find_buttons_pressed(self) -> str:
        """
        Execute all the instructions and find the buttons that got pressed and
        return a string of the buttons pressed.
        """
        for move_chars in self.codes:

            # Move the cursor around and save the last char it lands on
            for instr in move_chars:
                self.execute_instr(instr)

            self.pressed_buttons += self.keypad[self.curr_loc[0]][self.curr_loc[1]]

        return self.pressed_buttons


if __name__ == "__main__":
    ebh = SecSystem([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]], (1, 1))
    ebh.read_bathrm_codes("./data/input.txt")
    print(f"Part 1 = {ebh.find_buttons_pressed()}")

    ebh = SecSystem(
        [
            [None, None, "1", None, None],
            [None, "2", "3", "4", None],
            ["5", "6", "7", "8", "9"],
            [None, "A", "B", "C", None],
            [None, None, "D", None, None],
        ],
        (2, 0),
    )
    ebh.read_bathrm_codes("./data/input.txt")
    print(f"Part 2 = {ebh.find_buttons_pressed()}")
