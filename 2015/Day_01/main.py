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

"""


def final_floor(direction_file: str) -> int:
    """
    Using a direction file solely containing ) and ( work out the final
    floor Santa ends up on. We assume Santa starts at floor zero
    """
    floor = 0

    # Read the entire file into one big string
    with open(direction_file) as fp:
        dirs = fp.read()

    # Iterate over every instruction and move up and down based on it
    for char in dirs:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

    return floor


if __name__ == "__main__":
    print(f"The answer to part 1 = {final_floor('./data/input.txt')}")
