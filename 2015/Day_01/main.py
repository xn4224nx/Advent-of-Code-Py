"""
--- Day 1: Not Quite Lisp ---

Santa is trying to deliver presents in a large apartment building, but
he can't find the right floor - the directions he got are a little
confusing. He starts on the ground floor (floor 0) and then follows the
instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a
closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he
will never find the top or bottom floors.

PART 1: To what floor do the instructions take Santa?

PART 2: What is the position of the character that causes Santa to first
        enter the basement?
"""


def final_floor(direction_file: str, find_base_idx=False) -> int:
    """
    Using a direction file solely containing ) and ( work out the final
    floor Santa ends up on. We assume Santa starts at floor zero

    The flag `find_base_idx` means the function will return the index of
    the instruction character that first
    takes Santa into the basement, ie when the floor first has the value
    -1.

    """
    floor = 0

    # Read the entire file into one big string
    with open(direction_file) as fp:
        dirs = fp.read()

    # Iterate over every instruction and move up and down based on it
    for idx, char in enumerate(dirs):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

        # Basement check
        if find_base_idx and floor == -1:
            return idx + 1

    return floor


if __name__ == "__main__":
    print(f"The answer to part 1 = {final_floor('./data/input.txt')}")
    print(f"The answer to part 2 = {final_floor('./data/input.txt', True)}")
