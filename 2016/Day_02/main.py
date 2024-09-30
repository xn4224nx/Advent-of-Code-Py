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
"""


class SecSystem:
    """
    Model the Easter Bunnies security system.
    """

    def __init__(self, keypad, start_pnt):
        self.keypad = keypad
        self.start_pnt = start_pnt
        self.pressed_buttons = ""

    def read_bathrm_codes(self, file_path: str):
        """
        Open the file that has the bathroom instructions and store it within the
        class instance.
        """
        pass

    def execute_instr(self, instr: str):
        """
        Move the current cursor according to the instruction.
        """
        pass

    def find_buttons_pressed(self) -> str:
        """
        Execute all the instructions and find the buttons that got pressed and
        return a string of the buttons pressed.
        """
        pass


if __name__ == "__main__":
    pass
